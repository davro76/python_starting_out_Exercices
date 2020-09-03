#Global variables
YearlyBaseSalary = 30000
ExperienceJob = 2

# Get salary per year and experience in current job from bank customer
SalaryPerYear = int(input('Please, enter your salary per year:'))
ExperienceCurrentJob =float(input('Please, enter the number of years while you have been worked here:'))

#Determine if any customer is qualify
if SalaryPerYear >= YearlyBaseSalary and ExperienceCurrentJob >= ExperienceJob:
    print('Congratulation!, you qualify for the loan.')	
else:
    print('Sorry!, you are not qualify because ' + \
	      'you must earn at least $ 30,000 per year' + \
	      ' and also have been worked for at least 2 years in your current job.')
