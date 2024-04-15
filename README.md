# Cadastro de Clientes e Contatos

Este projeto desenvolve uma aplicação web completa para gerenciamento de clientes e seus respectivos contatos. A aplicação utiliza as seguintes tecnologias:

## Tecnologias Utilizadas

O Nunes Sports foi construído com as seguintes tecnologias:

- **Backend**:
  - Python 3
  - Flask (framework web)
  - SQLAlchemy (ORM)
  - PostgreSQL (banco de dados)
    
- **Frontend**:
  - HTML
  - CSS
  - Bootstrap
  - JavaScript
    
- **Testes**:
  - Pytest

## Funcionalidades

- **Conexão com o Banco de Dados**: Utiliza o SQLAlchemy para conectar e interagir com o banco de dados PostgreSQL.

- **API de Customers**: Rotas completas para CRUD de clientes, além de uma rota para gerar relatório que mostra o cliente e seus contatos.

- **API de Contacts**: Rotas completas para CRUD de contatos.

- **Tela de Login com Autenticação com o Google**: Permite que os usuários façam login utilizando suas contas do Google.

- **Dashboard**: Tela principal que apresenta opções para utilizar cada rota de clientes e contatos.

- **Relatório Cliente-Contatos**: Exibe um relatório na página de dashboard que mostra os clientes e seus contatos vinculados.

  ![image](https://github.com/nicolasKormann/roines_customer_manager/assets/104602223/65d0ee02-8f4a-4042-8189-434d7308c2aa)

  ![image](https://github.com/nicolasKormann/roines_customer_manager/assets/104602223/61bf669f-c4d8-4045-ae5a-ea961c1bc775)



## A ser desenvolvido

- **Frontend**: Desenvolver uma interface de usuário para interagir com as rotas de visualizar, adicionar, editar e excluir clientes e contatos.

## Rotas API

### Rotas da API de Customers:
- **Listar Todos os Clientes:**
  - Método: GET
  - Rota: /customers
  - Descrição: Retorna uma lista de todos os clientes cadastrados.

- **Editar Cliente:**
  - Método: PUT
  - Rota: /customers/\<id>
  - Descrição: Edita as informações do cliente com o ID especificado.

- **Criar Cliente:**
  - Método: POST
  - Rota: /customers
  - Descrição: Cria um novo cliente com as informações fornecidas.

- **Deletar Cliente:**
  - Método: DELETE
  - Rota: /customers/\<id>
  - Descrição: Exclui o cliente com o ID especificado.

- **Relatório de Cliente e Contatos:**
  - Método: GET
  - Rota: /customers/report
  - Descrição: Retorna um relatório que mostra os clientes e seus contatos vinculados.


### Rotas da API de Contacts:
- **Listar Todos os Contatos:**
  - Método: GET
  - Rota: /contacts
  - Descrição: Retorna uma lista de todos os contatos cadastrados.

- **Editar Contato:**
  - Método: PUT
  - Rota: /contacts/\<id>
  - Descrição: Edita as informações do contato com o ID especificado.

- **Criar Contato:**
  - Método: POST
  - Rota: /contacts
  - Descrição: Cria um novo contato com as informações fornecidas.

- **Deletar Contato:**
  - Método: DELETE
  - Rota: /contacts/\<id>
  - Descrição: Exclui o contato com o ID especificado.

## Como Executar Localmente

1. Clone este repositório.

```
git clone https://github.com/nicolasKormann/roines_customer_manager.git
```

2. Instale as dependências do backend.

```
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente necessárias.

5. Inicie o servidor.
   
```
python3 app.py
```

5. Rode o projeto em: https://localhost:5000/login


