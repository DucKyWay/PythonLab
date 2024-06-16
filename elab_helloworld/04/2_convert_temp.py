temp = float(input("Enter Celsius: "))

def celsiusToRomer(temp):
    r = (temp/5) * 4
    return r


def celsiusToKelvin(temp):
    k = (temp/5) * 5 + 273.15
    return k


def celsiusToFahrenheit(temp):
    f = (temp/5) * 9 + 32
    return f

print(f"Romer => {celsiusToRomer(temp):.2f}")
print(f"Kelvin => {celsiusToKelvin(temp):.2f}")
print(f"Fahrenheit => {celsiusToFahrenheit(temp):.2f}")