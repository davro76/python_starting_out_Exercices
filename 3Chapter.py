#3Chapter3

# Equivalence of Square Feet in acre
OneAcre = 43560 

#Getting the number of square feet

TotalSquareFeet = float(input('Enter the total of square feet:'))

#Convert the total square feet to acre 
TotalAcre = TotalSquareFeet / OneAcre

# Print TotalAcre

print('The total number of acre is:', format(TotalAcre, ',.2f'))
