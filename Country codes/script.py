import json

code_file = open('codes.json', 'r')
codes = json.load(code_file)
code_file.close()

def format_code_string(s):
    """ Formats the code string for the get_country_from_code()"""
    n_string = "0123456789"
    new_string = []
    for char in s:
        if char in n_string:
            new_string.append(char)
    return ''.join(new_string)

def get_country_from_code(s):
    """ Returns the name of the country for the dialcode given """
    code = format_code_string(s)
    if codes[code]:
        return codes[code]
    else:
        return None
        