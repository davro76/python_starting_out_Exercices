# This program allows users to enter their full names and after the program displays the names alphabetically
name1=input('Please, enter your full name (last name first):')
name2 = input('Please, enter your full name (last name first):')

# Print the names alphabetically

if name1 < name2:
    print("Names listed alphabetically:")
    print(name1)
    print(name2)
else:
    print("Names listed alphabetically:")
    print(name2)
    print(name1)
   
