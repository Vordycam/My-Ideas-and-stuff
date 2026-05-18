from flask import Flask, request, jsonify, g
import os
import stripe
import sqlite3
from dotenv import load_dotenv

load_dotenv()

STRIPE_SECRET = os.getenv('STRIPE_SECRET_KEY', 'sk_test_placeholder')
stripe.api_key = STRIPE_SECRET

DB_PATH = os.getenv('DB_PATH', os.path.join(os.path.dirname(__file__), 'subscriptions.db'))

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db


def init_db():
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with app.open_resource(schema_path, mode='r') as f:
        sql = f.read()
    db = get_db()
    db.executescript(sql)
    db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


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
        print('Checkout session completed:', session.get('id'))
        # Save minimal session info to SQLite for demo/testing
        try:
            db = get_db()
            db.execute(
                'INSERT INTO subscriptions (session_id, customer_id, price_id, status) VALUES (?, ?, ?, ?)',
                (session.get('id'), session.get('customer'), session.get('display_items', [{}])[0].get('price', {}).get('id') if session.get('display_items') else None, session.get('payment_status', 'unknown'))
            )
            db.commit()
        except Exception as e:
            app.logger.error('Failed to persist subscription: %s', e)

    return jsonify({'status': 'success'})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    # Ensure DB exists
    if not os.path.exists(DB_PATH):
        with app.app_context():
            init_db()
    app.run(debug=True, port=int(os.getenv('PORT', 5000)))
