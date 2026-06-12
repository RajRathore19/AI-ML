def fib(n):
    if n<=0:
        return n
    elif n==1:
        return 1
    v =0
    for i in range(n):
        
        v= v+i
    return v
for i in range(8):
    print(fib(i))
