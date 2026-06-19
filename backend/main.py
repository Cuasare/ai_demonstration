from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()
router = APIRouter(prefix="/api")
app.include_router(router)

CSV_PATH = "dados.csv"
COLUNAS = ["id", "nome", "idade"]

def inicializar_csv():
    if not os.path.exists(CSV_PATH):
        pd.DataFrame(columns=COLUNAS).to_csv(CSV_PATH, index=False)

inicializar_csv()

class UsuarioCreate(BaseModel):
    nome: str
    idade: int

class UsuarioUpdate(BaseModel):
    nome: str | None = None
    idade: int | None = None


def ler_csv() -> pd.DataFrame:
    return pd.read_csv(CSV_PATH)

def salvar_csv(df: pd.DataFrame):
    df.to_csv(CSV_PATH, index=False)

def proximo_id(df: pd.DataFrame) -> int:
    if df.empty:
        return 1
    return int(df["id"].max()) + 1


@router.get("/usuarios")
def listar():
    df = ler_csv()
    return df.to_dict(orient="records")


@router.get("/usuarios/{id}")
def buscar(id: int):
    df = ler_csv()
    resultado = df[df["id"] == id]

    if resultado.empty:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return resultado.iloc[0].to_dict()


@router.post("/usuarios", status_code=201)
def inserir(usuario: UsuarioCreate):
    df = ler_csv()

    novo = {
        "id": proximo_id(df),
        "nome": usuario.nome,
        "idade": usuario.idade
    }

    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    salvar_csv(df)

    return novo


@router.put("/usuarios/{id}")
def atualizar(id: int, dados: UsuarioUpdate):
    df = ler_csv()
    idx = df.index[df["id"] == id]

    if idx.empty:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if dados.nome is not None:
        df.loc[idx, "nome"] = dados.nome
    if dados.idade is not None:
        df.loc[idx, "idade"] = dados.idade

    salvar_csv(df)
    return df.loc[idx[0]].to_dict()


@router.delete("/usuarios/{id}", status_code=200)
def deletar(id: int):
    df = ler_csv()
    existe = df[df["id"] == id]

    if existe.empty:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    df = df[df["id"] != id]
    salvar_csv(df)

    return {"detail": f"Usuário {id} deletado"}