import random as rand

print("***************************")
print("Welcome to the math quiz")
print("***************************")

# bookeeping scores
q_asked = 0
q_answered_correctly = 0

while q_asked < 10:

    # Generate a number to choose the operator
    operator = rand.randint(0, 4)

    # Generate a random integer between 1 and 100
    num1 = rand.randint(1, 100)

    # Increment the questions asked by 1
    q_asked += 1

    match(operator):
        case 0:

            # Generate a random integer between 1 and 100
            num2 = rand.randint(1, 100)

            # Take input from user
            user_ans = int(input(f"\n{q_asked}. {num1} + {num2} = ? :"))

            # Calculate the correct answer
            ans = num1 + num2

            # Check the answer and display the appropriate message to the user
            if ans == user_ans:
                print("Wohoo! On to the next one")
                q_answered_correctly += 1
            else:
                print("Oops! Thats not the right answer")

        case 1:
            # Generate a random integer between 1 and num1
            num2 = rand.randint(0, num1)

            # Take input from user
            user_ans = int(input(f"\n{q_asked}. {num1} - {num2} = ?: "))

            # Calculate the correct answer
            ans = num1 - num2

            # Check the answer and display the appropriate message to the user
            if ans == user_ans:
                print("Wohoo! On to the next one")
                q_answered_correctly += 1
            else:
                print("Oops! Thats not the right answer")
        case 2:
            # Generate a random integer between 1 and 10
            num2 = rand.randint(1, 10)

            # Take input from user
            user_ans = int(input(f"\n{q_asked}. {num1} x {num2} = ?: "))

            # Calculate the correct answer
            ans = num1 * num2

            # Check the answer and display the appropriate message to the user
            if ans == user_ans:
                print("Wohoo! On to the next one")
                q_answered_correctly += 1
            else:
                print("Oops! Thats not the right answer")
        case 3:
            # Generate a random number between 1 and 10
            num2 = rand.randint(1, 10)

            # Take input from the user
            user_ans = int(input(f"\n{q_asked}. Is {num1} divisible by {num2}? Enter '1' for yes and '0' for no: "))

            # if num1 is divisible by num2 then assign 1 else assign 0
            ans = 1 if num1 % num2 == 0 else 0

            # Check the answer and display the appropriate message to the user
            if ans == user_ans:
                print("Wohoo! On to the next one")
                q_answered_correctly += 1
            else:
                print("Oops! Thats not the right answer")

        case 4:
            num2 = 2

            # Generate a random number between 1 and 30
            num1 = rand.randint(1, 30)

            # Take input from user
            user_ans = int(input(f"\n{q_asked}. {num1} raised to {num2} = ? : "))

            # Calculate the correct answer
            ans = num1 ** num2

            # Check the user entered answer and display the appropriate message to the user
            if ans == user_ans:
                print("Wohoo! On to the next one")
                q_answered_correctly += 1
            else:
                print("Oops! Thats not the right answer")

    # reset the num1 to zero
    num1 = num1 // (num1 + 1)

# Print the game stats
print("\n\nGame over!")
print(f"Final score: {q_answered_correctly}/{q_asked} questions answered correctly\nPercent: {(q_answered_correctly/q_asked) * 100}%")

