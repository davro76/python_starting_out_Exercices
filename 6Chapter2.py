# Getting the amount of purchase

amountpurchased = float(input('Enter the amount of purchase:'))

county_percentage_sales_tax = 0.025

state_percentage_sales_tax = 0.05

# Calculate state sales tax, county sales tax, total sales tax and total of the sale 

amount_county_sales_tax = amountpurchased * county_percentage_sales_tax

amount_state_sales_tax = amountpurchased * state_percentage_sales_tax

total_sales_tax = amount_county_sales_tax + amount_state_sales_tax 

total_sale = amountpurchased + total_sales_tax


# Display county, state sales tax, total sales tax and total sale

print('County sale tax is:', '$', format(amount_county_sales_tax,',.2f')) 

print('State sale tax is:', '$', format(amount_state_sales_tax,',.2f'))

print('Total sales tax is:', '$', format(total_sales_tax, ',.2f'))

print('Total purchased is:', '$', format(total_sale,',.2f'))





