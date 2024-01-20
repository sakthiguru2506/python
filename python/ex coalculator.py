def add(a,b):
    print("Addition value is",(a+b))
def sub(a,b):
    print("Subtration value is",(a-b))
def mul(a,b):
    print("Multiplication value is",(a*b))
def div(a,b):
    print("Division value is",(a/b))
z=1
while(z==1):
    x=int(input("Enter the first value:"))
    y=int(input("Enter the second value:"))
    print("1.Addition\n2.subtration\n3.maliplication\n4.division\n")
    c=int(input(" Ender your choice:"))
    if(c==1):
        add(x,y)
    elif(c==2):
        sub(x,y)
    elif(c==3):
        mul(x,y)
    elif(c==4):
        div(x,y)
    else:
        print("please ender the value")
    z=int(input("if you want continue please enter 1:"))
    
