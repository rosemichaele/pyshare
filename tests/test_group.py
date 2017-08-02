import pytest
from pyshare import group, party, expense, payment


class TestGroup:

    @classmethod
    def setup_class(cls):
        cls.test_group = group.Group(name="Test")
        cls.not_a_party = "This is not a party.Party, it's a string."
        cls.test_party = party.Party(name="Michael")
        cls.not_an_expense = ["This is not an expense.Expense, it's a list."]
        cls.test_expense = expense.Expense(paid_for="Impulse purchase", currency="USD", amount=153.19)
        cls.not_a_payment = {"This is not a payment.Payment": "This is a dict."}
        cls.test_payment = payment.Payment(expense=cls.test_expense, paid_by=cls.test_party, currency="USD", amount=10)

    def test_assertion_error_if_add_not_party(self):
        with pytest.raises(AssertionError):
            self.test_group.add_party(self.not_a_party)

    def test_no_error_if_add_party(self):
        self.test_group.add_party(self.test_party)
        assert len(self.test_group.parties) == 1

    def test_assertion_error_if_add_not_expense(self):
        with pytest.raises(AssertionError):
            self.test_group.add_expense(self.not_an_expense)

    def test_no_error_if_add_expense(self):
        self.test_group.add_expense(self.test_expense)
        assert len(self.test_group.expenses) == 1

    def test_assertion_error_if_add_not_payment(self):
        with pytest.raises(AssertionError):
            self.test_group.add_payment(self.not_a_payment)

    def test_no_error_if_add_payment(self):
        self.test_group.add_payment(self.test_payment)
        assert len(self.test_group.payments) == 1

