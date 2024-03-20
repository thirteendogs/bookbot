def num_words_in_book(book):
    num_words = len(book.split())
    print(num_words)

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words_in_book(file_contents)

main()










