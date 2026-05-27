# String formatting
f""" This is multi 
line command """

# user = "raj"
# print("hi {}".format(user))

user = "raj"
print(f"hello {user}");

#string function

str = 'this in python code'
val = str[1:4]
print(val)
val2= str.find("i")
print(val2)
val3= str.upper()
print(val3)
val4= str.title()
print(val4)
val5= str.strip()#it help to remove white sapce both side
print(val5)
val6= str.isalpha()# it return true if string contain only letter not space and any special character or digit
print(val6)
val7= str.isalnum()# it check only letter and number 
print(val7)