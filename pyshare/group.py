from pyshare.party import Party
from pyshare.expense import Expense
from pyshare.payment import Payment


class Group:

    def __init__(self, name: str, parties: "list of party.Party" = [], expenses: "list of expense.Expense" = [],
                 payments: "list of payment.Payment" = []):
        self.name = name
        self.parties = parties
        self.expenses = expenses
        self.payments = payments

    def add_party(self, party):
        assert isinstance(party, Party), "Cannot add type {} to list of parties".format(str(type(party)))
        self.parties.append(party)

    def add_expense(self, expense):
        assert isinstance(expense, Expense), "Cannot add type {} to list of expenses".format(str(type(expense)))
        assert expense.currency_is_supported(), "Invalid currency type {} when adding expense".format(expense.currency)
        self.expenses.append(expense)

    def add_payment(self, payment):
        assert isinstance(payment, Payment), "Cannot add type {} to list of payments".format(str(type(payment)))
        assert payment.currency_is_supported(), "Invalid currency type {} when adding expense".format(payment.currency)
        self.payments.append(payment)

    def currencies_match(self) -> bool:
        """Make sure all payments and expenses are reported in the same currency."""
        currencies_list = [e.currency for e in self.expenses] + [p.currency for p in self.payments]
        return currencies_list.count(currencies_list[0]) == len(currencies_list)


