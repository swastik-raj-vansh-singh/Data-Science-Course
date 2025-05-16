# OOP -> OGJECT ORIENTEF LANGUAGE 

# -- its is a programing paradigm that revolves around the obejcts and classes 
# -- OBJECT -> these are the real world entity created using the class
# -- CLASS -> it is a template or the blueprint use to create an object 
 

# class Dog :

#     # creating a constructor
#     def __init__ (self, name,age):
#         self.nam = name
#         self.ummar = age

#     # creating a method
#     def sound(self):
#         print(f"{self.nam}-{self.ummar} barks")    

# obj = Dog("swastik",2)
# obj.sound()



# making a bank system 

class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance 

    def deposite(self,amount):
        self.balance += amount
        print (f"{amount} has been deposite")

    def withdrawl(self,amount):
        if (amount < self.balance):
            self.balance -= amount 
            print(f"{amount} has be withdrawled")
        else:
            print ("insufficient amount")

    def checkBalance(self):
        print (self.balance)

obj = BankAccount("swastik",50000)
obj.checkBalance()
obj.deposite(32000)
obj.withdrawl(13000)
obj.checkBalance()