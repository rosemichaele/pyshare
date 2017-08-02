from pyshare.party import Party
from pyshare import exchange_rates


class Expense:

    def __init__(self, paid_for: str, currency: str, amount: float, parties_involved: "list of party.Party" = []):
        self.paid_for = paid_for
        self.currency = currency
        self.amount = amount
        self.parties_involved = parties_involved

    def add_party(self, party):
        assert isinstance(party, Party), "Cannot add type {} to list of parties".format(str(type(party)))
        self.parties_involved.append(party)

    def currency_is_supported(self) -> bool:
        return exchange_rates.is_supported(self.currency)
