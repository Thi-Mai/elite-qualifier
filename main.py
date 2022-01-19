import time


# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')
  print()

  return all_words


def suggest(text, all_words):
  text_list = list(text)
  smallest_difference = 100
  suggestions = []

  if text in all_words:
    print(text.capitalize() + ' is a word.')
    print("No suggestions. The word is spelled correctly.")
    print()
  else:
    print(text.capitalize() + ' is not a word.')
    print("Please wait for some suggestions.")

    for word in all_words:
      if text not in all_words:
        letter_list = list(word)
        non_match_list = []

        for letter in letter_list:
            if letter not in text_list:
              non_match_list.append(letter)

        for letter in text_list:
          if letter not in letter_list:
            non_match_list.append(letter)

        num_of_differences = len(non_match_list)

        if num_of_differences == smallest_difference:
          suggestions.append(word)

        if num_of_differences < smallest_difference:
          smallest_difference = num_of_differences
          suggestions.clear()
          suggestions.append(word)

    return (suggestions)
    #print()

def main_program():
    all_words = load_words()
    print('Type some text, or type \"QUIT\" to stop')
    while True:
        text = input(':> ')
        if ('QUIT' == text):
          print("Thank you for using my autocorrect!")
          break
        print(suggest(text, all_words))

if __name__ == "__main__":
    main_program()
