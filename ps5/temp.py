phrase = "purple cow"

def in_phrase_in(text):
        # PURPLE COW
        # The purple cow is soft and cuddly.
        # The farmer owns a really PURPLE cow.
        # Purple!!! Cow!!!
        # purple@#$%cow
        # Did you see a purple          cow?

        # text = str.lower(text)
        # if phrase in text:
        #     return True

        phrase_in_text = {}
        word_index = 0
        for word in phrase.split():
            if word in text:
                phrase_in_text[word] = phrase_in_text.get(word,list()) + [(word_index, len(word))]
            word_index += 1
        
        print()
        

            
print(in_phrase_in("Did you see a purple cow?"))
