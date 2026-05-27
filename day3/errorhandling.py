data = input("Enter no :")

print("befor handling")

try:
    val = int(data)
    for i in range(1,11):
        print(i*val)
    print("Table is printed")

except :
    print("Your enter data is not a number")


print("After handling")