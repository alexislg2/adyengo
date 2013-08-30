# Session Types

SESSION_TYPE_HPP_REGULAR = 'hpp_regular'
SESSION_TYPE_HPP_RECURRING = 'hpp_recurring'
SESSION_TYPE_API_RECURRING = 'api_recurring'

SESSION_TYPES_HPP = {
    SESSION_TYPE_HPP_REGULAR: "HPP Regular",
    SESSION_TYPE_HPP_RECURRING: "HPP Recurring",
}

SESSION_TYPES_API = {
    SESSION_TYPE_API_RECURRING: "API Recurring"
}

SESSION_TYPES = SESSION_TYPES_HPP.copy()
SESSION_TYPES.update(SESSION_TYPES_API)


# Page Types

PAGE_TYPE_MULTIPLE = 'multiple'
PAGE_TYPE_SINGLE = 'single'
PAGE_TYPE_SKIP = 'skip'

PAGE_TYPES = {
    PAGE_TYPE_MULTIPLE: "Multiple",
    PAGE_TYPE_SINGLE: "Single",
    PAGE_TYPE_SKIP: "Skip"
}


# Currency Code

CURRENCY_CODE_EUR = 'EUR'

CURRENCY_CODES = {
    CURRENCY_CODE_EUR: "Euro",
}


# Locales

LOCALE_NL_NL = 'nl_NL'
LOCALE_NL_BE = 'nl_BE'
LOCALE_FR_BE = 'fr_BE'
LOCALE_DE_DE = 'de_DE'
LOCALE_EN_GB = 'en_GB'

LOCALES = {
    LOCALE_NL_NL: "Dutch (Holland)",
    LOCALE_NL_BE: "Dutch (Belgium)",
    LOCALE_FR_BE: "French (Belgium)",
    LOCALE_DE_DE: "German (Germany)",
    LOCALE_EN_GB: "English (United Kingdom)"
}

# Country Code

COUNTRY_CODE_NL = 'NL'
COUNTRY_CODE_BE = 'BE'
COUNTRY_CODE_DE = 'DE'
COUNTRY_CODE_GB = 'GB'

COUNTRY_CODES = {
    COUNTRY_CODE_NL: "Netherlands",
    COUNTRY_CODE_BE: "Belgium",
    COUNTRY_CODE_DE: "Germany",
    COUNTRY_CODE_GB: "United Kingdom"
}

# Payment Method

PAYMENT_METHOD_VISA = 'visa'
PAYMENT_METHOD_MC = 'mc'
PAYMENT_METHOD_AMEX = 'amex'
PAYMENT_METHOD_IDEAL = 'ideal'
PAYMENT_METHOD_BANKTRANSFER_NL = 'bankTransfer_NL'
PAYMENT_METHOD_BANKTRANSFER_DE = 'bankTransfer_DE'
PAYMENT_METHOD_ELV = 'elv'
PAYMENT_METHOD_DIRECTDEBIT_NL = 'directdebit_NL'
PAYMENT_METHOD_DIRECT_E_BANKING = 'directEbanking'
PAYMENT_METHOD_PAYPAL = 'paypal'
PAYMENT_METHOD_CARD = 'card'
PAYMENT_METHOD_BANKTRANSFER = 'bankTransfer'

PAYMENT_METHODS = {
    PAYMENT_METHOD_VISA: "Visa",
    PAYMENT_METHOD_MC: "Master Card",
    PAYMENT_METHOD_AMEX: "Amex",
    PAYMENT_METHOD_IDEAL: "iDEAL",
    PAYMENT_METHOD_BANKTRANSFER_NL: "Dutch Banktransfer",
    PAYMENT_METHOD_BANKTRANSFER_DE: "German Banktransfer",
    PAYMENT_METHOD_ELV: "ELV",
    PAYMENT_METHOD_DIRECTDEBIT_NL: "Direct Debit (Netherlands)",
    PAYMENT_METHOD_DIRECT_E_BANKING: "SofortUberweisung",
    PAYMENT_METHOD_PAYPAL: "PayPal",
    PAYMENT_METHOD_CARD: "All debit and credit cards",
    PAYMENT_METHOD_BANKTRANSFER: "All banktransfers",
}


# Recurring contract types

RECURRING_CONTRACT_TYPE_RECURRING = 'RECURRING'
RECURRING_CONTRACT_TYPE_ONECLICK = 'ONECLICK'

RECURRING_CONTRACT_TYPES = {
    RECURRING_CONTRACT_TYPE_RECURRING: "Recurring",
    RECURRING_CONTRACT_TYPE_ONECLICK: "One click"
}

# Recurring contract types plus combinations

RECURRING_CONTRACT_TYPES_PLUS_COMBOS = RECURRING_CONTRACT_TYPES.copy()
RECURRING_CONTRACT_TYPES_PLUS_COMBOS.update({
    '{},{}'.format(
        RECURRING_CONTRACT_TYPE_RECURRING,
        RECURRING_CONTRACT_TYPE_ONECLICK
    ): "Recurring and One click (user chooses)"
})


# Recurring contract variant fields

RECURRING_CONTRACT_VARIANT_FIELDS = {
    'card': (
        'expiryMonth',
        'expiryYear',
        'holderName',
        'number',
        'cvc',
        'issueNumber',
        'startMonth',
        'startYear'
    ),
    'elv': (
        'bankLocation',
        'bankName',
        'bankLocationId',
        'accountHolderName',
        'bankAccountNumber'
    ),
    'bank': (
        'bankAccountNumber',
        'bankLocationId',
        'bankName',
        'bic',
        'countryCode',
        'iban',
        'ownerName'
    )
}


# Recurring payment result codes

RECURRING_PAYMENT_RESULT_AUTHORISED = 'Authorised'
RECURRING_PAYMENT_RESULT_REFUSED = 'Refused'
RECURRING_PAYMENT_RESULT_ERROR = 'Error'

RECURRING_PAYMENT_RESULT_CODES = {
    RECURRING_PAYMENT_RESULT_AUTHORISED: 'Authorised',
    RECURRING_PAYMENT_RESULT_REFUSED: 'Refused',
    RECURRING_PAYMENT_RESULT_ERROR: 'Error'
}


# Notification event codes

NOTIFICATION_EVENT_CODE_AUTHORISATION = 'AUTHORISATION'
NOTIFICATION_EVENT_CODE_CANCELLATION = 'CANCELLATION'
NOTIFICATION_EVENT_CODE_REFUND = 'REFUND'
NOTIFICATION_EVENT_CODE_CANCEL_OR_REFUND = 'CANCEL_OR_REFUND'
NOTIFICATION_EVENT_CODE_CAPTURE = 'CAPTURE'
NOTIFICATION_EVENT_CODE_REFUNDED_REVERSED = 'REFUNDED_REVERSED'
NOTIFICATION_EVENT_CODE_CAPTURE_FAILED = 'CAPTURE_FAILED'
NOTIFICATION_EVENT_CODE_REFUND_FAILED = 'REFUND_FAILED'
NOTIFICATION_EVENT_CODE_REQUEST_FOR_INFORMATION = 'REQUEST_FOR_INFORMATION'
NOTIFICATION_EVENT_CODE_NOTIFICATION_OF_CHARGEBACK = 'NOTIFICATION_OF_CHARGEBACK'
NOTIFICATION_EVENT_CODE_ADVICE_OF_DEBIT = 'ADVICE_OF_DEBIT'
NOTIFICATION_EVENT_CODE_CHARGEBACK = 'CHARGEBACK'
NOTIFICATION_EVENT_CODE_CHARGEBACK_REVERSED = 'CHARGEBACK_REVERSED'
NOTIFICATION_EVENT_CODE_REPORT_AVAILABLE = 'REPORT_AVAILABLE'

NOTIFICATION_EVENT_CODES = {
    NOTIFICATION_EVENT_CODE_AUTHORISATION: "Authorisation",
    NOTIFICATION_EVENT_CODE_CANCELLATION: "Cancellation",
    NOTIFICATION_EVENT_CODE_REFUND: "Refund",
    NOTIFICATION_EVENT_CODE_CANCEL_OR_REFUND: "Cancel or refund",
    NOTIFICATION_EVENT_CODE_CAPTURE: "Capture",
    NOTIFICATION_EVENT_CODE_REFUNDED_REVERSED: "Refunded reversed",
    NOTIFICATION_EVENT_CODE_CAPTURE_FAILED: "Capture failed",
    NOTIFICATION_EVENT_CODE_REFUND_FAILED: "Refund failed",
    NOTIFICATION_EVENT_CODE_REQUEST_FOR_INFORMATION: "Request for information",
    NOTIFICATION_EVENT_CODE_NOTIFICATION_OF_CHARGEBACK: "Notification of chargeback",
    NOTIFICATION_EVENT_CODE_ADVICE_OF_DEBIT: "Advice of debit",
    NOTIFICATION_EVENT_CODE_CHARGEBACK: "Chargeback",
    NOTIFICATION_EVENT_CODE_CHARGEBACK_REVERSED: "Chargeback reversed",
    NOTIFICATION_EVENT_CODE_REPORT_AVAILABLE: "Report available"
}


# Adyen servers ip addresses

ADYEN_SERVERS_IP_ADDRESS_RANGES = (
    u'82.199.87.128/26', # 82.199.87.129 to 82.199.87.191
    u'82.199.90.136/29', # 82.199.90.137 to 82.199.90.142
    u'82.199.90.160/27', # 82.199.90.161 to 82.199.90.190
    u'91.212.42.0/24'    # 91.212.42.1 to 91.212.42.254
)

# Only these IP addresses should be allowed to send notifications.
# You can check if an IP exists inside a range using ipaddress:
# https://pypi.python.org/pypi/ipaddress/1.0.4
#
# import ipaddress
# ipaddress.ip_address(u'82.199.87.135') in ipaddress.ip_network(u'82.199.87.128/26')
#
# Note that both IP addresses SHOULD be unicode.
