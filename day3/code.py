with open("sample.txt","r") as fs:
   val = fs.readlines()
   count=0;
   for i in val:
    val2 = i.find("indore")
    count+=1
    if val2 == -1:
      continue
    else:
      break

print("Data is found in index",val2,"line no :",count)


# with open ("sample1.txt","a+") as fs:
#   fs.write("hello python")
#   data = fs.readline()
# print(data)