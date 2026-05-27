#Methods(static and class)
# class heros:

#     def display(self,name):
#         self.name=name
#         print(f"hello {self.name}")


#     @staticmethod
#     def show(a,b):
#         print("spiderman")
#         return a+b
    

# h1 = heros()
# print(h1.display("thor"))
# print(heros.show(10,20))


# #class method

# class Student:
#     company ="Apple"

#     def show(self,name):
#         self.name = name
#         print(f"My name is {self.name} and {self.company} is my company")

#     @classmethod
#     def newCompany(cls,new_company):
#         cls.company=new_company


# obj = Student()

# obj.show("Raj")
# #obj.company="Tesla"

# obj.newCompany("Tesla")
# obj.show("Raj")
# print(Student.company)


# DuckTyping
class Animal:
    def speak(self):
        print("animal")
class dog(Animal):
    def speak(self):
        print("I am dog")
class cat(Animal):
    def speak(self):
        print("meow")

class car(Animal):
    def speak(self):
        print("horn")

animals = [Animal(),dog(),cat(),car()]

for i in animals:
    i.speak()

    