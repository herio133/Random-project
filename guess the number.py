import random 

def number_guessing_game():
    number = random.randint(1,100)
    attempts = 0
    

    while True:
        try: 
            guess = int(input("guess a number between 1 and 100; "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("too HIGH! try again")
            elif guess < number:
                print("TOO LOW! try again")
            else:
                print(f"you guessed it! the number was {number} and it took you {attempts} attempts")
                guessed_correctly = True
                break
        except ValueError:
            print("Please enter a valid integer between 1 and 100.")

number_guessing_game()
