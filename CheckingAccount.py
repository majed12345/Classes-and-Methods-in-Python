class CheckingAccount:
    def __init__(self,name,address,accountNumber,balance):
        self.name=name
        self.address=address
        self.accountNumber=accountNumber
        self.__balance=balance
         
    def creditAccount(self,amount):
        self.__balance=self.__balance + amount

    def debitAccount(self,amount):
        if (self.__balance < amount):
            print("Balance in the debit account ${:.2f} is low. Transaction will not process ${:.2f}.".format(self.__balance,amount))
            print("==============================================")
        else:
            self.__balance=self.__balance-amount
    
    def availableBalance(self):
        print("Account Overview : \nAccount Number   : {} \nAccount Balance  : ${:.2f}  \nAccount holder   : {}".format(self.accountNumber,self.__balance,self.name))
    
    
    
    


    
