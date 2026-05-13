const API_BASE = window.location.origin.replace(/:\d+$/, ':5000'); // assumes server runs on 5000 locally

document.getElementById('buy-standard').addEventListener('click', async () => {
  await createCheckout('standard_monthly');
});
document.getElementById('buy-pro').addEventListener('click', async () => {
  await createCheckout('professional_monthly');
});

async function createCheckout(priceKey) {
  const res = await fetch(`${API_BASE}/create-checkout-session`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ price: priceKey })
  });
  const data = await res.json();
  if (data.error) { alert(data.error); return }
  // Normally call Stripe.js redirectToCheckout with session id and publishable key
  // For demo, show the session id and a QR code to open it from mobile
  const qrDiv = document.getElementById('qr');
  qrDiv.innerHTML = `<p>Session: ${data.id}</p><p>Open session on Stripe dashboard or implement client redirect.</p>`;
}
