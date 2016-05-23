# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    simple_texts = ''
    for line in f:
        simple_text = ''
        for i in range(0, len(line), 2):
            if (i < len(line) - 1):
                simple_text += line[i]
        simple_texts += simple_text + '\n'
    f.close()
    return simple_texts
