def sum(a,b):
    A=(a+b)
    print("the sum is", A)

  
def multiply(a,b):
    A=(a*b)
    print("the product is", A)

  
def subtract(a,b):
    A=(a-b)
    print("the difference is", A)

  
def divide(a,b):
    A=(a/b)
    print("the dividend is", A)

  
x=int(input("Type number 1: "))
y=int(input("Type number 2: "))
z=input("Type the operation sign (+, -, *, /)")

  
if(z=="-"):
    subtract(x , y)

elif(z=="+"):
    sum(x,y)

elif(z=="*"):
    multiply(x,y)

elif(z=="/"):
    divide(x,y)

else:
    print("error")

