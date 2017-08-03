import pytest
from pyshare.expense import Expense
from pyshare.party import Party


class TestExpense:
    @classmethod
    def setup_class(cls):
        cls.not_a_party = "This is not a party.Party, it's a string."
        cls.test_party = Party(name="Michael")
        cls.test_expense = Expense(paid_for="Impulse purchase", currency="USD", amount=153.19)

    def test_add_party_to_expense_succeeds(self):
        assert not self.test_expense.parties_involved
        self.test_expense.add_party(self.test_party)
        assert len(self.test_expense.parties_involved) == 1

    def test_add_not_party_to_expense_fails(self):
        with pytest.raises(AssertionError):
            self.test_expense.add_party(self.not_a_party)
