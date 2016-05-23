# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    simple_texts = ''
    for line in f:
        simple_text = ''
        for i in range(len(line.rstrip()) - 1, - 1, - 1):
            simple_text += line.rstrip()[i]
        simple_texts += simple_text + '\n'
    f.close()
    return simple_texts
