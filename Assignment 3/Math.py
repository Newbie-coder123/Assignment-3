import math
def func(a):
    print(f"The square root of {a} is{math.sqrt(a)}")
    print(f"The log of {a} is {math.log(a,10)}")
    print(f"The sin of {a} is {math.sin(a)}")
num=1
while num==1:
    b=int(input(" Enter a number to calculate the square root,natural log, and sin value of the number"))
    func(b)
    num=int(input(" Enter 1 to find the values for another number and any other number to exit"))
print("Thankyou")