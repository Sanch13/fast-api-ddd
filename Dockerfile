# Использование образа Python с предустановленным uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Установка рабочего каталога
WORKDIR /app

# Включение компиляции байт-кода
ENV UV_COMPILE_BYTECODE=1
# Копирование из кеша вместо создания ссылок, поскольку это смонтированный том
ENV UV_LINK_MODE=copy

# Копируем файлы проекта заранее (pyproject.toml и uv.lock)
COPY pyproject.toml uv.lock /app/

# Установка зависимостей проекта с использованием lock-файла и настроек
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-dev

# Добавление остального исходного кода проекта
COPY fast-api.db .dockerignore /app/

# Добавление исполняемых файлов в начало PATH
ENV PATH="/app/.venv/bin/:$PATH"
