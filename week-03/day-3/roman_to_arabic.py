roman_number = 'CDXXIV'

roman_numerals = [
{'name': 'I', 'value': 1},
{'name': 'V', 'value': 5},
{'name': 'X', 'value': 10},
{'name': 'L', 'value': 50},
{'name': 'C', 'value': 100},
{'name': 'D', 'value': 500},
{'name': 'M', 'value': 1000}
]

def convert(input_name):
    output_value = 0
    for input_name_i in roman_numerals:
        if input_name_i['name'] == input_name:
            output_value = input_name_i['value']
    return(output_value)

def roman_to_arabic(input_number):
    counter = 0
    for input_number_i in range(0, len(input_number)):
        converted_number = convert(input_number[input_number_i])
        if input_number_i == len(input_number) - 1:
            after_converted_number = converted_number
        else:
            after_converted_number = convert(input_number[input_number_i + 1])
        if converted_number < after_converted_number:
            counter -= converted_number
        else:
            counter += converted_number
    return(counter)

print(roman_to_arabic(roman_number))
