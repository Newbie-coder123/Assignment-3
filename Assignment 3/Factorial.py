def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
b=1
while b == 1:
    a=input("Enter a number: ")
    a=int(a)
    if a==0:
        print("The number is 0 factorial not possible")
    else:
        print("The factorial of ",a," is ",factorial(a))
    b=int(input("Enter 1 to continue and anything else to exit "))
print("Thank you")