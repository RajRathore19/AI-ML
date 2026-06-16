# List Comprehension

# val = [i for i in range(1,11)]
# print(val)

# val1 =[i*2 for i in range(1,11)]
# print(val1)

# val2 = [i for i in range(1,11) if i%2==0]
# print(val2)

# dic = {i:i*2 for i in range(1,11)}
# print(dic)



# prime number
# var = int(input("Enter value"))
# flag=False
# for i in range(2,var):
#     if var % i==0:
#       flag=True  
#       break
    
# if flag:
#    print("Not a Prime No")
# else:
#    print("Prime number")

#palindrom
# str = input("Enter string ")
# rev=""
# str2 = str[::-1]
# print(str2)
# for ch in str:
#    rev = ch + rev
# print(rev)

#vowel and consonent

# data = input("enter string here : ")
# vowel=0
# con=0
# for i in data:
#     if i in "aeiou":
#         vowel+=1
#     else:
#         con+=1
# print("no of vowel is",vowel ,"consonent is",con)


#fact

# def fact(n):
#     if n<=0:
#      return 1
#     else:
#        return n* fact(n-1)
# print(fact(5))
# n=5
# f=1
# for i in range(1,n+1):
#    f = f*i
# print(f)

#perform sorting

# arr = [40, 30,10,20]

# swapped = True
# while swapped:
#     swapped = False  # Assume the list is sorted
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#             swapped = True  # A swap occurred, so we need to check again

# print(arr)  # Generates [10, 20, 30, 40] for ANY combination of numbers

# class A:
#     x = 10

# obj1 = A()
# obj2 = A()

# obj1.x = 20

# print(obj2.x)

# class account:
#     def __init__(self,balance,name):
#         self.name =name
#         self.balance=balance
    
#     def deposite(self,amount):
#         self.balance+=amount
    
#     def withdraw(self,amount):
#         self.balance-=amount
    
#     def checkbalance(self):
#         print("your balance",self.balance)

# a1=account(1000,"Raj")
# a1.checkbalance()
# a1.deposite(500)
# a1.withdraw(200)
# a1.checkbalance()

