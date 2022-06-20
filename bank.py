from datetime import datetime


class Account:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=100

       
        self.total=[]
        self.loan=0

    def deposit(self,amount):
#updating deposit transaction with dictionary

        if amount <=0:
            return f"Deposit must be positive amount"
        else:
            now= datetime.now()
            update={ 
            "date":now, 
            "amount":amount,
             "narration":'deposit'}
            self.balance+=amount
            self.deposits.append(amount)
            self.total.append(update)

            return f"Hello {self.account_name} your current balance is {self.balance} and the amount of deposits are {self.deposits} and the statement is {self.total}"

    def withdraw(self,amount):
#updating withdaw transaction with dictionary

        if amount<=0:
             return f"Deposit must be positive amount" 
        elif amount>self.balance:
            return f"Hello {self.account_name} your balance is {self.balance},you cannot withdraw {amount}"
        elif amount+self.transaction>self.balance:
            return f"Hello {self.account_name} your balance is {self.balance},you cannot withdraw {amount}"
        else:
            now= datetime.now()
            upgrade ={ 
            "date":now,
             "amount":amount,
              "narration":'withdraw'
              }
            self.total.append(upgrade)
            self.balance-=amount+self.transaction
            self.withdrawals.append(amount)
            return f"Hello {self.account_name} you have withdrawn {amount} your current balance is {self.balance} and the transaction fee was {self.transaction} and the amount of withdrawals are {self.withdrawals} and the statement is {self.total}"

    def deposits_statement(self):
            for x  in self.deposits:
                print(x,end="\n")
            
    
    def withdrawals_statement(self):
            for b in self.withdrawals:
                print(b,end="\n")

    def current_balance(self):
        return f"{self.balance}"

#full statement method
    def full_statement(self):
        for item in self.total:
            date=item["date"]
            amount=item["self.amount"]
            narration=item["narration"]
            print(f"{date} {narration}  {amount} ")


    #borrow method
    def borrow(self, borrow_loan):
        self.borrow_loan=borrow_loan
        self.interest=0.03*self.borrow_loan
        if len(self.deposits)>10 and borrow_loan<=sum(self.deposits)//3 and borrow_loan>100 and self.balance<0:
            print(f"Hello {self.account_name} you need to have recieved {borrow_loan} your current balance is {self.amount}")
        else:
            print(f"Hello {self.account_name} you cannot get a loan")

#loan repayments
    def repay_loan(self,amount_repayloan):
        self.amount_repayloan=amount_repayloan
        total_payment=amount_repayloan+self.interest
        remaining_loan=self.borrow_loan-total_payment
        if total_payment>0:
            print(f"Hello {self.account_name}You have deposited {self.amount_repayloan} your loan of {self.borrow_loan}Ksh.Your new loan balance is {self.balance}Ksh")
        elif total_payment>remaining_loan:
            print(f"Congratulations {self.account_name}!! You have cleared your loan of{amount_repayloan}.Your new balance is{self.balance}")

        else:
             print(f"Hello {self.account_name} You have a loan balance of {amount_repayloan}")


#transfer method
    def transfer(self,amount,new_account):
        self.new_account=new_account
        self.amount=amount
        current_balance=self.balance-amount
        if amount<=0:
            print(f" Hello {self.account_name } You cannot transfer a non-existant amount")
        elif amount>self.balance:
            print(f"Hello {self.account_name} Your cannot transfer {amount}.Your current balance is {self.balance}")
        elif amount<self.balance:
             print(f"Hello {self.account_name} You have transfered {amount} to {self.new_account} your balance is {current_balance}")



