class BankAccount:
    def __init__(self, account_balance=0):
        # Ensure we don't start with a negative balance
        self._account_balance = max(account_balance, 0)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self._account_balance
        
        self._account_balance += amount
        print(f"Deposited: ${amount:,.2f}. New Balance: ${self._account_balance:,.2f}")
        return self._account_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self._account_balance
        
        if amount > self._account_balance:
            print(f"Insufficient funds. Current balance: ${self._account_balance:,.2f}")
            return self._account_balance
        
        self._account_balance -= amount
        print(f"Withdrew: ${amount:,.2f}. Remaining Balance: ${self._account_balance:,.2f}")
        return self._account_balance

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:,.2f}")
        return self._account_balance
