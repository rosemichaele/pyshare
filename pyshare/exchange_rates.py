from requests import get


def current_exchange_rates(base: str) -> dict:
    """Return a dictionary of conversion rates to base, which is a 3-char string indicating the target currency."""
    request_url = "http://api.fixer.io/latest"
    query_string = "?base=" + base
    response_object = get(request_url + query_string)
    exchange_rates = response_object.json()
    return exchange_rates


def conversion_rate(base: str, origin: str) -> float:
    """Return a float which is the conversion rate from origin to base. Both base and origin are 3-char strings."""
    conversion_key = current_exchange_rates(base)
    return conversion_key["rates"][origin]


def is_supported(base: str) -> bool:
    """Indicates whether base is currently available for conversion via the fixer.io api."""
    request_url = "http://api.fixer.io/latest"
    query_string = "?base=" + base
    response_object = get(request_url + query_string)
    if response_object.status_code == 200:
        return True
    else:
        return False
