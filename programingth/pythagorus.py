import math
length = input()
length_a, length_b = length.split()
f_length_a = float(length_a)
f_length_b = float(length_b)

c = math.sqrt(f_length_a**2 + f_length_b**2)
print(f"{c:.6f}")