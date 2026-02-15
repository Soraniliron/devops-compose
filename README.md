
# Docker Compose – Flask + Redis + Nginx

Small DevOps project demonstrating a production-like setup using Docker Compose.

## Stack
- Flask (Python)
- Redis (counter persistence)
- Nginx (reverse proxy)
- Docker Compose

## Features
- Multi-container setup
- Internal Docker networking
- Redis volume for persistence
- Healthchecks & restart policies
- Environment variables via .env
- Nginx as entry point (port 80)

## How to run
```bash
docker compose up -d
## Production-style run (no build)

This setup demonstrates running services from pre-built images,
similar to real production environments.

```bash
docker compose up -d
## Architecture

User -> Nginx (port 80) -> Flask app -> Redis

- Nginx acts as a reverse proxy
- Flask application is stateless
- Redis provides persistent storage via Docker volume
- All services communicate over an internal Docker network

## DevOps Highlights

- Docker Compose orchestration
- Healthchecks and restart policies
- Environment-based configuration
- Separation between build-time and run-time
- Production-style execution from images
## Production run (no build)

This project can be run directly from Docker Hub without building locally:

```bash
docker compose up -d
## Scaling
The application supports horizontal scaling of the web service:

```bash
docker compose up -d --scale web=3
## Environments

Run dev:
```bash
docker compose --env-file env/.env.dev up -d

docker compose --env-file env/.env.prod up -d
## Environments

Run dev:
```bash
docker compose --env-file env/.env.dev up -d
