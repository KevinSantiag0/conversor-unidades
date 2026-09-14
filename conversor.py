def celsius_to_fahrenheit(c):
    return c * 9/5 + 32


def fahrenheit_to_celsius(f):
    return (f-32)*5/9


def show_menu():
    print("=== Unit converter ===")
    print("1)Celsius → Fahrenheit")
    print("2)Fahrenheit → Celsius")
    print("0)Exit")


while True:

    show_menu()
    option = input("Choose an option: ")

    if option == "1":
        temperature_celsius = float(input("Temperature - °C: "))
        fahrenheit = celsius_to_fahrenheit(temperature_celsius)
        print(f"Temperature in fahrenheit: {fahrenheit:.2f}")
    elif option == "2":
        temperature_fahrenheit = float(input("Temperature - °F: "))
        celsius = fahrenheit_to_celsius(temperature_fahrenheit)
        print(f"Temperature in celsius: {celsius:.2f}")
    elif option == "0":
        print("Bye :)")
        break
    else:
        print("Invalid option")
