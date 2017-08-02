class Party:

    def __init__(self, name: str, email: str = None, venmo_id: str = None):
        self.name = name
        self.email = email
        self.venmo_id = venmo_id

    def has_linked_email(self) -> bool:
        if self.email is None:
            return False
        else:
            return True

    def has_linked_venmo(self) -> bool:
        if self.venmo_id is None:
            return False
        else:
            return True
