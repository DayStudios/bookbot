from stats import get_num_words, get_char_number, sort_characters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_chars = get_char_number(book)
    print("--------- Character Count -------")
    sorted_dict = sort_characters(num_chars)
    print("============= END ===============")

main()