# Sistema de Agendamento CRUD 📅

[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-black.svg?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Um sistema simples para gerenciar agendamentos (CRUD - Create, Read, Update, Delete) utilizando uma API RESTful construída com Flask, um banco de dados PostgreSQL e uma interface frontend básica em HTML/CSS/JS. O projeto inclui configuração para containerização com Docker.

---

## ✨ Tecnologias Utilizadas

*   **Backend:**
    *   ![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white) - Linguagem principal.
    *   ![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?style=flat-square&logo=flask&logoColor=white) - Microframework web.
    *   ![Flask-CORS](https://img.shields.io/badge/Flask--CORS-Cross--Origin-lightgrey?style=flat-square) - Para permitir requisições do frontend.
    *   ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white) - ORM para interação com o banco de dados.
    *   ![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-Integration-red?style=flat-square) - Integração do SQLAlchemy com Flask.
    *   ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=flat-square&logo=postgresql&logoColor=white) - Banco de dados relacional.
    *   ![Psycopg2](https://img.shields.io/badge/Psycopg2-Driver-blue?style=flat-square) - Adaptador PostgreSQL para Python.
    *   ![Alembic](https://img.shields.io/badge/Alembic-Migrations-lightgrey?style=flat-square) - Ferramenta de migração de schema de banco de dados.
    *   ![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Management-60A5FA?style=flat-square&logo=poetry&logoColor=white) - Gerenciamento de dependências e pacotes.
    *   ![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-e92063?style=flat-square) - Validação de dados (nos Schemas).
    *   ![Flask-RESTX](https://img.shields.io/badge/Flask--RESTX-API%20Docs%20%26%20Helpers-4EA8B6?style=flat-square) - Extensão Flask para criação de APIs RESTful com documentação Swagger (embora não explicitamente usada para docs aqui, está como dependência).
*   **Frontend:**
    *   ![HTML5](https://img.shields.io/badge/HTML5-Structure-E34F26?style=flat-square&logo=html5&logoColor=white) - Estrutura da página.
    *   ![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=flat-square&logo=css3&logoColor=white) - Estilização visual.
    *   ![JavaScript](https://img.shields.io/badge/JavaScript-Logic%20(Vanilla)-F7DF1E?style=flat-square&logo=javascript&logoColor=black) - Lógica de interação com a API e DOM.
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
*   Um Navegador Web moderno (Chrome, Firefox, Edge, etc.)

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

3.  **Configuração Manual (Alternativa - apenas Backend):**
    *   **Backend:**
        *   Navegue até a pasta `backend`: `cd backend`
        *   Instale as dependências: `poetry install`
    *   **Banco de Dados:**
        *   Garanta um servidor PostgreSQL rodando e acessível.
        *   Crie o banco `agendamento` com usuário `user` e senha `senha`, ou ajuste as strings de conexão em `alembic.ini`, `backend/app_factory.py`, e `backend/logger/database/databaseConfig.py`.
    *   **Migrações:**
        *   Aplique as migrações: `cd backend && poetry run alembic upgrade head` (execute da pasta `backend`).

---

## ▶️ Como Executar a Aplicação

**Importante:** O backend **precisa** estar rodando para que o frontend funcione, pois ele consome a API do backend.

**1. Usando Docker Compose (Método Recomendado):**

*   **Iniciar Backend e Banco de Dados:**
    *   Na raiz do projeto, execute:
        ```bash
        docker compose -f docker/compose.yaml up --build -d
        ```
        *(O `-d` executa em modo detached/background)*
    *   Isso irá iniciar os containers do backend (API em `http://localhost:8000`) e do banco de dados.
*   **Aplicar Migrações (se necessário na primeira vez):**
    *   Verifique os logs do container `flask-app` (`docker logs flask-app`). Se as tabelas não foram criadas automaticamente pelo `db.create_all()` ou se precisar de migrações futuras:
        ```bash
        docker exec -it flask-app bash
        # Dentro do container:
        alembic upgrade head
        exit
        ```
*   **Acessar o Frontend:**
    *   Após o backend estar rodando, abra o arquivo `frontend/index.html` diretamente no seu navegador web.
    *   O frontend fará requisições para `http://localhost:8000`. A configuração do `Flask-CORS` no backend permite essa comunicação.

**2. Executando Manualmente (Sem Docker):**

*   **Banco de Dados:** Certifique-se que seu servidor PostgreSQL configurado manualmente esteja rodando.
*   **Backend:**
    *   Navegue até a pasta `backend`: `cd backend`
    *   Execute a aplicação Flask: `poetry run python main.py`
    *   A API estará disponível em `http://localhost:8000`.
*   **Frontend:**
    *   Abra o arquivo `frontend/index.html` diretamente no seu navegador web.

---

## ⚙️ Endpoints da API

A API oferece os seguintes endpoints para gerenciar agendamentos (base: `http://localhost:8000`):

| Método   | Path                        | Descrição                   | Corpo da Requisição (Exemplo)                                | Resposta (Sucesso)                                                                                                  |
| :------- | :-------------------------- | :-------------------------- | :----------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| `POST`   | `/agendamentos`             | Cria um novo agendamento    | `{ "data": "YYYY-MM-DD", "horario": "HH:MM:SS", ... }`        | `201 Created` - Retorna o agendamento criado (JSON)                                                                 |
| `GET`    | `/agendamentos`             | Lista todos os agendamentos | N/A                                                          | `200 OK` - Retorna `{ "agendamento": [...] }` (JSON)                                                                |
| `GET`    | `/agendamentos/<uuid>`      | Obtém um agendamento por ID | N/A                                                          | `200 OK` - Retorna o agendamento específico (JSON) / `404 Not Found`                                                |
| `PUT`    | `/agendamentos/<uuid>`      | Atualiza um agendamento     | `{ "data": "...", "horario": "...", ... }` (campos opcionais) | `200 OK` - Retorna o agendamento atualizado (JSON) / `404 Not Found`                                                |
| `DELETE` | `/agendamentos/<uuid>`      | Exclui um agendamento       | N/A                                                          | `200 OK` - Retorna `{ "id": "uuid-string" }` (JSON) / `404 Not Found`                                               |

*(Consulte os arquivos em `backend/schemas/` para detalhes exatos dos campos)*

