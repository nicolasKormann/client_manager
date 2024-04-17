# Cadastro de Clientes e Contatos

Este projeto desenvolve uma aplicação web completa para gerenciamento de clientes e seus respectivos contatos. A aplicação utiliza as seguintes tecnologias:

## Tecnologias Utilizadas

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

- **API de Clientes**: Rotas completas para CRUD de clientes.

- **API de Contatos**: Rotas completas para CRUD de contatos.
  
- **API de Relatório**: Rota completa para relatório Cliente-Contatos

- **Tela de Login com Autenticação com o Google**: Permite que os usuários façam login utilizando suas contas do Google.

- **Dashboard**: Tela principal que apresenta o telatório de Cliente-Contatos e opções para ir para a página de gerenciamento de clientes ou contatos.

- **Relatório Cliente-Contatos**: Exibe um relatório na página de dashboard que mostra os clientes e seus contatos vinculados.

  ![image](https://github.com/nicolasKormann/roines_customer_manager/assets/104602223/65d0ee02-8f4a-4042-8189-434d7308c2aa)

  ![image](https://github.com/nicolasKormann/roines_customer_manager/assets/104602223/e574a4b2-ce69-42f3-8214-f9ebb62346f2)


## A ser desenvolvido

- **Frontend**: Integração do botão editar com o API para atualizar Cliente/Contato

## Rotas API

### Rotas da API para Clientes:
- **Listar Todos os Clientes:**
  - Método: GET
  - Rota: api/customers
  - Descrição: Retorna uma lista de todos os clientes cadastrados.

- **Editar Cliente:**
  - Método: PUT
  - Rota: api/customers/\<id>
  - Descrição: Edita as informações do cliente com o ID especificado.

- **Criar Cliente:**
  - Método: POST
  - Rota: api/customers
  - Descrição: Cria um novo cliente com as informações fornecidas.

- **Deletar Cliente:**
  - Método: DELETE
  - Rota: api/customers/\<id>
  - Descrição: Exclui o cliente com o ID especificado.


### Rotas da API para Contatos:
- **Listar Todos os Contatos:**
  - Método: GET
  - Rota: api/contacts
  - Descrição: Retorna uma lista de todos os contatos cadastrados.

- **Editar Contato:**
  - Método: PUT
  - Rota: api/contacts/\<id>
  - Descrição: Edita as informações do contato com o ID especificado.

- **Criar Contato:**
  - Método: POST
  - Rota: api/contacts
  - Descrição: Cria um novo contato com as informações fornecidas.

- **Deletar Contato:**
  - Método: DELETE
  - Rota: api/contacts/\<id>
  - Descrição: Exclui o contato com o ID especificado.


### Rotas da API para o Relatório:
- **Relatório de Cliente e Contatos:**
  - Método: GET
  - Rota: api/customers/report
  - Descrição: Retorna um relatório que mostra os clientes e seus contatos vinculados.
 
    
## Como Executar Localmente

1. Clone este repositório.

```
git clone https://github.com/nicolasKormann/roines_customer_manager.git
```

2. Altere para a branch stage.

```
git checkout stage
```

3. Instale as dependências do backend.

```
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente necessárias.

5. Inicie o servidor.
   
```
python3 app.py
```

6. Rode o projeto em: https://localhost:5000/login


