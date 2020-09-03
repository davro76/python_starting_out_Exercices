# Enter the three test score and assigne the high score to a variable
test_score1 = int(input('Enter the test score one:'))
test_score2 = int(input('Enter the test score two:'))
test_score3 = int(input('Enter the test score three:'))
high_score = 95

# Calculate the average test score
average = (test_score1 + test_score2 + test_score3) /3

# Display the average
print('The average test score is:', format(average, '.2f'))

# Gongratulate student with an average greater than high score
if average >= high_score:
   print("Congratulation! You have a good score.")





