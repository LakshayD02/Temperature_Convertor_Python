def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

while True:
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        temperature = float(input("Enter temperature value: "))
        if choice == '1':
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result}°F")
        elif choice == '2':
            result = celsius_to_kelvin(temperature)
            print(f"{temperature}°C is equal to {result} K")
        elif choice == '3':
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result}°C")
        elif choice == '4':
            result = fahrenheit_to_kelvin(temperature)
            print(f"{temperature}°F is equal to {result} K")
        elif choice == '5':
            result = kelvin_to_celsius(temperature)
            print(f"{temperature} K is equal to {result}°C")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} K is equal to {result}°F")
    else:
        print("Invalid input. Please choose a valid option.")