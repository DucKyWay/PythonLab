def fibo(n):
    fibonacci = [1, 1, 2, 3, 5]
    if n >= 4:
        for i in range(4, n):
            fibonacci.append(fibonacci[i] + fibonacci[i-1])
    return fibonacci[n]

n = int(input())
print(f"fibonacci({n}) = {fibo(n)}")