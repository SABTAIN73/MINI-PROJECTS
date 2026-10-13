import random


# ask the user which difficulty they want
def choose_level():
    print("Pick a level:")
    print("1 - Easy (1 to 50)")
    print("2 - Medium (1 to 100)")
    print("3 - Hard (1 to 500)")

    # keep asking until they give a valid answer
    while True:
        pick = input("Enter 1, 2 or 3: ")
        if pick == "1":
            return 50
        elif pick == "2":
            return 100
        elif pick == "3":
            return 500
        else:
            print("That's not a valid option, try again.")


# get a valid guess from the user
def get_number(low, high):
    while True:
        try:
            num = int(input(f"Your guess ({low}-{high}): "))
        except ValueError:
            # they typed something that isn't a number
            print("That's not a number, try again.")
            continue

        # make sure it's actually in range
        if num < low or num > high:
            print(f"Stay between {low} and {high} please.")
            continue

        return num


# the main game
def play():
    print("Welcome to the number guessing game!")

    high = choose_level()
    low = 1
    secret = random.randint(low, high)  # the number to guess
    attempts = 0

    print(f"\nI picked a number between {low} and {high}. Try to guess it!")

    while True:
        guess = get_number(low, high)
        attempts += 1

        # correct guess, stop the loop
        if guess == secret:
            break

        # give a hint if they're really close
        diff = abs(guess - secret)
        if diff <= 5:
            print("You're super close!")

        # tell them which way to go
        if guess > secret:
            print("Go lower.")
        else:
            print("Go higher.")

    print(f"\nNice! The number was {secret}.")
    print(f"You got it in {attempts} tries.")

    # just for fun, rate how they did
    if attempts <= 3:
        print("That was really good.")
    elif attempts <= 6:
        print("Not bad at all.")
    else:
        print("Well, you got there eventually!")


# run the game and ask if they want to play again
def main():
    while True:
        play()
        again = input("\nWanna play again? (y/n): ").lower()
        if again != "y":
            print("Alright, see ya!")
            break
        print()  # blank line before next round


# only start the game if this file is run directly
if __name__ == "__main__":
    main()