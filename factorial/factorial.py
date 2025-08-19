def factorial(n):
    if n<0:
        return "factorial of a number is not negative"
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter a number"))
print(f"the factorial {num}:is {factorial(num)}")

