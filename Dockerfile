# Использование образа Python с предустановленным uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Установка рабочего каталога
WORKDIR /app

# Включение компиляции байт-кода
ENV UV_COMPILE_BYTECODE=1
# Копирование из кеша вместо создания ссылок, поскольку это смонтированный том
ENV UV_LINK_MODE=copy

# Установка зависимостей проекта с использованием lock-файла и настроек
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev \

# Добавление остального исходного кода проекта и его установка
ADD COPY pyproject.toml uv.lock /

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev \

# Добавление исполняемых файлов в начало PATH
ENV PATH="/app/.venv/bin:$PATH"

# Сброс точки входа, чтобы не вызывать `uv`
ENTRYPOINT []

# Запуск FastAPI-приложения по умолчанию
# Использует `fastapi dev` для включения горячей перезагрузки при изменениях
# Параметр `--host 0.0.0.0` позволяет доступ извне контейнера
# CMD ["fastapi", "dev", "--host", "0.0.0.0", "src/uv_docker_example"]

