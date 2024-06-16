x = int(input("Enter your number: "))

def diyFactorial(x):
    if x <= 1:
        return 1
    else:
        return x * diyFactorial(x-1)

if x >= 0:
    print(f"Factorial of {x} ({x}!) = {diyFactorial(x)}")
else:
    print("ERROR")