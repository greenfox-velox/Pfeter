# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['og go', ' dad ', 'd d', 'dood', 'eve']
def reverse_text(text_input):
    reversed_text = ''
    for i in range(len(text_input)-1, -1, -1):
        reversed_text += text_input[i]
    return(reversed_text)

def search_palindromes(input_full_text):
    palindromes = []
    for first_letter_position in range( 0, len(input_full_text)):
        possible_palindrome = ''
        first_letter = input_full_text[first_letter_position]
        for second_letter_position in range(first_letter_position, len(input_full_text)):
            second_letter = input_full_text[second_letter_position]
            if (first_letter == second_letter) and (second_letter_position > first_letter_position + 1):
                possible_palindrome = input_full_text[first_letter_position: second_letter_position + 1]
                if reverse_text(possible_palindrome) == possible_palindrome:
                    palindromes += [possible_palindrome]
    return(palindromes)
print(search_palindromes('dog goat dad duck doodle never indulagorogaludni'))
