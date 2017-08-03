from pyshare.party import Party
from pyshare import exchange_rates


class Expense:

    def __init__(self, paid_for: str, currency: str, amount: float, parties_involved: "set of party.Party" = None):
        self.paid_for = paid_for
        self.currency = currency
        self.amount = amount
        if parties_involved:
            self.parties_involved = parties_involved
        else:
            self.parties_involved = set()

    def add_party(self, party):
        assert isinstance(party, Party), "Cannot add type {} to list of parties".format(str(type(party)))
        self.parties_involved.add(party)

    def remove_party(self, party):
        self.parties.remove(party)

    def currency_is_supported(self) -> bool:
        return exchange_rates.is_supported(self.currency)
