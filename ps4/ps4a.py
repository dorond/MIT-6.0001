# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #If only a single letter, return it

    #Otherwise, take the first letter of the sequence out and work out the permutations of the remaining letters. Eventually there will 
    #only be 1 letter, which will be return up the stack

    if len(sequence) == 1:
        return list(sequence[0])

    if len(sequence) == 2:
        letter1 = sequence[0]
        letter2 = sequence[1]
        return [letter1 + letter2, letter2 + letter1]

    permutations = []
    held_letter = ''    

    for letter in sequence:
        seq_list = list(sequence)
        held_letter = letter
        seq_list.remove(held_letter) 
        shorter_string = ''.join(seq_list)
        temp_permutations = get_permutations(shorter_string)
        for j in range(len(temp_permutations)):
            temp_permutations[j] = temp_permutations[j] + held_letter
            permutations.append(temp_permutations[j])
    return permutations

  

if __name__ == '__main__':
#    #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

   example_input = 'fhj'
   print('Input:', example_input)
   print('Expected Output:', ['hjf', 'jhf', 'fjh', 'jfh', 'fhj', 'hfj'])
   print('Actual Output:', get_permutations(example_input))




