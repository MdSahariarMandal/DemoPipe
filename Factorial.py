a=int(input("Enter the number : "))
def Factorial (n):
    b=1
    for i in range (1,n+1):
        b=b*i
    return b
c=Factorial(a)
print("The factorial is : ",c)