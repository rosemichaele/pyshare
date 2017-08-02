from pyshare.party import Party
from pyshare.expense import Expense
from pyshare import exchange_rates


class Payment:

    def __init__(self, expense: Expense, paid_by: Party, currency: str, amount: float):
        self.expense = expense
        self.paid_by = paid_by
        self.currency = currency
        self.amount = amount

    def currency_is_supported(self):
        return exchange_rates.is_supported(self.currency)
