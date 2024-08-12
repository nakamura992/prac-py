words = ["apple", "banana", "orange"]

def print_text(words, func):
    for word in words:
        print(func(word))
print_text(words, lambda word: word.upper())

