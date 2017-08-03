from pyshare.party import Party
from pyshare.expense import Expense
from pyshare.payment import Payment
from pyshare import exchange_rates


class Group:

    def __init__(self, name: str, currency: str, parties: "set of party.Party" = None,
                 expenses: "set of expense.Expense" = None, payments: "set of payment.Payment" = None):
        self.name = name
        self.currency = currency
        if parties:
            self.parties = parties
        else:
            self.parties = set()
        if expenses:
            self.expenses = expenses
        else:
            self.expenses = set()
        if payments:
            self.payments = payments
        else:
            self.payments = set()

    def add_party(self, party):
        assert isinstance(party, Party), "Cannot add type {} to list of parties".format(str(type(party)))
        self.parties.add(party)

    def add_expense(self, expense):
        assert isinstance(expense, Expense), "Cannot add type {} to list of expenses".format(str(type(expense)))
        assert expense.currency_is_supported(), "Invalid currency type {} when adding expense".format(expense.currency)
        self.expenses.add(expense)

    def add_payment(self, payment):
        assert isinstance(payment, Payment), "Cannot add type {} to list of payments".format(str(type(payment)))
        assert payment.currency_is_supported(), "Invalid currency type {} when adding payment".format(payment.currency)
        self.payments.add(payment)

    def currency_is_supported(self):
        return exchange_rates.is_supported(self.currency)

    def currencies_match(self) -> bool:
        """Make sure all payments and expenses are reported in the same currency."""
        currencies_list = [e.currency for e in self.expenses] + [p.currency for p in self.payments] + [self.currency]
        return currencies_list.count(currencies_list[0]) == currencies_list.__len__()

    def standardize_group_expenses(self):
        """Converts all expenses into the currency of the group."""
        for expense in self.expenses:
            if not self.currency == expense.currency:
                conversion_rate = exchange_rates.conversion_rate(self.currency, expense.currency)
                expense.amount *= conversion_rate
                expense.currency = self.currency

    def standardize_group_payments(self):
        """Converts all payments into the currency of the group."""
        for payment in self.payments:
            if not self.currency == payment.currency:
                conversion_rate = exchange_rates.conversion_rate(self.currency, payment.currency)
                payment.amount *= conversion_rate
                payment.currency = self.currency

    def consolidated_debts(self) -> dict:
        """
        Determine how much everyone owes without considering payments.
        """
        self.standardize_group_expenses()
        party_debts = dict()
        for party in self.parties:
            party_debts[party.name] = dict()
            party_debts[party.name]["currency"] = self.currency
            party_debts[party.name]["debts"] = 0

        for expense in self.expenses:
            num_parties_involved = len(expense.parties_involved)
            split_expense = expense.amount / num_parties_involved
            for party in expense.parties_involved:
                party_debts[party.name]["debts"] += split_expense
        return party_debts

    def consolidated_payments(self) -> dict:
        """
        Determine how much everyone has already paid.
        """
        self.standardize_group_payments()
        party_payments = dict()
        for party in self.parties:
            party_payments[party.name] = dict()
            party_payments[party.name]["currency"] = self.currency
            party_payments[party.name]["payments"] = 0

        for payment in self.payments:
            party_payments[payment.paid_by.name]["currency"] = self.currency
            party_payments[payment.paid_by.name]["payments"] += payment.amount
        return party_payments
