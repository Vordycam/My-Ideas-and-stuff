Render deployment (fast path)
================================

This document explains how to enable one-click deploys to Render using the existing container workflow.

Steps
1. Create a Web Service on Render and note the `Service ID`.
2. Create an API key in Render (Account → API Keys). Keep it secure.
3. Add the following repository secrets in GitHub (Settings → Secrets → Actions):
   - `RENDER_API_KEY` — the API key from Render
   - `RENDER_SERVICE_ID` — the Render service ID

How it works
- The workflow `.github/workflows/container.yml` will build and push a container to GHCR.
- If both `RENDER_API_KEY` and `RENDER_SERVICE_ID` are set, the workflow will call Render's deploy action to trigger a deploy of the new image.

Notes
- Render will pull the image and perform the deploy; ensure your Render service is configured to accept the image or to follow the repo settings as needed.
- Keep Stripe secrets in GitHub Secrets (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`) for production use.
