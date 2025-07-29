import random

word_categories = {
    "Easy": {
        "Used for reading": "book",
        "A yellow fruit": "banana",
        "Keeps the doctor away": "apple"
    },
    "Medium": {
        "King of the jungle": "lion",
        "Tallest animal": "giraffe",
        "Panda's favorite food": "bamboo"
    },
    "Hard": {
        "Capital of France": "paris",
        "Largest continent": "asia",
        "Programming snake": "python"
    }
}

def get_word_by_difficulty(difficulty):
    hints = list(word_categories[difficulty].keys())
    hint = random.choice(hints)
    return word_categories[difficulty][hint], hint
