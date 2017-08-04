class Party:

    def __init__(self, name: str, email: str = None, venmo_id: str = None):
        self.name = name.strip()
        self.email = email
        self.venmo_id = venmo_id

    def has_linked_email(self) -> bool:
        if self.email:
            return True
        else:
            return False

    def has_linked_venmo(self) -> bool:
        if self.venmo_id:
            return True
        else:
            return False
