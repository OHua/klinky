FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip install poetry
WORKDIR /bot
COPY poetry.lock pyproject.toml /bot/
RUN poetry config virtualenvs.create false &&\
    poetry install --no-root --no-dev --no-interaction --no-ansi
COPY . /bot
CMD python src/main.py
