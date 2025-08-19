x = int(input("Enter the number: "))
if x <= 1:
    print("Write valid number")
else:
    ft = 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            ft = 1
            break

    if ft == 0:
        print("Given number is Prime number")
    else:
        print("Not a prime number")
