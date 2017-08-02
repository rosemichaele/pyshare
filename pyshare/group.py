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
        self.expenses.append(expense)

    def add_payment(self, payment):
        assert isinstance(payment, Payment), "Cannot add type {} to list of payments".format(str(type(payment)))
        self.payments.append(payment)

