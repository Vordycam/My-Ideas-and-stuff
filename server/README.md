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
