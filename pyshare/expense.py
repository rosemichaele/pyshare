from pyshare.party import Party


class Expense:

    def __init__(self, currency: str, amount: float, parties_involved: "list of party.Party" = []):
        self.currency = currency
        self.amount = amount
        self.parties_involved = parties_involved

    def add_party(self, party):
        assert isinstance(party, Party), "Cannot add type {} to list of parties".format(str(type(party)))
        self.parties_involved.append(party)


