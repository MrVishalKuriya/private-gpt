FROM python:3.12-slim

# Install uv for fast dependency management
COPY --from=astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install system dependencies required for psycopg and building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy configuration and lock files
COPY pyproject.toml uv.lock ./

# Install project dependencies using uv (skips building if wheels exist)
RUN uv sync --frozen --no-dev

# Copy the rest of the application
COPY . .

ENV PYTHONPATH=/app
ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
