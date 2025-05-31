import sys
from stats import *

def get_book_text(path) -> str: 
  with open(path) as f: 
    file_contents = f.read()

  return file_contents

def main():
  if len(sys.argv) < 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  words_count, words = count_words(book_text)
  char_dict = count_characters(words)
  prepared_characters = prepare_char_data(char_dict)

  # output msg
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {words_count} total words")
  print("--------- Character Count -------")
  for char_dict in prepared_characters: 
    print(f"{char_dict["char"]}: {char_dict["num"]}")

main()

