# Desenvolvimento da Interface Gráfica da API de Usuários

## Objetivo

Desenvolver uma interface gráfica moderna para consumir uma API REST de gerenciamento de usuários.

A interface deve ser simples, responsiva e intuitiva, permitindo realizar todas as operações CRUD disponíveis na API.

---

# Tecnologias

Utilizar:

- React
- TypeScript
- Vite
- Material UI (MUI)
- Axios
- React Query (@tanstack/react-query)

Não utilizar Redux.

Organizar o projeto seguindo boas práticas de separação de responsabilidades.

Exemplo:

```
src/
    api/
    components/
    pages/
    hooks/
    services/
    types/
    utils/
```

---

# API

Base URL

```
http://localhost:8000
```

Todos os endpoints possuem o prefixo:

```
/api
```

---

# Endpoints

## Listar usuários

GET

```
/api/usuarios
```

Retorna todos os usuários.

---

## Buscar usuário

GET

```
/api/usuarios/{id}
```

---

## Inserir usuário

POST

```
/api/usuarios
```

Body:

```json
{
    "nome": "João",
    "idade": 25
}
```

---

## Atualizar usuário

PUT

```
/api/usuarios/{id}
```

Body:

```json
{
    "nome": "Novo nome",
    "idade": 30
}
```

Os campos são opcionais.

---

## Excluir usuário

DELETE

```
/api/usuarios/{id}
```

---

# Modelos

## Usuario

```ts
interface Usuario {
    id: number;
    nome: string;
    idade: number;
}
```

Caso o endpoint de listagem não retorne exatamente este formato, adaptar automaticamente os tipos.

---

# Layout

A aplicação deve possuir apenas uma página.

Estrutura:

```
+-----------------------------------------------------------+
|                    Cadastro de Usuários                   |
+-----------------------------------------------------------+

[ Novo usuário ]

------------------------------------------------------------

Tabela de usuários

------------------------------------------------------------

```

---

# Funcionalidades

## 1. Listagem

Ao abrir a aplicação:

- carregar automaticamente os usuários;
- exibir indicador de carregamento;
- tratar erros de conexão.

A listagem deve utilizar:

- DataGrid do Material UI.

Colunas:

- ID
- Nome
- Idade
- Ações

---

## 2. Inserção

Um botão:

```
Novo usuário
```

abre um Dialog.

Campos:

Nome

Idade

Botões:

Cancelar

Salvar

Após salvar:

- fechar o diálogo;
- atualizar automaticamente a tabela;
- mostrar Snackbar de sucesso.

---

## 3. Edição

Cada linha possui um botão:

```
Editar
```

Ao clicar:

abrir o mesmo Dialog preenchido.

Ao salvar:

realizar PUT.

Atualizar automaticamente a tabela.

---

## 4. Exclusão

Cada linha possui um botão:

```
Excluir
```

Antes de excluir:

mostrar Dialog de confirmação.

Mensagem:

```
Deseja realmente excluir este usuário?
```

Botões:

Cancelar

Excluir

Após excluir:

- atualizar tabela;
- Snackbar de sucesso.

---

## 5. Busca por ID

Acima da tabela adicionar:

```
[ campo ID ]

[ Buscar ]

[ Limpar ]
```

Buscar utiliza:

```
GET /usuarios/{id}
```

Caso encontrado:

mostrar apenas aquele usuário.

Caso não exista:

mostrar mensagem amigável.

---

# Validações

Nome:

- obrigatório
- mínimo 2 caracteres

Idade:

- obrigatória
- inteiro
- maior ou igual a zero

Usar validação no frontend.

Não permitir submissão inválida.

---

# UX

Mostrar:

Loading Circular

Skeletons quando apropriado.

Snackbar para:

- sucesso
- erro

Desabilitar botões durante requisições.

---

# Tratamento de erros

Caso a API retorne:

422

mostrar mensagem:

"Dados inválidos."

Erro de conexão:

"Não foi possível conectar à API."

404:

"Usuário não encontrado."

500:

"Erro interno do servidor."

Nunca exibir stack traces.

---

# React Query

Utilizar React Query para:

- listagem
- busca
- inserção
- edição
- exclusão

Após INSERT/UPDATE/DELETE invalidar automaticamente o cache da listagem.

---

# Axios

Criar uma instância:

```
api.ts
```

com:

- baseURL
- timeout
- interceptors para tratamento de erros

---

# Componentização

Separar:

```
UserTable

UserDialog

DeleteDialog

SearchBar

Loading

ErrorMessage
```

Evitar componentes muito grandes.

---

# Design

Utilizar Material UI.

Preferir:

- AppBar
- Paper
- Dialog
- Snackbar
- DataGrid
- IconButton
- Tooltip

Ícones:

- Add
- Edit
- Delete
- Search
- Refresh

Tema claro.

Espaçamento consistente utilizando o sistema do Material UI.

---

# Qualidade

Utilizar:

- TypeScript estrito
- Hooks
- Componentes funcionais
- Código limpo
- Nomes descritivos
- Tipagem forte

Evitar:

- any
- código duplicado
- lógica de negócio dentro dos componentes visuais

---

# Objetivo Final

Ao finalizar, o usuário deve conseguir:

- visualizar usuários;
- criar usuários;
- editar usuários;
- excluir usuários;
- buscar usuário por ID;

Tudo através de uma interface moderna, organizada, responsiva e com excelente experiência de uso.

A aplicação deve estar pronta para execução após:

```bash
npm install
npm run dev
```

sem necessidade de alterações adicionais.
