def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()  # Normalize to lowercase for character count
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters