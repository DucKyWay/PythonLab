# 1 - Prime Number Checker

def check_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
        else:
            print(num, "is a prime number.")
            break

inputNum = int(input())
while True: 
    if inputNum != 0:
        check_prime(inputNum)
        inputNum = int(input())
    elif inputNum == 1:
        print("Invalid input, try again.")
        inputNum = int(input())
    else:
        print("End of program, goodbye.")
        break