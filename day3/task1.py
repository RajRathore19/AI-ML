#Practice problem 1

class Bank_account:
    def __init__(self,Acc_no,Owner_name,Balance=0):
           self.Acc_no=Acc_no
           self.Owner_name=Owner_name
           self.Balance=Balance

    def deposite(self,amount):
          if amount > 0:
            self.Balance+=amount;
            print(f"Deposite {amount}")   

    def Withdraw(self,amount):
        if amount >0 :
                self.Balance-=amount
                print(f"Withdraw amount :{amount}")
        else:
            print("Invalid")

    def check_balance(self):
         if self.Balance < 0:
                print(f"Insufficent balace")
         else:
                print(f"Your balance is {self.Balance}")
         
holder = Bank_account(25012546,"Raj Rathore",500);
holder.check_balance()
holder.deposite(1000)
holder.check_balance()
holder.Withdraw(500)
holder.check_balance()
