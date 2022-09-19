"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request, current_app
import stripe
import paymentapi.config
from os import environ


payment_api = Blueprint('api', __name__)
stripe.api_key = paymentapi.config.BaseConfig.STRIPE_SECRET_KEY


@payment_api.route("/Payment.fetch_public_key", methods=["GET"])
def fetch_public_key():
    stripe_public_key = paymentapi.config.BaseConfig.STRIPE_PUBLIC_KEY
    return jsonify({"public_key": stripe_public_key})


def generate_response(intent, licence_plate_number):
    if intent.status == "requires_action" and intent.next_action.type == "use_stripe_sdk":
        return jsonify({
            "requires_action": True,
            "payment_intent_client_secret": intent.client_secret,
        }), 200
    if intent.status != "succeeded":
        return jsonify({"error": "invalid_payment" % (intent.status)}), 200


    return jsonify({"msg": "payment_done", "data": {"success": True, "licence_plate_number": licence_plate_number }}), 200


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


@payment_api.route("/Payment.create_customer_pay", methods=["POST"])
def create_customer_pay():
    data = request.get_json(force=True)

    customer_id = ''
    pay_method = ''

    print(data)

    try:
        if "payment_intent_id" in data:
            intent = stripe.PaymentIntent.confirm(data["payment_intent_id"])

        else:
            cus_exist = stripe.Customer.list(email = data["card_email"])

            if(len(cus_exist.data) == 0) :
                cus_create = stripe.Customer.create(
                                name = data["card_name"], #licence_plate_number
                                email = data["card_email"],
                                # phone = '9401059543'
                            )
                customer_id = cus_create['id']
                
            else :
                customer_id = cus_exist.data[0]['id']

            pay_method = stripe.PaymentMethod.create( #https://stripe.com/docs/api/payment_methods/create
                type="card",
                card={
                    "number": data["card_number"],
                    "exp_month": 9,
                    "exp_year": 2023,
                    "cvc": data["card_cvc"],
                },
            )

            payment_method_id = pay_method.id

            intent = stripe.PaymentIntent.create(
                        payment_method = payment_method_id,
                        amount =data["card_amount"],
                        currency = "chf",
                        confirmation_method = "manual",
                        capture_method = "automatic",
                        confirm = True,
                        receipt_email = data["card_email"],
                        customer = customer_id,
                    )

    except stripe.error.CardError as error:
        return jsonify({"error": error.user_message}), 200

    # return jsonify({"msg": "customer created", "data": {"success": True }}), 200
    return generate_response(intent, data["card_name"])
