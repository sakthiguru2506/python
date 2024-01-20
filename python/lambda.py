"""
x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(5,10))

def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(5)
a=myfunc(5)
print(a(2))
print(mydoubler(10))
print(mydoubler(20))
print(mydoubler(5))
"""
data = (1,2,3,4,5)
result1 = map(lambda x:x*2,data)
print(list(result1))

result2 = filter(lambda x:x%2==0,data)
print(list(result2))
