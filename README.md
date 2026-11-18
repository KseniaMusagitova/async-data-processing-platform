
# Async Data Processing Platform

A Python backend project for building an asynchronous data processing system using FastAPI, Docker, and automated testing.

The project currently supports CSV file uploads and input validation. Future development will introduce background job processing, persistent storage, and job status tracking.

## Current Features

- FastAPI REST application
- Health check endpoint (`GET /health`)
- CSV file upload endpoint
- CSV file validation, including empty-file handling
- Docker Compose development environment
- Automated API testing with pytest and HTTPX

## Planned Features

- Asynchronous processing with Celery and Redis
- Job status tracking
- PostgreSQL persistence
- Retry handling and idempotent processing
- Structured logging
- CI/CD with GitHub Actions

## Tech Stack

**Currently implemented:** Python 3.12, FastAPI, Docker, Docker Compose, pytest, HTTPX.

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

Use the interactive API documentation to explore and test the available endpoints.

### Run tests

```bash
docker compose run --rm --no-deps \
  -v "$PWD/tests:/app/tests:ro" \
  api python -m pytest -q
```

The automated test suite covers API behavior, including CSV upload validation.

## Project Status

**Active development**

Implemented:
- REST API foundation
- Docker-based development environment
- CSV upload and validation
- Automated API tests

Next milestone:
- Background processing with Celery and Redis
- Asynchronous job execution and status tracking

## Development Goals

- Build a reliable backend for processing uploaded datasets.
- Separate API request handling from background processing.
- Introduce persistent job tracking and retry mechanisms.
- Improve reliability through automated testing and CI/CD.
