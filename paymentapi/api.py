"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request, current_app
import stripe
import paymentapi.config
from os import environ
from flask_cors import CORS


payment_api = Blueprint('api', __name__)
CORS(payment_api)
stripe.api_key = paymentapi.config.BaseConfig.STRIPE_SECRET_KEY


@payment_api.route("/Payment.fetch_public_key", methods=["GET"])
def fetch_public_key():
    stripe_public_key = paymentapi.config.BaseConfig.STRIPE_PUBLIC_KEY
    return jsonify({"public_key": stripe_public_key})


def generate_response(intent, licence_plate_number):
    print(intent)

    if intent.status == "requires_action" and intent.next_action.type == "use_stripe_sdk":
        return jsonify({
            "requires_action": True,
            "payment_intent_client_secret": intent.client_secret,
        }), 200
    if intent.status != "succeeded":
        return jsonify({"error": "invalid_payment" % (intent.status)}), 200
        
    if intent.status == "succeeded":
        return jsonify({
            "msg": "payment_done", 
            "success": True, 
            "licence_plate_number": licence_plate_number
        }), 200


    return jsonify({"msg": "payment_done", "success": True, "licence_plate_number": licence_plate_number }), 200


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
                            )
                customer_id = cus_create['id']
                
            else :
                customer_id = cus_exist.data[0]['id']

            pay_method = stripe.PaymentMethod.create( #https://stripe.com/docs/api/payment_methods/create
                type="card",
                card={
                    "number": data["card_number"],
                    "exp_month": data["card_expiry"].split("/", 1)[0].strip(),
                    "exp_year": data["card_expiry"].split("/", 1)[1].strip(),
                    "cvc": data["card_cvc"],
                },
            )

            payment_method_id = pay_method.id

            intent = stripe.PaymentIntent.create(
                        payment_method = payment_method_id,
                        amount = int(data["card_amount"])*100,
                        currency = "inr",
                        confirmation_method = "manual",
                        capture_method = "automatic",
                        confirm = True,
                        receipt_email = data["card_email"],
                        customer = customer_id,
                    )

    ## https://stripe.com/docs/error-handling
    except stripe.error.CardError as error:
        return jsonify({"error": format(error.user_message)}), 200
    except stripe.error.InvalidRequestError:
        return jsonify({"error": "An invalid request occurred"}), 200
    except Exception:
        return jsonify({"error": "Another problem occurred, maybe unrelated to Stripe."}), 200


    # return jsonify({"msg": "customer created", "data": {"success": True }}), 200

    print(data['card_name'])
    return generate_response(intent, data["card_name"])

##TO BE DELETED. FOR DEVELOPMENT PURPOSES.
@payment_api.route("/Payment.fetch", methods=["GET"])
def fetch():
    data = {
            "licensePlate": "abc 6666",
            "areaInfos": [
                {
                    "areaID": "incididunt",
                    "areaName": "nulla aliqua eu voluptate eu",
                    "address": "qui proident 23, 73313 aliquip"
                },
                {
                    "areaID": "sunt",
                    "areaName": "aliqua ipsum sit quis voluptate",
                    "address": "ex cillum 53, 63705 aliquip"
                },
                {
                    "areaID": "ad",
                    "areaName": "velit labore ad quis eiusmod",
                    "address": "et exercitation 53, 13958 amet"
                }
            ],
            "parkingProcesses": [
                {
                    "areaID": "incididunt",
                    "start": "2004-08-15T10:45:45.555Z",
                    "stop": "1973-06-27T06:52:33.676Z",
                    "parkingFee": 45
                },
                {
                    "areaID": "sunt",
                    "start": "2016-01-24T18:44:43.205Z",
                    "stop": "2014-08-14T13:11:02.743Z",
                    "parkingFee": 26
                },
                {
                    "areaID": "ad",
                    "start": "1977-07-30T03:33:39.609Z",
                    "stop": "1982-01-02T20:46:28.974Z",
                    "parkingFee": 40
                }
            ]
        }

    return jsonify(data)

##TO BE DELETED. FOR DEVELOPMENT PURPOSES.
@payment_api.route("/Payment.discount", methods=["GET"])
def discount():
    # input = "licensePlate": "abc 6666",
    # "discountCode": "aaabbb",
    # "parkingProcess":  {
    #                 "areaID": "incididunt",
    #                 "start": "2004-08-15T10:45:45.555Z",
    #                 "stop": "1973-06-27T06:52:33.676Z",
    #                 "parkingFee": 45
    #             }

    data = {
            "licensePlate": "abc 6666",
            "parkingProcess": {
                "areaID": "incididunt",
                "start": "2004-08-15T10:45:45.555Z",
                "stop": "1973-06-27T06:52:33.676Z",
                "parkingFee": 45
            },
            "parkingFee": 37,
            "discountCode": "aaabbb"
        }

    return jsonify(data)
