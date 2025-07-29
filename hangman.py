import tkinter as tk
from tkinter import ttk
from words import get_word_by_difficulty

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#f2f2f2")

        self.word = ""
        self.hint = ""
        self.guessed_letters = []
        self.display_word = []
        self.lives = 6

        # Difficulty dropdown
        self.difficulty_var = tk.StringVar(value="Easy")
        self.dropdown = ttk.Combobox(root, textvariable=self.difficulty_var, values=["Easy", "Medium", "Hard"])
        self.dropdown.pack(pady=10)

        # Hint label
        self.hint_label = tk.Label(root, text="Hint will appear here", bg="#f2f2f2", fg="#d35400", font=("Arial", 12))
        self.hint_label.pack(pady=5)

        # Word display
        self.word_label = tk.Label(root, text="_ _ _ _", bg="#f2f2f2", fg="#333333", font=("Arial", 24))
        self.word_label.pack(pady=10)

        # Entry box
        self.entry = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess)

        # Guess button
        self.guess_button = tk.Button(root, text="Guess", bg="#4a90e2", fg="white", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(pady=10)

        # Message label
        self.message_label = tk.Label(root, text="", bg="#f2f2f2", fg="#2c3e50", font=("Arial", 12))
        self.message_label.pack(pady=5)

        # Reset button
        self.reset_button = tk.Button(root, text="🔁 Play Again", bg="#27ae60", fg="white", font=("Arial", 12), command=self.start_game)
        self.reset_button.pack(pady=10)

        self.start_game()

    def start_game(self, event=None):
        difficulty = self.difficulty_var.get()
        self.word, self.hint = get_word_by_difficulty(difficulty)
        self.guessed_letters = []
        self.display_word = ["_" for _ in self.word]
        self.lives = 6
        self.update_display()
        self.message_label.config(text="")
        self.hint_label.config(text=f"💡 Hint: {self.hint}")
        self.entry.config(state="normal")

    def update_display(self):
        self.word_label.config(text=" ".join(self.display_word))

    def check_guess(self, event=None):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            self.message_label.config(text="❗ Enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.config(text="⚠️ Already guessed.")
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display_word[i] = guess
            self.message_label.config(text="✅ Correct!")
        else:
            self.lives -= 1
            self.message_label.config(text=f"❌ Wrong! Lives left: {self.lives}")

        self.update_display()

        if "_" not in self.display_word:
            self.message_label.config(text=f"🎉 You won! The word was: {self.word}")
            self.entry.config(state="disabled")
        elif self.lives == 0:
            self.word_label.config(text=" ".join(list(self.word)))
            self.message_label.config(text=f"💀 You lost! The word was: {self.word}")
            self.entry.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
