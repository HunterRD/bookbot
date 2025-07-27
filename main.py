from stats import count_words
from stats import count_characters

def get_book_text (book_file):
    with open(book_file) as file:   
        book_text = file.read()
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{count_words(book_text)} words found in the document")
    print(count_characters(book_text))

main()