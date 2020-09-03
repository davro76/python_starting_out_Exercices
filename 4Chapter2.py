# Getting item prices
article_1 = float(input('Enter the price for the first item:'))

article_2 = float(input('Enter the price for the second item:'))

article_3 = float(input('Enter the price for the third item:'))

article_4 = float(input('Enter the price for the fourth item:'))

article_5 = float(input('Enter the price for the fifth item:'))

# Percentage sales tax
percentageSalesTax = 0.07

# Calculate subtotal of the sale, amount of sales tax and the total
subtotal=article_1+article_2+article_3+article_4+article_5
subtotal_tax=subtotal* percentageSalesTax
total_sales = subtotal + subtotal_tax

#Display subtotal, amount sales tax and total sales

print('subtotal is:', '$', format(subtotal, ',.2f'))

print('subtotal_tax is:', '$', format(subtotal_tax, ',.2f'))

print('total_sales is:', '$', format(total_sales, ',.2f'))



