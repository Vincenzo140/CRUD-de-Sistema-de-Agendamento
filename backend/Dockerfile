FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry env use python3.12

RUN poetry config virtualenvs.in-project true

RUN poetry install

COPY requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "main.py"]
