# Sistema de Agendamento CRUD 📅

[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-black.svg?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Um sistema simples para gerenciar agendamentos (CRUD - Create, Read, Update, Delete) utilizando uma API RESTful construída com Flask e um banco de dados PostgreSQL. O projeto inclui configuração para containerização com Docker.

---

## ✨ Tecnologias Utilizadas

*   **Backend:**
    *   ![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white) - Linguagem principal.
    *   ![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?style=flat-square&logo=flask&logoColor=white) - Microframework web.
    *   ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white) - ORM para interação com o banco de dados.
    *   ![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-Integration-red?style=flat-square) - Integração do SQLAlchemy com Flask.
    *   ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=flat-square&logo=postgresql&logoColor=white) - Banco de dados relacional.
    *   ![Psycopg2](https://img.shields.io/badge/Psycopg2-Driver-blue?style=flat-square) - Adaptador PostgreSQL para Python.
    *   ![Alembic](https://img.shields.io/badge/Alembic-Migrations-lightgrey?style=flat-square) - Ferramenta de migração de schema de banco de dados.
    *   ![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Management-60A5FA?style=flat-square&logo=poetry&logoColor=white) - Gerenciamento de dependências e pacotes.
    *   ![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-e92063?style=flat-square) - Validação de dados (nos Schemas).
    *   ![Flask-RESTX](https://img.shields.io/badge/Flask--RESTX-API%20Docs%20%26%20Helpers-4EA8B6?style=flat-square) - Extensão Flask para criação de APIs RESTful com documentação Swagger.
*   **Frontend (Exemplo - Conforme solicitado para a IA):**
    *   ![HTML5](https://img.shields.io/badge/HTML5-Structure-E34F26?style=flat-square&logo=html5&logoColor=white)
    *   ![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=flat-square&logo=css3&logoColor=white)
    *   ![JavaScript](https://img.shields.io/badge/JavaScript-Logic-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
*   **Containerização:**
    *   ![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=flat-square&logo=docker&logoColor=white)
    *   ![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Orchestration-2496ED?style=flat-square&logo=docker&logoColor=white)

---

## 📋 Pré-requisitos

Antes de começar, garanta que você tenha instalado:

*   [Git](https://git-scm.com/)
*   [Python 3.12+](https://www.python.org/)
*   [Poetry](https://python-poetry.org/docs/#installation) (Para gerenciamento de dependências do backend)
*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (Geralmente incluído com o Docker Desktop)

---

## 🚀 Configuração e Instalação

Siga estes passos para configurar o ambiente de desenvolvimento:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Vincenzo140/CRUD-de-Sistema-de-Agendamento.git
    cd CRUD-de-Sistema-de-Agendamento
    ```

2.  **Configuração com Docker (Recomendado):**
    *   Docker e Docker Compose cuidarão da configuração do banco de dados e da instalação das dependências do backend.
    *   **Observação:** As credenciais do banco de dados (`user`/`senha`) e o nome do banco (`agendamento`) estão definidos em `docker/compose.yaml` e são usados pela aplicação Flask e pelo Alembic.

3.  **Configuração Manual (Alternativa):**
    *   **Backend:**
        *   Navegue até a pasta `backend`:
            ```bash
            cd backend
            ```
        *   Instale as dependências usando Poetry:
            ```bash
            poetry install
            ```
        *   (Opcional, se o `poetry install` não cobrir tudo ou se preferir): Instale dependências adicionais do `requirements.txt` (verifique se é necessário com Poetry):
            ```bash
            # Dentro do ambiente virtual do Poetry ou globalmente se não usar venv
            # pip install -r requirements.txt
            ```
    *   **Banco de Dados:**
        *   Certifique-se de ter um servidor PostgreSQL rodando.
        *   Crie um banco de dados chamado `agendamento` com um usuário `user` e senha `senha`, ou ajuste as configurações em:
            *   `alembic.ini` (linha `sqlalchemy.url`)
            *   `backend/app_factory.py` (linha `app.config["SQLALCHEMY_DATABASE_URI"]`)
            *   `backend/logger/database/databaseConfig.py` (linha `DATABASE_URL`) - *Idealmente, centralize essa configuração ou use variáveis de ambiente.*
    *   **Migrações do Banco:**
        *   Aplique as migrações do Alembic para criar as tabelas:
            ```bash
            # Certifique-se de estar na raiz do projeto ou ajuste os caminhos
            alembic upgrade head
            ```
            *Nota: Se estiver usando Poetry, execute com `poetry run alembic upgrade head` dentro da pasta `backend`.*

---

## ▶️ Como Executar a Aplicação

**1. Usando Docker Compose (Método Recomendado):**

*   Na raiz do projeto, execute:
    ```bash
    docker compose -f docker/compose.yaml up --build
    ```
*   Isso irá:
    *   Construir a imagem do backend Flask.
    *   Iniciar um container para o backend.
    *   Iniciar um container para o banco de dados PostgreSQL.
    *   Expor a API na porta `8000` (`http://localhost:8000`).
*   **Primeira vez:** Pode ser necessário aplicar as migrações do Alembic *após* os containers estarem rodando se a inicialização do app não as criar automaticamente (o `db.create_all()` pode criar, mas Alembic é mais robusto para evoluções). Você pode entrar no container do backend para isso:
    ```bash
    docker exec -it flask-app bash  # Ou o nome do seu container backend
    # Dentro do container:
    alembic upgrade head
    exit
    ```

**2. Executando Manualmente (Sem Docker):**

*   **Banco de Dados:** Certifique-se que seu servidor PostgreSQL esteja rodando.
*   **Backend:**
    *   Navegue até a pasta `backend`:
        ```bash
        cd backend
        ```
    *   Execute a aplicação Flask usando Poetry:
        ```bash
        poetry run python main.py
        ```
    *   A API estará disponível em `http://localhost:8000` (ou a porta definida em `backend/config.py`).
*   **Frontend (Após ser gerado):**
    *   Normalmente, basta abrir o arquivo `index.html` em seu navegador. Se for servido por um servidor web simples, siga as instruções dele.

---

## ⚙️ Endpoints da API

A API oferece os seguintes endpoints para gerenciar agendamentos (base: `http://localhost:8000`):

| Método   | Path                        | Descrição                   | Corpo da Requisição (Exemplo)                                | Resposta (Sucesso)                                                                                                  |
| :------- | :-------------------------- | :-------------------------- | :----------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| `POST`   | `/agendamentos`             | Cria um novo agendamento    | `{ "data": "YYYY-MM-DD", "horario": "HH:MM:SS", ... }`        | `201 Created` - Retorna o agendamento criado (JSON)                                                                 |
| `GET`    | `/agendamentos`             | Lista todos os agendamentos | N/A                                                          | `200 OK` - Retorna uma lista de agendamentos (JSON)                                                                 |
| `GET`    | `/agendamentos/<uuid>`      | Obtém um agendamento por ID | N/A                                                          | `200 OK` - Retorna o agendamento específico (JSON) / `404 Not Found`                                                |
| `PUT`    | `/agendamentos/<uuid>`      | Atualiza um agendamento     | `{ "data": "...", "horario": "...", ... }` (campos opcionais) | `200 OK` - Retorna o agendamento atualizado (JSON) / `404 Not Found`                                                |
| `DELETE` | `/agendamentos/<uuid>`      | Exclui um agendamento       | N/A                                                          | `200 OK` - Retorna o ID do agendamento excluído (JSON) / `404 Not Found`                                            |

*(Consulte os arquivos em `backend/schemas/` para detalhes exatos dos campos)*

---

## 📂 Estrutura do Projeto (Simplificada)