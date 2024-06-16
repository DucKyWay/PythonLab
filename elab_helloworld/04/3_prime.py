x = int(input())

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

if x <= 1:
    print("ERROR")
else:
    if isPrime(x):
        print(f"Yes, {x} is a Prime number")
    else:
        print(f"No, {x} is not Prime")