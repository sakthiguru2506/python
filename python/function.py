def hat():
    print("Hello from  a  function")
    print("Yes this is function ")
    print("A function is a block of code wich only runs when it is called.")
print("hai")
hat()

#function passing prameters
def my_function(fname):
    print(fname+"wecome")
my_function("Raja")
my_function("Pugal")
my_function("afil")

def add(a,b):
    print(a+b)
add(4,5)
add(7,5)

def harry(fname,lname):
    print(fname+" "+lname)
a=input("Enter tha a")
b=input("Enter tha b")
harry(a,b)

def my_function(c,b,a):
    print("The youngest child is" + c)
my_function(a="balaji",b="mahesh",c="marish")
def my_function(**c):
    print("The youngest child is"+c["a"])
