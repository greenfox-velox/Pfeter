# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    simple_texts = ''
    for line in reversed(f.readlines()):
        simple_text = ''
        for i in range(0, len(line.rstrip())):
            simple_text += line.rstrip()[i]
        simple_texts += simple_text + '\n'
    f.close()
    return simple_texts
