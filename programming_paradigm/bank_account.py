class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
            return 0
        
        self.account_balance -= amount
        return self.account_balance
    
    def display_balance(self):
        print("Current Balance: ", self._account_balance)
        return self.account_balance
