def get_hint(secret, guess):
    """Provides hints by revealing which digits in the guess are correct."""
    hint = []
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint.append(guess[i])
        else:
            hint.append('*')
    return ''.join(hint)

def play_game(secret, max_attempts=10):
    """Main function to play the Mastermind game."""
    attempts = 0
    while attempts < max_attempts:
        guess = input("Enter your guess: ")
        if len(guess) != len(secret):
            print(f"Please enter a {len(secret)}-digit number.")
            continue
        if guess == secret:
            print("Correct! You've guessed the number.")
            return attempts + 1
        else:
            hint = get_hint(secret, guess)
            print(f"Hint: {hint}")
        attempts += 1
    print("You've exceeded the maximum number of attempts!")
    return attempts

def main():
    print("Welcome to Mastermind!")
    max_attempts = 10
    
    # Player 1 sets a number for Player 2 to guess
    secret_number_1 = input("Player 1, enter the secret number: ")
    print("\n" * 50)  # Clear the screen
    print("Player 2, try to guess the number set by Player 1.")
    attempts_player_2 = play_game(secret_number_1, max_attempts)
    
    # Player 2 sets a number for Player 1 to guess
    secret_number_2 = input("Player 2, enter the secret number: ")
    print("\n" * 50)  # Clear the screen
    print("Player 1, try to guess the number set by Player 2.")
    attempts_player_1 = play_game(secret_number_2, max_attempts)
    
    # Determine the winner
    if attempts_player_1 < attempts_player_2:
        print("Player 1 wins the game and is crowned Mastermind!")
    elif attempts_player_2 < attempts_player_1:
        print("Player 2 wins the game and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
