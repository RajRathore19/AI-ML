str = input("enter string :")
list=[]
for i in str:
  if i in "aeiou":
       list.append(i) 
  elif i in "AEIOU":
        list.append(i)
  else:
      continue
print(list)
  
