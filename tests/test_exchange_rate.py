import pytest
from pyshare import exchange_rates


class TestExchangeRates:
    @classmethod
    def setup_class(cls):
        cls.invalid_base = "invalid"
        cls.unsupported_currency = "LLL"
        cls.supported_currency = "EUR"
        cls.supported_base = "USD"

    def test_error_response_on_invalid_base(self):
        assert exchange_rates.current_exchange_rates(self.invalid_base) == {'error': 'Invalid base'}

    def test_currency_is_supported(self):
        assert exchange_rates.is_supported(self.supported_currency)

    def test_not_currency_is_supported(self):
        assert not exchange_rates.is_supported(self.unsupported_currency)

    def test_cannot_convert_to_unsupported_currency(self):
        with pytest.raises(AssertionError):
            exchange_rates.conversion_rate(self.unsupported_currency, self.supported_currency)

    def test_cannot_convert_from_unsupported_currency(self):
        with pytest.raises(AssertionError):
            exchange_rates.conversion_rate(self.supported_currency, self.unsupported_currency)

    def test_successful_conversion_returns_float(self):
        assert isinstance(exchange_rates.conversion_rate(self.supported_base, self.supported_currency), float)
