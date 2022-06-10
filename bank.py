class Account:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits=[]
        self.withdrawals=[]

    def deposit(self,amount):
        if amount <=0:
            return f"Deposit must be positive amount"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f"Hello {self.account_name} your current balance is {self.balance} and the amount of deposits are {self.deposits}"
#withdrawal conditions
#amount requested should be less than or equal to the balance
#the amount should not be negative
    def withdraw(self,amount):
        self.transaction=100
        if amount<=0:
             return f"Deposit must be positive amount" 
        elif amount>self.balance:
            return f"Hello {self.account_name} your balance is {self.balance},you cannot withdraw {amount}"
        else:
            self.balance-=amount+self.transaction
            self.withdrawals.append(amount)
            return f"Hello {self.account_name} you have withdrawn {amount} your current balance is {self.balance} and the transaction fee was {self.transaction} and the amount of withdrawals are {self.withdrawals}"

    def deposits_statement(self):
            for x  in self.deposits:
                print(x,end="\n")
            
    
    def withdrawals_statement(self):
            for b in self.withdrawals:
                print(b,end="\n")

    def current_balance(self):
        return f"{self.balance}"

    
    

# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.
        