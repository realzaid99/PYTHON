def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# User input
c = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", celsius_to_fahrenheit(c))

f = float(input("Enter temperature in Fahrenheit: "))
print("Celsius:", fahrenheit_to_celsius(f))