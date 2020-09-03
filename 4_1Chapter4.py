# Create a variable to control the loop
KeepGoing ='y'

# Calculate a serie of commissions
while KeepGoing =='y':

	# Get a salesperson's sales and commission rate
	Sales = float(input('Enter the amount of sales:'))
	Commission_Rate = float(input('Enter the commission rate:'))

	# Calculate the commission
	Commission = Sales * Commission_Rate

	# Display the commission
	print('The Commission is $', format(Commission, ',.2f'))

	# See if the user wants to do another one
	KeepGoing = input('Do you want to calculate another commission (Enter y or n):')


    


	