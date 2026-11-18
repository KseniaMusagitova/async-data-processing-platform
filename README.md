# Async Data Processing Platform

A Python backend project for building an asynchronous data processing system using FastAPI, Docker, and automated testing.

## Current Features

- FastAPI REST application
- Health check endpoint (`GET /health`)
- Docker Compose development environment
- Automated API testing with Pytest

## Planned Features

- CSV file upload and validation
- Asynchronous processing with Celery and Redis
- Job status tracking
- PostgreSQL persistence
- Retry handling and idempotent processing
- Structured logging
- CI/CD with GitHub Actions

## Tech Stack

**Currently implemented:** Python 3.12, FastAPI, Docker, Pytest, HTTPX.

**Planned:** Celery, Redis, PostgreSQL, GitHub Actions.

## Getting Started

### Requirements

- Docker
- Docker Compose

### Run the application

```bash
docker compose up --build
```

The API will be available at:

- API documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### Run tests

```bash
docker compose run --rm --no-deps \
  -v "$PWD/tests:/app/tests:ro" \
  api python -m pytest -q
```

## Project Status

Active development. The initial API, Docker configuration, and first automated test are implemented.

## Development Goals

This project focuses on writing maintainable Python code, designing reliable APIs, processing data efficiently, and implementing automated tests.
