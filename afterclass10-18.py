arr=''
for i in range(32):
    if i == 2 or i ==7 or i ==12 or i ==17 or i ==22 or i ==27 :
        arr+=' '   
    else:
        i=input()
        arr+=i

class Bank_account():
    def __init__(self):
        self.account_balance=0
        self.account_number=arr
    def deposit(self, balance):
        self.account_balance+=balance
    def pay_out(self, balance):
        if (self.account_balance)>balance:
            self.account_balance-=balance
        else:
            print(f'Za mało środków na koncie')
    def account_status(self):
        print(f'\nBank Account No:{self.account_number}\n')
        print(f'Balance: PLN {self.account_balance}')
        
ba=Bank_account()
ba.account_status()
ba.deposit(25.30)
ba.account_status()
ba.pay_out(31.70)
ba.account_status()
ba.pay_out(14)
ba.account_status()