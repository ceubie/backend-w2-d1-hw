# 2. Loop Condition Logic

# Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.

#---------------------------------------------------------------------
# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).


basketball = True

while basketball:
    athlete = input("Do you want to keep playing baksetball? (yes or no)  ")
    if athlete == "no":
        break
    

#---------------------------------------------------------------------

# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)

x = 0

while x <= 4:
    print('The number is less than 5', 'iteration', x)
    x += 1

#---------------------------------------------------------------------