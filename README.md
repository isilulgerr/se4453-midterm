# SE4453 Final Project - Flask Backend Deployment on Azure

## 🧠 Project Overview

This project demonstrates the deployment of a Flask web application on Azure App Service using Docker and GitHub Actions. The backend connects securely to a public PostgreSQL server and fetches secrets from Azure Key Vault.

## 🔧 Tech Stack

- Python (Flask + Gunicorn)
- Azure App Service (Linux)
- Azure Container Registry (ACR)
- Azure PostgreSQL (Public with IP Restriction)
- Azure Key Vault
- GitHub Actions CI/CD
- Docker

## 📁 Project Structure

.
├── app.py # Main Flask app
├── Dockerfile # Docker build config
├── startup.sh # SSH + Gunicorn startup script
├── .env # (Local testing, ignored in Git)
├── .github/
│ └── workflows/
│ └── deploy.yml # GitHub Actions deployment workflow
└── requirements.txt # Dependencies


## 🚀 Deployment Flow

1. Developer pushes to `develop` branch.
2. GitHub Actions triggered:
   - Logs into Azure with `AZURE_CREDENTIALS`.
   - Logs into ACR with `REGISTRY_USERNAME` and `REGISTRY_PASSWORD`.
   - Builds Docker image and pushes to `isilacrgr1.azurecr.io`.
   - Configures App Service to pull image from ACR.
3. App Service starts the container using `startup.sh`.

## 🔐 Secrets Management

Secrets are managed via Azure Key Vault:
- `POSTGRES_HOST`
- `POSTGRES_DATABASE`
- `POSTGRES_USERNAME`
- `POSTGRES_PASSWORD`

They are loaded inside `app.py` using `os.environ.get()`.

## 🔎 Endpoints

- `GET /hello`: Connects to the database and returns `Hello from DB!`.

## ✅ Requirements Checklist

| Requirement                        | Status |
|-----------------------------------|--------|
| Dockerfile with SSH + Gunicorn    | ✅     |
| Azure Container Registry setup    | ✅     |
| GitHub Actions CI/CD              | ✅     |
| PostgreSQL IP restricted          | ✅     |
| Key Vault secrets                 | ✅     |
| Automatic Deployment via GitHub   | ✅     |
| Secure DB connection (SSL)        | ✅     |


