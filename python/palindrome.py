def strreverse(n):
    b=n[::1]
    return b
def reverse(n):
    b=0
    while(n>0):
        r=n%10
        b=(b*10)+r
        n=n//10
    return b
def check(a,b):
    if(a==b):
        print("It is a palindrome")
    else:
        print("It is a not a palindrome")
o=1
while(o==1):
 c=int(input("1.Integer reverse2.string reverse:"))
 if(c==1):
    a=int(input("Enter tha value"))
    b=reverse(a)
    check(a,b)
 elif(c==2):
    x=input("Enter tha sring value:")
    y=strreverse(x)
    check(x,y)
 else:
    print("you Enter wrong one")
 o=int(input("If you want to coutiune pls enter 1:"))
