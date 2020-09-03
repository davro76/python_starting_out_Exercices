# Get the number of hours worked, the hourly pay rate and store the limit hour worked by week
hours_worked = float(input("Enter the number of hours worked:"))
hours_pay_rate = float(input("Enter the hourly pay rate:"))
limit_hour = 40
overtime_multiplier = 1.5
   
if hours_worked > limit_hour:
    overtime_hour = hours_worked - limit_hour
    amount_overtime = overtime_hour * hours_pay_rate * overtime_multiplier
    gross_pay = hours_worked * hours_pay_rate + amount_overtime
else:
    gross_pay = hours_worked * hours_pay_rate

print('The gross pay is:', '$', format(gross_pay, ',.2f'))
 

