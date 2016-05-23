# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    simple_texts = ''
    for line in (f.readlines()):
        simple_text = ''
        for i in range(0, len(line.rstrip())):
            if line.rstrip()[i] == ' ':
                simple_text += ' '
            else:
                simple_text += chr(ord(line.rstrip()[i])-1)
        simple_texts += simple_text + '\n'
    f.close()
    return simple_texts
