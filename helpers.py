def is_blank(form_input):
    if form_input == '':
        return True

def check_length(form_input):
    if len(form_input) not in range(3, 20):
        return True

def find_space(form_input):
    if ' ' in form_input:
        return True