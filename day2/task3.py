# Practice problems
#1 palindrom

# text = input("Enter String :")
# rev = ""
# for i in text:
#     rev = i + rev

# if text.lower() == rev.lower() :
#     print("palindrom")
# else:
#     print("Not a Palindrom")


#2 list avg

# list = [10,20,30,40]
# sum=0
# for i in list:
#     sum+=i
# print(sum)
# print("Average :",sum/4);

#3 list 

# list1 =[]
# for i in range(0,5):
#     val = int(input("Enter list element :"))
#     list1.append(val)

# list2 =[]
# for j in range(0,5):
#     val = int(input("Enter list element :"))
#     list2.append(val)

# list3 = list1 + list2
# val = set(list3)
# list3.sort()
           
# print(val)


#4 dictionary

dic={"name":{
    1:"raj",
    2:"jay"
},
"marks":{
    1:90,
    2:85
}}
print(dic["name"][1],dic["marks"][1])


u = "Raju"
print(u[::-1])