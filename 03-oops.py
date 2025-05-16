## OOP -> OGJECT ORIENTEF LANGUAGE 

##-- its is a programing paradigm that revolves around the obejcts and classes 
## -- OBJECT -> these are the real world entity created using the class
## -- CLASS -> it is a template or the blueprint use to create an object 
 

## class Dog :

#     # creating a constructor
#     def __init__ (self, name,age):
#         self.nam = name
#         self.ummar = age

#     # creating a method
#     def sound(self):
#         print(f"{self.nam}-{self.ummar} barks")    

# obj = Dog("swastik",2)
# obj.sound()



## making a bank system 

# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name = name
#         self.balance = balance 

#     def deposite(self,amount):
#         self.balance += amount
#         print (f"{amount} has been deposite")

#     def withdrawl(self,amount):
#         if (amount < self.balance):
#             self.balance -= amount 
#             print(f"{amount} has be withdrawled")
#         else:
#             print ("insufficient amount")

#     def checkBalance(self):
#         print (self.balance)

# obj = BankAccount("swastik",50000)
# obj.checkBalance()
# obj.deposite(32000)
# obj.withdrawl(13000)
# obj.checkBalance()



## INHERITANCE
# class car:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color

#     def carSpeed(self,speed):
#         print (f"{self.name} have the top speed {speed} ")

# class kia(car):
#     def __init__ (self,name,color,model):
#         super().__init__(name,color)  # Here we user super keyword 
#         self.model = model

#     def selfDrive(self):
#         print(f"{self.name} Support {self.model}")

# obj = car("swastik","gray")
# obj.carSpeed(100)

# obj2 = kia("swastik","gray","base")
# obj2.selfDrive()


## multi class inheritance
# class Animals :
#     def __init__ (self,name):
#         self.name= name
    
#     def speak(self):
#         print("animal class")

# class pet:
#     def __init__(self,owner):
#         self.owner = owner

# class Dog(Animals,pet):
#     def __init__ (self,name,owner):
#         Animals.__init__(self,name)
#         pet.__init__(self,owner)

#     def identity(self):
#         print(f"{self.owner} ows {self.name}")

# obj = Dog("bunny","swastik")
# obj.identity()


## Polymorphism --> method overriding

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print("sound of the animal")

# class Dog(Animal):
#     def speak(self):
#         print("this is dog speaking ")

 
# obj = Dog("swastik")
# obj.speak()


# # Interfaces -- Abstract class
# from abc import ABC, abstractmethod

# class vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

# class car(vehicle):
#     def start_engine(self):
#         return ("car engine")
    
# obj = car()
# print(obj.start_engine())



# Encapsulation 

# private 
class Person:
    def __init__ (self,name,age,gender):
        self.__name = name  #yeh bn gaya pvt variable 
        self.age = age  # this is normal public var
        self._gender = gender

    def getName(self):
        return (self.__name)
    
class ToCheckProtectedVariable(Person):
    def check(self):
        print(f"{self._gender}")


obj1 = Person("Swastik",23,"male")
print(obj1.getName())
# print(obj1.__name)   # this give error

print(obj1.age)       # work fine 
obj2 = ToCheckProtectedVariable("Swastik",23,"male")
obj2.check()

