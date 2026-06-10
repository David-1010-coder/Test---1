secret_number = 42
hearts = 5

while hearts > 0:
    print(f"\nRemaining lives: {'❤️ ' * hearts}")
    guess = int(input("Enter your guess: "))
    
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
        break  # Stops the game once they win
    elif guess < secret_number:
        print("📉 Too cold! Try a higher number.")
        hearts -= 1
    else:
        print("📈 Too hot! Try a lower number.")
        hearts -= 1

if hearts == 0:
    print(f"\n❌ Game Over! You ran out of hearts. The secret number was {secret_number}.")
    