from words import get_random_word

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""", """
     +---+
     O   |
         |
         |
        ===""", """
     +---+
     O   |
     |   |
         |
        ===""", """
     +---+
     O   |
    /|   |
         |
        ===""", """
     +---+
     O   |
    /|\\  |
         |
        ===""", """
     +---+
     O   |
    /|\\  |
    /    |
        ===""", """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def display_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    word, category = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_guesses = len(HANGMAN_PICS) - 1

    print("🎮 Welcome to Hangman!")
    print(f"💡 Hint: It's from the category '{category}'.")

    while wrong_guesses < max_guesses:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word: ", display_progress(word, guessed_letters))
        guess = input("🔤 Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
        elif guess in word:
            print("✅ Correct!")
            guessed_letters.add(guess)
        else:
            print("❌ Wrong!")
            wrong_guesses += 1
            guessed_letters.add(guess)

        if set(word).issubset(guessed_letters):
            print(f"\n🎉 You won! The word was: {word}")
            break
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"\n💀 You lost! The word was: {word}")

if __name__ == "__main__":
    play_game()
