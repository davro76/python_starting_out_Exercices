# Getting Celsius temperature
celsius_temperature = float(input('Enter the Celsius temperature:'))

# Convert Celsius temperature to Fahrenheit
slope = 1.8
y_intercept = 32
fahrenheit = (slope*celsius_temperature) + y_intercept

# Display the Fahrenheit temperature
print("The temperature in Fahrenheit's degree is:", format(fahrenheit, ',.2f'))



