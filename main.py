def main():
    print(f"--- Starting the report for {book} ---")
    with open(book) as f:
        file_contents = f.read()
        book_words = get_book_words(file_contents)
        num_words_in_book = get_num_words_in_book(book_words)
        print(f"This book has {num_words_in_book} words!")
        count_characters_dict = get_count_characters_dict(book_words)
        sort_characters_dict(count_characters_dict)

def get_book_words(book):
    return book.split()
        
def get_num_words_in_book(book_words):
    return len(book_words)

def get_count_characters_dict(book_words):
    characters_count_dict = {}
    book_charaters = ''.join(book_words).lower()

    for char in book_charaters:
        if char.isalpha() == True:
            if char not in characters_count_dict:
                characters_count_dict[char] = 1
            else:
                characters_count_dict[char] +=1
    return characters_count_dict

def sort_characters_dict(characters_dict):
    characters_dict_list_keys = sorted(list(characters_dict))
    sorted_characters_dict = {}
    
    for char in characters_dict_list_keys:
        sorted_characters_dict[char] = characters_dict[char]

    return sorted_characters_dict

book = "./books/frankenstein.txt"

main()










