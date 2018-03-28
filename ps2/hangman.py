# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # s = ""
    # letters = s.join(letters_guessed)
    # return secret_word in letters 
    count = 0
    for letter in secret_word:
      if letter in letters_guessed:
        count += 1
    
    return count == len(secret_word)

    # pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word=""

    for letter in secret_word:
      if letter in letters_guessed:
        guessed_word = guessed_word + letter
      else:
        guessed_word = guessed_word + "_ "
    
    return guessed_word
    #pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available = ""

    for letter in alphabet:
      if letter not in letters_guessed:
        available = available + letter
        
    return available
    #pass
    
def show_header(secret_word, num_warnings):
  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is", len(secret_word), "letters long")
  print("You have", num_warnings ,"warnings left.")
  print("-----------")

def validate_input(guess, secret_word, letters_guessed):
  error = ""
  if guess not in string.ascii_letters:
    error = "Oops! That is not a valid letter."
    return (False, error)
  elif (guess in secret_word) and (guess in letters_guessed):
    error = "Oops! You've already guessed that letter."
    return (False, error)
  else:
    return (True, error) 


def is_guess_in_word(guess, secret_word):
  return guess in secret_word

def is_game_over(num_guesses, num_warnings):
  return True




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #secret_word = "peaches"

    num_guesses = 6
    num_warnings = 3
    letters_guessed = []
    game_over = False

    show_header(secret_word, num_warnings)

    while not game_over:
      print("You have", num_guesses, "guesses left")
      print("Available letters:", get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ")
      is_valid_input, error = validate_input(guess, secret_word, letters_guessed)   

      if not is_valid_input:
        num_warnings -= 1
        print(error, end= " ")
        if num_warnings > 0:
          print("You have", num_warnings, "warnings left:", end=" ")
        else:
          print("You have no warnings left so you lose one guess:", end=" ")
          num_guesses -= 1
      
      else:
        letters_guessed.append(guess)
        if is_guess_in_word(guess, secret_word):
          print("Good guess:", end =" ") 
          
        else:
          print("Oops! That letter is not in my word:", end =" ") 
          num_guesses -= 1
      
      print(get_guessed_word(secret_word, letters_guessed))
      print("-----------")

      if(is_word_guessed(secret_word, letters_guessed)):
        print("Congratulations, you won!")
        print("Your total score for this game is:", num_guesses * len(secret_word))
        game_over = True 
      
      if num_guesses == 0:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")
        game_over = True      



    #pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    stripped_word = ""
    for i in my_word:
      if i != " ":
        stripped_word = stripped_word + i
    
    if len(stripped_word) != len(other_word):
      return False
    
    index = 0
    total_matches = 0
    
   

    for letter in other_word:
      if stripped_word[index] == "_" or stripped_word[index] == letter:
        total_matches += 1
      index += 1
    return total_matches == len(other_word)
         

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Possible word matches are:")
    for word in wordlist:
      if match_with_gaps(my_word, word):
        print(word, end=" ")
        
  
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guesses = 6
    num_warnings = 3
    letters_guessed = []
    game_over = False

    show_header(secret_word, num_warnings)

    while not game_over:
      print("You have", num_guesses, "guesses left")
      print("Available letters:", get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ")
      if guess == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      else:
        is_valid_input, error = validate_input(guess, secret_word, letters_guessed)   

        if not is_valid_input:
          num_warnings -= 1
          print(error, end= " ")
          if num_warnings > 0:
            print("You have", num_warnings, "warnings left:", end=" ")
          else:
            print("You have no warnings left so you lose one guess:", end=" ")
            num_guesses -= 1
        
        else:
          letters_guessed.append(guess)
          if is_guess_in_word(guess, secret_word):
            print("Good guess:", end =" ") 
            
          else:
            print("Oops! That letter is not in my word:", end =" ") 
            num_guesses -= 1
        
        print(get_guessed_word(secret_word, letters_guessed))
      print("-----------")

      if(is_word_guessed(secret_word, letters_guessed)):
        print("Congratulations, you won!")
        print("Your total score for this game is:", num_guesses * len(secret_word))
        game_over = True 
      
      if num_guesses == 0:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")
        game_over = True      



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
