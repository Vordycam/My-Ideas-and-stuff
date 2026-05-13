from flask import Flask, request, jsonify
import os
import stripe
from dotenv import load_dotenv

load_dotenv()

STRIPE_SECRET = os.getenv('STRIPE_SECRET_KEY', 'sk_test_placeholder')
stripe.api_key = STRIPE_SECRET

app = Flask(__name__)


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = request.get_json() or {}
    price = data.get('price', 'standard_monthly')
    prices = {
        'standard_monthly': os.getenv('PRICE_STANDARD_ID', 'price_standard_placeholder'),
        'professional_monthly': os.getenv('PRICE_PRO_ID', 'price_professional_placeholder')
    }
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='subscription',
            line_items=[{'price': prices.get(price), 'quantity': 1}],
            success_url=os.getenv('SUCCESS_URL', 'https://example.com/success'),
            cancel_url=os.getenv('CANCEL_URL', 'https://example.com/cancel')
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
    try:
        if endpoint_secret:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        else:
            event = stripe.Event.construct_from(request.get_json(), stripe.api_key)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Handle checkout.session.completed
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # TODO: fulfill subscription, save to DB
        print('Checkout session completed:', session.get('id'))

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('PORT', 5000)))
