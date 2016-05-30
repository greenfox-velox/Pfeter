import string

def anagramm(string_1, string_2):
    string_1 = str(string_1)
    string_2 = str(string_2)
    return sorted(list(string_1.lower())) == sorted(list(string_2.lower()))

def count_letters(string_input):
    string_letters_dictionary = {}
    for i in sorted(list(string_input.lower())):
        if i.isalpha():
            string_letters_dictionary.update({i: sorted(list(string_input.lower())).count(i)})
    return string_letters_dictionary
