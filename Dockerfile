# ─────────── Builder ───────────
FROM ghcr.io/astral-sh/uv:0.6.11-python3.12-bookworm-slim AS builder

WORKDIR /SchoolReminder

# Copy project metadata and source
COPY pyproject.toml uv.lock ./
COPY src/ src/

# Install dependencies & our package into .venv
RUN uv sync --locked 

# ─────────── Runtime ───────────
FROM python:3.12-slim-bookworm

WORKDIR /SchoolReminder

# pull in only the venv from builder
COPY --from=builder /SchoolReminder/.venv /venv
ENV PATH="/venv/bin:$PATH"

# copy your actual code (no build tools)
COPY src/ src/

# Start the bot
ENTRYPOINT ["python3", "-m", "app.main"]
