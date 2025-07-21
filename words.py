import random

word_categories = {
    "Fruits": ["apple", "banana", "grape", "mango", "orange"],
    "Animals": ["elephant", "giraffe", "kangaroo", "lion", "penguin"],
    "Countries": ["india", "canada", "brazil", "france", "japan"]
}

def get_random_word():
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    return word, category
