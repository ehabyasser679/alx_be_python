FAHRENHEIT_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            type_of_temperature = input("Is the temperature in Celsius or Fahrenheit? ")

            if type_of_temperature.lower() == "celsius":
                fahrenheit = convert_to_fahrenheit(temperature)
                print(f"The temperature in Fahrenheit is {fahrenheit:.2f}")
                break
            elif type_of_temperature.lower() == "fahrenheit":
                celsius = convert_to_celsius(temperature)
                print(f"The temperature in Celsius is {celsius:.2f}")
                break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()