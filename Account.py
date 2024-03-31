""" Create an Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest_gained):
        self.balance = balance
        self.interest_gained = interest_gained

    # This method gets the balance on the account.
    def get_balance(self):
        """Outputs the balance of the account."""
        return self.balance
    
    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # This method gets the interest gained on the account.
    def get_interest_gained(self):
        """Output the interest gained."""
        return self.interest_gained

    # The method sets the interest gained for the account.
    def set_interest_gained(self, interest):
        """Sets the interest gained for the the account"""
        self.interest_gained = interest
