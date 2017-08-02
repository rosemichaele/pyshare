from pyshare import exchange_rates


class TestExchangeRates:

    def test_error_response_on_invalid_base(self):
        assert exchange_rates.current_exchange_rates("invalid") == {'error': 'Invalid base'}
