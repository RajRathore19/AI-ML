#concept of oop

# class hero:
#     fullname = "spiderman"
#     def __init__(self,name):
#         self.name = name

# hero1 = hero("raj")
# print(f"{hero1.name} is {hero1.fullname}")


# basic code of class

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks=marks

#     def avg_marks(self):
#         sum=0;
#         for i in self.marks:
#             sum+=i
#         print(f"Hello {self.name} your score is {sum/3}")

# s1= student("raj",[98,90,89])
# s1.avg_marks()


#inheritance

class parent:
    def hair(self):
        print("hair color is black")

class child(parent):
    def display(self):
        print("hello")

obj = child()
obj.hair()
obj.display()


#set

# s={1,2,3,2}

# print(s)

# s.remove(1)
# print(s)
# s.pop()
# print(s)
# s.add(1)
# print(s)
