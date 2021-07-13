print("Welcome to the Temperature Conversion App")

#Gather user input
temp_fahrenheit = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))

#convert temps
temp_celsius = (5/9)*(temp_fahrenheit - 32)
temp_kelvin = temp_celsius + 273.15

#Round temps
temp_fahrenheit = round(temp_fahrenheit, 4)
temp_celsius = round(temp_celsius, 4)
temp_kelvin = round(temp_kelvin, 4)

#Summary table
print("\nDegrees Fahrenheit:\t" + str(temp_fahrenheit))
print("Degrees Celsius:\t" + str(temp_celsius))
print("Degrees Kelvin:\t\t" + str(temp_kelvin))
