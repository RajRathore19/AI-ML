# List Comprehension

val = [i for i in range(1,11)]
print(val)

val1 =[i*2 for i in range(1,11)]
print(val1)

val2 = [i for i in range(1,11) if i%2==0]
print(val2)

dic = {i:i*2 for i in range(1,11)}
print(dic)
