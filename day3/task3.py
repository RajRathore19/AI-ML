#practice 3

class Shape:
    def area(self):
        print("area of shape")

class Circle(Shape):
    def __init__(self,a):
        self.a=a
        
    def area(self):
        print("area of circle ",(3.14*self.a*self.a))

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        print("area of Rectangle ",self.l*self.b)

class Triangle(Shape):
    def __init__(self,h,b):
        self.h=h
        self.b=b
        
    def area(self):
        print("area of Triangle ",0.5*self.h*self.b)

obj1=Circle(10)
obj1.area()

obj2=Rectangle(10,20)
obj2.area()

obj3=Triangle(5,2)
obj3.area()

