# find huffman code for string characters
# Example : word = "zero"
# input : word
# output :{"z":1, "e":1, "r":1, "o":1}


def get_code(input_word):
    code  = {}
    for char in input_word:
        if  code.get(char, None) is not None:
            code[char]=code[char]+1
        else:
            code[char]=1
    return code

