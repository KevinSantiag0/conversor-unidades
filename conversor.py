import math
from datetime import datetime


def celsius_to_fahrenheit(c):
    return c * 9/5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def volts_to_milivolts(v):
    return v * 1000


def millivolts_to_volts(m):
    return m * 0.001


def amps_to_milliamps(a):
    return a * 1000


def milliamps_to_amps(ma):
    return ma/1000


def hertz_to_rad(h):
    return h * 2 * math.pi


def history(value, origin, result, target):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"{now} | {value} {origin} = {result:.2f} {target}\n")


def show_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("No history yet")


CONVERSIONS = {
    "1": ("°C", "°F", celsius_to_fahrenheit),
    "2": ("°F", "°C", fahrenheit_to_celsius),
    "3": ("V", "mV", volts_to_milivolts),
    "4": ("mV", "V", millivolts_to_volts),
    "5": ("A", "mA", amps_to_milliamps),
    "6": ("mA", "A", milliamps_to_amps),
    "7": ("Hz", "rad/s", hertz_to_rad)
}


def show_menu():
    print("=== Unit converter ===")
    for key, (origin, target, func) in CONVERSIONS.items():
        print(f"{key}) {origin} → {target}")
    print("h) History")
    print("0) Exit")


def ask_num(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("That's not a number, try again")


while True:
    show_menu()
    option = input("Choose an option: ")

    if option == "0":
        print("Bye :)")
        break

    if option == "h":
        show_history()
        continue

    if option not in CONVERSIONS:
        print("Invalid option")
        continue

    origin, target, func = CONVERSIONS[option]
    value = ask_num(f"Value in {origin}: ")
    result = func(value)
    print(f"{value} {origin} = {result:.2f} {target}")
    history(value, origin, result, target)
