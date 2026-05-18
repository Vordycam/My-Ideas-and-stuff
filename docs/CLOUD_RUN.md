Google Cloud Run deployment (recommended production path)
=========================================================

This document describes how to deploy the subscription server to Google Cloud Run using a service account. The repository includes a workflow to build and push the container to GHCR and then deploy to Cloud Run.

Prerequisites
- A GCP project with Cloud Run enabled.
- A service account with these roles:
  - `roles/run.admin`
  - `roles/iam.serviceAccountUser`
  - `roles/storage.admin` (to allow Artifact Registry or temporary usage; adjust as needed)

Create service account key
1. Create a service account in the GCP Console.
2. Assign the roles above.
3. Create a JSON key and download it. Keep it secret.

Repository secrets
- Add these repository secrets in GitHub (Settings → Secrets → Actions):
  - `GCP_SA_KEY` — the contents of the JSON key (base64-encoded or raw JSON; workflow expects raw JSON)
  - `GCP_PROJECT` — your GCP project id
  - `GCP_REGION` — desired Cloud Run region (e.g., `us-central1`)
  - `CLOUD_RUN_SERVICE` — the Cloud Run service name (will be created if it doesn't exist)

How the workflow works
- The workflow `.github/workflows/cloud-run.yml` will:
  1. Build and push a container image to GHCR.
  2. Authenticate to GCP using `GCP_SA_KEY` and run `gcloud run deploy` with the pushed image.

Security notes
- Keep the service account key secret and rotate periodically.
- For production, prefer Workload Identity or short-lived credentials where possible.
