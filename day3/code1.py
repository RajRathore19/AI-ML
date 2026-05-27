with open("sample.txt","r") as fs:
   val = fs.readlines()
   count=0;
   lsit=[]
   for i in val:
    val2 = i.find("indore")
    count+=1
    if val2 == -1:
      continue
    else:
      lsit.append(f"{count},{val2}")
     
for i in lsit:
    print("Data is found in Line and index is",i)

#print(lsit)