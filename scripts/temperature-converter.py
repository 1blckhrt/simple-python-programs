### Temperature Converter ###
# This program converts temperatures between Fahrenheit and Celsius
# The user is prompted to input a temperature and a unit (F or C)
# The program then outputs the converted temperature

def temperatureConverter():
    temperature = input("Enter temperature: \n")
    unit = input("Enter the unit your current temperature is in, and this program will convert it to the opposite:. (F/Fahrenheit, C/Celsius): \n").lower()
    try:
        temperature = float(temperature)
    except:
        raise ValueError("Please enter a valid temperature! Returning to start...")
    
    if not temperature or not unit:
        print("Error: please enter a valid temperature and unit! Returning to start...\n")
        return temperatureConverter()
    
    if unit not in ['f', "fahrenheit", 'c', 'celsius']:
        print("Error: please enter either F or C as the unit! Returning to start...\n")
        return temperatureConverter()
    
    def convertToCelsius():
        nonlocal temperature
        nonlocal unit
        final_temperature = (temperature - 32) * 5/9

        print(f"\nOriginal Temperature: {temperature}°{unit.upper()}")
        print(f"Converted Temperature: {final_temperature}°C")

    def convertToFahrenheit():
        nonlocal temperature
        nonlocal unit
        final_temperature = (temperature * 9/5) + 32

        print(f"\nOriginal Temperature: {temperature}°{unit.upper()}")
        print(f"Converted Temperature: {final_temperature}°F")

    if unit in ['f', 'fahrenheit']:
        convertToCelsius()

    elif unit in ['c', 'celsius']:
        convertToFahrenheit()

temperatureConverter()