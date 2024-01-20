
n=int(input("Enter tha value:"))
a=1
b=1
while(a<=n):
    b=(b*a)
    a+=1
    print(b)
    
n=int(input("Enter tha value:"))
b=1
while(n>0):
    b=b*n
    n-=1
    print(b)
    

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=5
print("The factorial of",num,"is",factorial(num))
