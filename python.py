import random

def play_guessing_game():
    guesses_made = 0

    # Hardcode the player's name
    name = "Test Player"

    # Generate a random number
    number = random.randint(1, 20)
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')

    # Hardcoded guesses
    guesses = [5, 10, 15, 3, 8, 20]  # These can be adjusted to test different scenarios

    for guess in guesses:
        guesses_made += 1

        print(f'Take a guess: {guess}')  # Outputting the guess for testing transparency

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            print(f'Good job, {name}! You guessed my number in {guesses_made} guesses!')
            break

    if guess != number:
        print(f'Nope. The number I was thinking of was {number}')

if __name__ == "__main__":
    play_guessing_game()
