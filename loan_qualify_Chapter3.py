# This program allows users to see if they are qualify for a loan
# Required to qualify for the loan, minimum anual wage >= $ 30000
# >= 2 years at your current job

# Getting the anual wage 
anual_wage = float(input("Enter your anual wage:"))

# Decided whether the customer is qualify for the loan
if anual_wage >= 30000:
# Getting the number of years on the current job
    years = int(input('Enter the number of years you have on this cuurent job:'))
    if years >= 2:
      print("Congratulation, you qualify for the loan.")
    else:
      print('Sorry, you must have been employed for at least two years.')
          
else:
    print('Sorry, you must have been earned at least $ 30000 by year.')
    
    
    
