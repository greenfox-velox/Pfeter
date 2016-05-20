# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['og go', ' dad ', 'd d', 'dood', 'eve']

def search_palindromes(full_txt):
    palindromes = []
    for first_pos in range( 0, len(full_txt)):
        possible_palindrome = ''
        first_letter = full_txt[first_pos]
        for second_pos in range(first_pos, len(full_txt)):
            second_letter = full_txt[second_pos]
            if (first_letter == second_letter) and (second_pos > first_pos + 1):
                if full_txt[first_pos: second_pos + 1] == full_txt[second_pos: first_pos - 1: - 1]:
                    palindromes += [full_txt[first_pos: second_pos + 1]]
    return(palindromes)
print(search_palindromes('dog goat dad duck doodle never'))
