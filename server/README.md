Server skeleton (Stripe)

Setup

1. Create a virtualenv and install requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r server/requirements.txt
```

2. Set environment variables (example `.env`):

```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
PRICE_STANDARD_ID=price_...
PRICE_PRO_ID=price_...
SUCCESS_URL=https://yourdomain.example/success
CANCEL_URL=https://yourdomain.example/cancel
```

3. Run server:

```powershell
python server/app.py
```

Notes
- This is a minimal example. Use HTTPS and proper secret management in production.
- Use Stripe's recommended libraries and webhook signature verification for security.

Deployment
----------

We publish the server as a Docker container and push images to GitHub Container Registry (GHCR).

Workflow in this repository will build and push images on `main` to `ghcr.io/<OWNER>/my-ideas-and-stuff-server:latest`.

To enable automatic deploy to Render, set the following repository secrets:

- `RENDER_API_KEY` — Render API key with deploy permissions.
- `RENDER_SERVICE_ID` — Render service ID to deploy the new image.

Alternative deployments
-----------------------

- Cloud Run / ECS / App Service: build the container and push to a registry, then deploy using the provider's recommended workflow and service account keys stored in GitHub Secrets.

Setting production Stripe secrets
--------------------------------

Set these repository secrets for production use (do not commit them to source):

- `STRIPE_SECRET_KEY` — your Stripe secret key
- `STRIPE_WEBHOOK_SECRET` — your webhook signing secret

Once those secrets are configured and a deployment target is set, the server will read them from the environment.
