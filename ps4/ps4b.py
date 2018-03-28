# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert 0 <= shift < 26
                
        shift_dict = {}       

        count = 0
        for letter in string.ascii_lowercase:
            new_letter_number = shift - (26 - count)
            shift_dict[letter] = string.ascii_lowercase[new_letter_number]
            count += 1
        
        count = 0
        for letter in string.ascii_uppercase:
            new_letter_number = shift - (26 - count)
            shift_dict[letter] = string.ascii_uppercase[new_letter_number]
            count += 1  
        
        return shift_dict          

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        assert 0 <= shift < 26
        
        shifted_message = ""
        shift_dict = self.build_shift_dict(shift)

        for letter in self.message_text:
            shifted_message += shift_dict.get(letter, letter)   #Apply the matching letter from dictionary, otherwise apply spaces/punctuations without change

        return shifted_message 

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)       


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert 0 <= shift < 26

        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift) 


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        #For each shift from 1 to 26
        #   For each word in message
            #   Create a new word using this shift value
            #   Check that word is a valid word
            #   If valid
            #       Add word to a dictionary indexed by shift.  dict: int > list[string]
                   

        #Go through dictionary and which shift key has the most valid valuees
        #Return in tuple. tuple (int, string)
        
        shift_validwords_dict = {}
        

        for shift in range(0, 26):
            for word in self.apply_shift(shift).split():                
                if is_word(self.valid_words, word):
                    temp_list = shift_validwords_dict.get(shift, list())
                    temp_list.append(word)
                    shift_validwords_dict[shift] = temp_list
                    
        total_valid_words = 0
        best_shift = None
        for shift in shift_validwords_dict:
           if len(shift_validwords_dict[shift]) > total_valid_words:
               best_shift = shift
               total_valid_words = len(shift_validwords_dict[shift])
        
        decoded_message = ""
        if len(shift_validwords_dict) != 0:
            for word in shift_validwords_dict[best_shift]:
                decoded_message = decoded_message + " " + word
            return (best_shift, decoded_message)
        else:
            return (None, "")
        #plaintext_letter = self.message_text[0] + 26 - shift
        

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print()
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())

    # ciphertext = CiphertextMessage('Lipps, Asvph!')
    # print()
    # print('Expected Output:', (22, 'Hello, World!'))
    # print('Actual Output:', ciphertext.decrypt_message())

    # ciphertext = CiphertextMessage('cdefgh')
    # print()
    # print('Expected Output:', (None, ''))
    # print('Actual Output:', ciphertext.decrypt_message())

    

    #TODO: WRITE YOUR TEST CASES HERE

    plaintext = PlaintextMessage('My name is Doron. My favorite sport is rugby!', 6)
    print('Expected Output: Se tgsk oy Juxut. Se lgbuxozk yvuxz oy xamhe!')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage('Se tgsk oy Juxut. Se lgbuxozk yvuxz oy xamhe!')
    print()
    print('Expected Output:', (20, 'My name is. My favorite sport is rugby!'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: best shift value and unencrypted story 

    ciphertext = CiphertextMessage(get_story_string())
    print()
    print('Expected Output:', (12, 'Jack is a mythical character created on the spur of a moment to help cover an planned hack. He has been registered for classes at twice before, but has reportedly never passed It has been the tradition of the residents of East Campus to become Jack for a few nights year to educate incoming students in the ways, means, and ethics of hacking.'))
    print('Actual Output:', ciphertext.decrypt_message())

    
    pass #delete this line and replace with your code here
