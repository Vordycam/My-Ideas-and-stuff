# Subscription Plans

This document describes the subscription plans and payment modes for AEGIS.

Plans

- **Standard**
  - Price: $9 / month
  - Package:
    - Basic feed updates
    - Search and filtering
    - Community support via issues

- **Professional**
  - Price: $29 / month
  - Package:
    - Everything in Standard
    - Priority support
    - Advanced exports and backups
    - Team-shared access (up to 5 users)

Payment methods

- **Cards (Visa, Mastercard, Amex)** — PCI-compliant gateway recommended (Stripe / Braintree).
- **QR payments** — support for platform QR (e.g. local wallets) via payment provider that exposes QR checkout.

Implementation notes

- Integrate a payment gateway (recommended: Stripe): create product SKUs for `standard_monthly` and `professional_monthly`.
- Use hosted checkout sessions to avoid handling card data directly and to keep PCI-scope low.
- For QR payments, use the provider's API to generate a checkout URL and render the QR code on the client.
- Store subscriptions server-side and validate webhooks for status updates (invoices, cancellations).

Security & Compliance

- Do not store raw card numbers in the app. Use tokenization via the provider.
- Ensure webhooks are signed and verify signatures on receipt.
