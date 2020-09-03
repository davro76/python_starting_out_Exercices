# This program calculates and displays gross play.

def main():
    
    #Get the number of hours worked.
        hours = int(input('How many hours did you work:'))
    #Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))
     # Calculate gross pay.
        gross_pay = hours * pay_rate

     # Display the gross play.
        print('Gross pay: $', format(gross_pay, ',.2f'))
          
# Call the main function.
main()
