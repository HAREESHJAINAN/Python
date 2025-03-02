
"""
num = int(input("Enter a number: "))

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


print("Factorial:", factorial(num))
"""


#Example2

n =int(input("Enter a number: "))
ans=1
if n==0:
    print(1)
elif n<0:
    print("error, Please enter positive value")

else:
    for i in range(1,n+1):
        ans=ans*i
print(ans)
