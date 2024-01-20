def add(a,b):
    return(a+b)
c=add(12,28)
print(c*5)

#calcculator

def add(a,b):
    print("Addition value is", a+b)
def sub(a,b):
    print("Subtration value is",a-b)
def mul(a,b):
    print("mulitiplication vaue is",a*b)
def div(a,b):
    print("Division value is",a/b)
z=1
while(z==1):
    x=int(input("Enter the first value:"))
    y=int(input("Enter tha second value:"))
    print("1.Addition\n2.subtration\n3.malitiplication\n4.division")
    c=int(input("Enter your choise:"))
    if(c==1):
        add(x,y)
    elif(c==2):
        sub(x,y)
    elif(c==3):
        mul(x,y)
    elif(c==4):
        div(x,y)
    else:
        print("please enter valid input")
    z=int(input("if you want continue please enter 1:"))
