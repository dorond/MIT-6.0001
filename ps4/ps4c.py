# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        mapping_dict = {}

        count = 0
        for letter in VOWELS_LOWER:
            mapping_dict[letter] = vowels_permutation[count].lower()
            count += 1

        count = 0
        for letter in VOWELS_UPPER:
            mapping_dict[letter] = vowels_permutation[count].upper()
            count += 1
        
        for letter in CONSONANTS_LOWER + CONSONANTS_UPPER:
            mapping_dict[letter] = letter
        
        return mapping_dict
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''  

        encrypted_message = ""
        for letter in self.message_text:
            if letter not in string.ascii_lowercase and letter not in string.ascii_uppercase:
                encrypted_message = encrypted_message + letter
            else:
                encrypted_message = encrypted_message + transpose_dict[letter]
        
        return encrypted_message

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #For each vowel set in the vowel permutations
            #For each word in message
                #Decrypt using an instance of the vowel permutation
                #Check if valid word
                    #If valid, add word to number of valid words for this vowel permutation. Stored in ("aieuo", ["word1", "word2"])

        #if empty tuple, return original message
        #else see which vowel permutation has most words and return a string version of that.  


        permutation_list = get_permutations(VOWELS_LOWER)
        valid_word_count = 0
        original_message = ""
        possible_original_messages = {} 
        

        for vowel_set in permutation_list:
            valid_word_count = 0
            perm_dict = self.build_transpose_dict(vowel_set)
            possible_message = self.apply_transpose(perm_dict)
            
            possible_original_messages[vowel_set] = {}            

            for word in possible_message.split():
                if is_word(self.get_valid_words(), word):
                    valid_word_count += 1               
                possible_original_messages[vowel_set][valid_word_count] = possible_message

        max_valid_words = 0
        original_message = ""
        best_vowel_set = ""

        for (vowel_set, count_message_dict) in possible_original_messages.items():
             
             for value in count_message_dict:            
                count = value
             if count > 1:
                 if count > max_valid_words:
                    max_valid_words = count
                    best_vowel_set = vowel_set
                    original_message = possible_original_messages[best_vowel_set][count] 

        if max_valid_words == 0:
            return self.message_text
        else:
            return original_message          

        

if __name__ == '__main__':

    # Example test case
    # message = SubMessage("Hello World!")
    # permutation = "eaiuo"
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "Hallu Wurld!")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    # print("Decrypted message:", enc_message.decrypt_message())

    print()

    message = SubMessage("Let's go to the park for some coffee!")
    permutation = "uaeio"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Lat's gi ti tha purk fir sima ciffaa!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())


     
    #TODO: WRITE YOUR TEST CASES HERE
