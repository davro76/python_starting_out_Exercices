# Tip and Tax percentage
tip_percentage = 0.18
tax_percentage = 0.07

# Getting the charge for the food
food_charge = float(input('Enter the charge for the food:'))

# Calculate the amount of tip, tax and the total purchased
amount_tip = food_charge * tip_percentage
amount_tax = food_charge * tax_percentage
total_purchased = food_charge + amount_tax + amount_tip

# Display the amounts of tip, tax and the total purchased
 
print('The amount of tip is:', '$', format(amount_tip, ',.2f'))
print('The amount of tax is:', '$', format(amount_tax, ',.2f'))
print('The total amount purchased is:', '$', format(total_purchased, ',.2f'))
