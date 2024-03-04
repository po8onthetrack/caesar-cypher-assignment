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
        alpha_index = alpha.index(character)
        new_alpha = alpha[alpha_index+number]
        result += new_alpha
    return result
word_number = input().split(', ')
number = int(word_number[1])
word = word_number[0]
print(caesar_cypher(word,number))
