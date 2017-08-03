from requests import get


def current_exchange_rates(base: str) -> dict:
    """Return a dictionary of conversion rates to base, which is a 3-char string indicating the target currency."""
    request_url = "http://api.fixer.io/latest"
    query_string = "?base=" + base
    response_object = get(request_url + query_string)
    exchange_rates = response_object.json()
    return exchange_rates


def conversion_rate(base: str, origin: str) -> float:
    """Return a float which is the conversion rate from origin to base. Both base and origin are 3-char strings.

        e.g >>> conversion_rate("USD", "EUR") = 1.186
            Thus: 100 EUR = (100 EUR * 1.186) USD = 118.6 USD
    """
    assert is_supported(base), "Cannot convert to invalid currency type: {}".format(base)
    assert is_supported(origin), "Cannot convert from invalid currency type: {}".format(origin)
    conversion_key = current_exchange_rates(origin)
    return conversion_key["rates"][base]


def is_supported(base: str) -> bool:
    """Indicates whether base is currently available for conversion via the fixer.io api."""
    request_url = "http://api.fixer.io/latest"
    query_string = "?base=" + base
    response_object = get(request_url + query_string)
    if response_object.status_code == 200:
        return True
    else:
        return False
