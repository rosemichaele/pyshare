from pyshare.party import Party
from pyshare.expense import Expense


class Payment:

    def __init__(self, expense: Expense, paid_by: Party, currency: str, amount: float):
        self.expense = expense
        self.paid_by = paid_by
        self.currency = currency
        self.amount = amount
