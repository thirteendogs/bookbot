def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        book_words = get_book_words(file_contents)
        num_words_in_book(book_words)
        count_characters(book_words)

def get_book_words(book):
    return book.split()
        
def num_words_in_book(book_words):
    print(len(book_words))

def count_characters(book_words):
    characters_count = {}
    book_charaters = ''.join(book_words).lower()

    for char in book_charaters:
        if char not in characters_count:
            characters_count[char] = 1
        else:
            characters_count[char] +=1
    print(characters_count)

main()










