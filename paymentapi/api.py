"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request, current_app
import stripe
import paymentapi.config

payment_api = Blueprint('api', __name__)
stripe.api_key = paymentapi.config.BaseConfig.STRIPE_SECRET_KEY


@payment_api.route("/Payment.fetch_public_key", methods=["GET"])
def fetch_public_key():
    stripe_public_key = paymentapi.config.BaseConfig.STRIPE_PUBLIC_KEY
    return jsonify({"public_key": stripe_public_key})


@payment_api.route("/Payment.create_payment", methods=["POST"])
def create_payment():
    data = request.get_json(force=True)

    amount = float(data["amount"])

    if amount <= 0.50:
        return jsonify({"error": _("invalid_payment_amount")}), 200

    calculate_order_amount = int(amount * 100)
    try:
        if "payment_method_id" in data:
            intent = stripe.PaymentIntent.create(
                payment_method = data["payment_method_id"],
                amount = calculate_order_amount,
                currency = "chf",
                confirmation_method = "manual",
                confirm = True,
                receipt_email = data["receipt_email"],
                customer = data["licence_plate_number"],
            )

        elif "payment_intent_id" in data:
            intent = stripe.PaymentIntent.confirm(data["payment_intent_id"])
    except stripe.error.CardError as e:
        return jsonify({"error": e.user_message}), 200

    return generate_response(intent, data["licence_plate_number"])


def generate_response(intent, licence_plate_number):
    if intent.status == "requires_action" and intent.next_action.type == "use_stripe_sdk":
        return jsonify({
            "requires_action": True,
            "payment_intent_client_secret": intent.client_secret,
        }), 200
    if intent.status != "succeeded":
        return jsonify({"error": _("invalid_payment") % (intent.status)}), 200


    return jsonify({"msg": _("payment_done"), "data": {"success": True, "licence_plate_number": licence_plate_number }}), 200


@payment_api.route("/Payment.get_payment_list", methods=["GET"])
def get_payment_list():

    payment_data     = []
    data = request.get_json(force=True)

    if data["licence_plate_number"]:
        intent = stripe.PaymentIntent.list(
            customer = data["licence_plate_number"],
            limit=100,
        )

        for row in intent.data:
            data = {
                'name': '',
                'amount': row.currency.upper() + ' ' + str(float(row.amount) / 100),
                'payment_method_types': row.payment_method_types[0],
                'receipt_number': '',
                'receipt_url': '#',
                'refunded': '',
                'status': row.status,
                'payment_id': row.id,
                'created': 0,
            }

            if len(row.charges) > 0:
                charge = row.charges.data[0]
                data['name'] = charge.billing_details.name
                data['receipt_number'] = charge.receipt_number
                data['receipt_url'] = charge.receipt_url
                data['refunded'] = charge.refunded
                data['created'] = charge.created

            payment_data.append(data)

    return jsonify({"msg": "stripe_payment_fetched", "data": {"payment_list": payment_data}}), 200
