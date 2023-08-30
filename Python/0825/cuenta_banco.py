class Bank_account:
    def __init__ (self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
        
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    

class Savings_account(Bank_account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.__interest_rate = interest_rate

    def interest_return(self):
        interest_earned = self.get_balance() * self.__interest_rate
        self._Bank_account__balance += interest_earned
        return
    
cuenta_ahorro = Savings_account(200, '2305', 0.02)

cuenta_ahorro.interest_return()

print(f'Su saldo despues de interes fue de: {cuenta_ahorro.get_balance()}')