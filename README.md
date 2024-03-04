# caesar-cypher-assignment
def caesar_cypher(word,number):
    ''' this funcrion shifts each letter in the plaintext by a fixed number of positions down or up the alphabet
    arg:
        word: an string input represents the word
        number: an integer input for shifting 
    return:
        a new shifted string
    '''
    result = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for character in word:
        alpha_index = alpha.index(character)   # get the index of the character in the input from the alphabetic reference 
        new_alpha = alpha[alpha_index+number]  # get the new letter based ont integer input 
        result += new_alpha                    # get the new encrypted word
    return result                              # return result
word_number = input().split(', ')              # split the input to get the word input and the integer input
number = int(word_number[1])                   
word = word_number[0]
print(caesar_cypher(word,number))              # print the result
