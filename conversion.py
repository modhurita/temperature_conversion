# Functions to make temperature conversions

 def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius/5*9 + 32
    return fahrenheit
    
# Mancy's version
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# New function
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius_to_fahrenheit(celsius)
