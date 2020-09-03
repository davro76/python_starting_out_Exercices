# Getting the number of miles driven
mile_driven = float(input('Enter the number of miles driven:'))

# Getting the number of gallons of gas used
gallons_used = float(input('Enter the number of gallons of gas:'))

# Calculate the car's MPG
MPG = mile_driven / gallons_used

# Display the car's MPG
print("The car's MPG is:", format(MPG, ',.2f'),'Mile per Gallon')

