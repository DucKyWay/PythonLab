import math
radius = float(input("Enter Radius: "))

def calculateCircleArea(radius):
    area = math.pi * radius * radius
    return area

Area = calculateCircleArea(radius)
print(f"The Circle area with radius {radius:.2f}")
print(f"Is {Area:.2f}")



