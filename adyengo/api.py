import json
import requests
from django.utils import timezone
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
        },
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


def payment_link(
    shopper_email,
    merchant_reference,
    payment_amount,
    currency_code,
    merchant_account=settings.MERCHANT_ACCOUNT,
    locale=None,
    shopper_reference=None
):
    data = {
        'amount': {
            'value': int(payment_amount),
            'currency': currency_code
        },
        'merchantAccount': merchant_account,
        'reference': merchant_reference,
        'expiresAt': (timezone.now() + timezone.timedelta(days=60)).isoformat()
    }
    if locale:
        data['shopperLocale'] = locale
    if shopper_reference:
        data['shopperReference'] = shopper_reference
    return checkout_api_request(
        'paymentLinks',
        data
    )


def session(
    merchant_reference,
    payment_amount,
    currency_code,
    merchant_account=settings.MERCHANT_ACCOUNT,
    shopper_email=None,
    return_url=None,
    locale=None,
    shopper_reference=None,
    ip=None
):
    data = {
        'amount': {
            'value': int(payment_amount),
            'currency': currency_code
        },
        'merchantAccount': merchant_account,
        'reference': merchant_reference,
        'shopperEmail': shopper_email,
        'returnUrl': return_url,
        'enableOneClick': True,
        'enableRecurring': True,
    }
    if locale:
        data['shopperLocale'] = locale
    if ip:
        data['shopperIP'] = ip
    if shopper_reference:
        data['shopperReference'] = shopper_reference
    return checkout_api_request(
        'sessions',
        data
    )


def checkout_api_request(endpoint, data):
    return checkout_api_base_request(
        '{}{}'.format(settings.CHECKOUT_API_BASE_URL.replace('PREFIX', settings.PREFIX_URL), endpoint),
        data
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

def checkout_api_base_request(url, data):
    return requests.post(
        url,
        headers={
            'Content-Type': 'application/json',
            'X-API-Key': settings.API_KEY},
        data=json.dumps(data)
    ).json()


def api_request(url, data):
    return requests.post(
        url,
        headers={'Content-Type': 'application/json'},
        auth=(settings.API_USERNAME, settings.API_PASSWORD),
        data=json.dumps(data)
    ).json()
