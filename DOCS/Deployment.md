# 🚀 Teach Cloud · Production Deployment Architecture & Troubleshooting Guide

Welcome to the definitive **Production Deployment & Troubleshooting Guide** for Teach Cloud. This document details the GitHub Actions CI/CD deployment pipeline (`.github/workflows/deploy.yml`), common deployment failure root causes (including missing runtime dependencies), and step-by-step diagnostic workflows.

---

## 📌 Table of Contents
1. [CI/CD Pipeline Architecture](#1-cicd-pipeline-architecture)
2. [Root Cause Analysis of Production Deployment Failures](#2-root-cause-analysis-of-production-deployment-failures)
   - [Issue 1: Missing Dependency in `requirements.txt` (RESOLVED)](#issue-1-missing-dependency-in-requirementstxt-resolved)
   - [Issue 2: Missing or Misconfigured GitHub Secrets](#issue-2-missing-or-misconfigured-github-secrets)
   - [Issue 3: Port 80/443 Conflicts on Droplet Host](#issue-3-port-80443-conflicts-on-droplet-host)
   - [Issue 4: SSH Authentication & Host Key Failures](#issue-4-ssh-authentication--host-key-failures)
   - [Issue 5: Health Check HTTP Failure (200/301/302 Exits)](#issue-5-health-check-http-failure-200301302-exits)
3. [Step-by-Step Manual Deployment & Recovery Protocol](#3-step-by-step-manual-deployment--recovery-protocol)
4. [Verification Checklist](#4-verification-checklist)

---

## 1. CI/CD Pipeline Architecture

The automated deployment pipeline triggers on every push to the **`production`** branch:

```
[Push to production branch]
          │
          ▼
┌───────────────────────────┐
│  Stage 1: Lint & Test     │ ➔ Installs requirements.txt, runs flake8 & pytest
└─────────┬─────────────────┘
          │ (Pass)
          ▼
┌───────────────────────────┐
│  Stage 2: Build & Push    │ ➔ Builds Docker image & pushes to ghcr.io
└─────────┬─────────────────┘
          │ (Pass)
          ▼
┌───────────────────────────┐
│  Stage 3: Deploy Droplet  │ ➔ SSH into DigitalOcean, pulls image, restarts containers & verifies HTTP
└───────────────────────────┘
```

---

## 2. Root Cause Analysis of Production Deployment Failures

### Issue 1: Missing Dependency in `requirements.txt` (RESOLVED)
- **Symptom**: Stage 1 (`Lint & Test`) fails during `pytest tests/` step with `ModuleNotFoundError: No module named 'numpy'`.
- **Root Cause**: The new NumPy tutorial module added `import numpy as np` in `cloud_app/tutorials/numpy_basics.py` and `tests/test_numpy_tutorial.py`. While installed in the local `.venv`, `numpy` was missing from `requirements.txt`.
- **Fix Applied**: Added `numpy>=2.0.0` to `requirements.txt`.

---

### Issue 2: Missing or Misconfigured GitHub Secrets
- **Symptom**: Stage 3 (`Deploy to Droplet`) fails immediately with `::error::Missing secret: <SECRET_NAME>`.
- **Required Secrets** (Set in GitHub Repository → **Settings** → **Secrets and variables** → **Actions**):
  - `DROPLET_HOST`: Public IP address of the DigitalOcean droplet (e.g. `143.198.x.x`).
  - `DROPLET_USER`: SSH username (e.g. `root` or `deploy`).
  - `DROPLET_SSH_KEY`: Full private SSH key (contents of `~/.ssh/id_ed25519`).
  - `DROPLET_APP_DIR`: Target path on Droplet (e.g. `/opt/teach-cloud`).
  - `ENV_PRODUCTION`: Full contents of the `.env.production` configuration file.

---

### Issue 3: Port 80/443 Conflicts on Droplet Host
- **Symptom**: Container launch fails with `bind: address already in use` or Nginx container fails to bind.
- **Root Cause**: A native standalone Nginx or Apache web server running directly on the Droplet host OS is binding to port 80/443 before Docker Compose launches.
- **Fix Protocol**: The deployment pipeline executes:
  ```bash
  sudo systemctl stop nginx apache2 2>/dev/null || true
  sudo systemctl disable nginx apache2 2>/dev/null || true
  docker compose up -d --force-recreate
  ```

---

### Issue 4: SSH Authentication & Host Key Failures
- **Symptom**: `ssh: connect to host ... Permission denied (publickey)`.
- **Fix Protocol**: Verify the public key counterpart of `DROPLET_SSH_KEY` is present in `/root/.ssh/authorized_keys` on the Droplet:
  ```bash
  cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
  chmod 600 ~/.ssh/authorized_keys
  ```

---

### Issue 5: Health Check HTTP Failure (200/301/302 Exits)
- **Symptom**: Stage 3 completes container startup but fails on step `Health check — wait for app to respond` with `curl: (7) Failed to connect`.
- **Root Cause**: Flask container crashed upon initialization (e.g. database schema mismatch or invalid `SECRET_KEY`).
- **Fix Protocol**: Check live container logs on Droplet:
  ```bash
  ssh root@<DROPLET_HOST> "cd /opt/teach-cloud && docker compose logs web --tail 100"
  ```

---

## 3. Step-by-Step Manual Deployment & Recovery Protocol

If automatic deployment encounters network interruptions, execute the manual deployment recovery sequence:

```bash
# 1. SSH into DigitalOcean Droplet
ssh root@<DROPLET_HOST>

# 2. Navigate to application directory
cd /opt/teach-cloud

# 3. Pull latest docker image from GHCR
docker login ghcr.io -u <GITHUB_ACTOR>
docker pull ghcr.io/dilshadgit/cloud_flask:latest

# 4. Restart container stack with forced recreation
docker compose up -d --force-recreate --remove-orphans

# 5. Check container statuses and logs
docker compose ps
docker compose logs -f web
```

---

## 4. Verification Checklist

Before pushing to `production`:
1.  Run local pytest: `.venv/bin/pytest tests/`
2.  Verify `requirements.txt` contains all imported standard & 3rd party packages.
3.  Execute Git deployment sequence:
    ```bash
    git checkout main
    git merge numpy_module
    git push origin main

    git checkout production
    git merge main
    git push origin production
    ```
