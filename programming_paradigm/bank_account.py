class BankAccount:
    def __init__(self, account_balance = 0):
        self._account_balance = max(account_balance, 0)

    def deposit(self, amount):
        self._account_balance += amount

        if self._account_balance < 0:
            self._account_balance = 0
            print(f"Deposit amount must be positive.")
            return 0
        
        elif self._account_balance == 0:
            print(f"Account is empty")
            return 0
        
        else:
            print(f"Deposited: ${self._account_balance:,.2f}")
            return self._account_balance
    
    def withdraw (self, amount):
        
        self._account_balance -= amount

        if self._account_balance < 0:
            self._account_balance = 0
            print("Withdrawal amount must be positive.")
            return 0
        
        elif self._account_balance == 0:
            print(f"Account is empty")
            return 0
        
        elif self._account_balance < amount:
            print(f"Insufficient funds.")
            return self._account_balance
        
        else:
            print(f"Withdrew: ${self._account_balance:,.2f}")
            return self._account_balance
    
    def display_balance(self):
        print("Current balance is: ", self._account_balance)
        return self._account_balance
    
    
