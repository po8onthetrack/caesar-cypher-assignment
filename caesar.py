def caesar_cypher(word,number):
    ''' this function shifts each letter in the plaintext by a fixed number of positions down or up the alphabet
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
        checker = alpha_index+number
        if checker > 25 or checker < -26:
            checker  = checker%26
        new_alpha = alpha[checker]
        result += new_alpha
    return result
word_number = input().split(', ')
number = int(word_number[1])
word = word_number[0]
print(caesar_cypher(word,number))
