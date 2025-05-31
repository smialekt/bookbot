def count_words(book_content) -> int: 
  words = book_content.split()
  return len(words), words

def count_characters(words) -> dict: 
  char_dict = {}

  for word in words: 
    for char in word: 
      char = char.lower()
      if char in char_dict: 
        char_dict[char] += 1
      else: 
        char_dict[char] = 1
      
  return char_dict

def prepare_char_data(char_dict) -> list:
  char_dict_list = []
  for char in char_dict:
    if char.isalpha():
      char_dict_list.append({"char": char, "num": char_dict[char]})

  char_dict_list.sort(reverse=True ,key=lambda dict : dict["num"])
  return char_dict_list