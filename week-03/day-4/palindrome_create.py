# output = create_palindrome('pear')
# print(output) # it prints: pearraep

def create_palindrome(text_input):
    reversed_text = ''
    for i in range(len(text_input)-1, -1, -1):
        reversed_text += text_input[i]
    return(text_input + reversed_text)

print(create_palindrome('Atya'))
