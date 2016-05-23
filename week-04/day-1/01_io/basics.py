# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    lines = f.readlines()
    result = lines[number - 1].rstrip()
    f.close()
    return result

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
# solution 1:
# def words(sentence):
#     words_list = []
#     for i in range(0, len(sentence)):
#         for j in range(i+1, len(sentence)):
#             if sentence[j] == ' ' or j == len(sentence) - 1:
#                 words_list.append(sentence[i: j])
#                 i = j + 1
#         return words_list

# solution 2:
def words(sentence):
    return sentence[0: len(sentence) - 1].split(' ')

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    sentenced = words[0]
    for i in range(1, len(words)):
        sentenced += ' ' + words[i]
    sentenced += '.'
    return sentenced

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    characters = []
    for i in string:
        characters.append(ord(i))
    return characters

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    characters = ''
    for i in char_codes:
        characters += chr(i)
    return characters
