import json
import requests
from . import settings


def exec_recurring_payment(
    contract_type,
    shopper_interaction,
    shopper_reference,
    shopper_email,
    merchant_reference,
    payment_amount,
    currency_code,
    recurring_detail_reference=None,
    shopper_statement=None,
    cvc=None,
    merchant_account=settings.MERCHANT_ACCOUNT
):
    data = {
            'amount': {
                'value': int(payment_amount),
                'currency': currency_code
            },
            # "card": {
            #     "cvc": "737"
            # },
            'reference': merchant_reference,
            'merchantAccount': merchant_account,
            'shopperEmail': shopper_email,
            'shopperReference': shopper_reference,
            'selectedRecurringDetailReference': recurring_detail_reference or "LATEST",
            'shopperInteraction': shopper_interaction,
            'recurring': {
                'contract': contract_type
            },
            'shopperStatement': shopper_statement,
        }

    if cvc:
        data["card"] = {"cvc": cvc}

    return payment_api_request(
        'authorise',
        data
    )


def list_recurring_details(shopper_reference, contract_type, merchant_account=settings.MERCHANT_ACCOUNT):
    return recurring_api_request(
        'listRecurringDetails',
        {
            'merchantAccount': merchant_account,
            'recurring': {
                'contract': contract_type
            },
            'shopperReference': shopper_reference
        }
    )


def disable_recurring_details(shopper_reference, recurring_detail_reference, merchant_account=settings.MERCHANT_ACCOUNT):
    return recurring_api_request(
        'disable',
        {
            'merchantAccount': merchant_account,
            'shopperReference': shopper_reference,
            'recurringDetailReference': recurring_detail_reference
        }
    )


def payment_api_request(endpoint, data):
    return api_request(
        '{}{}'.format(settings.PAYMENT_API_BASE_URL, endpoint),
        data
    )


def recurring_api_request(endpoint, data):
    return api_request(
        '{}{}'.format(settings.RECURRING_API_BASE_URL, endpoint),
        data
    )


def api_request(url, data):
    return requests.post(
        url,
        headers={'Content-Type': 'application/json'},
        auth=(settings.API_USERNAME, settings.API_PASSWORD),
        data=json.dumps(data)
    ).json()
