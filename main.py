from pyscript import display, document


def make_account(e):
    document.getElementById('output').innerHTML = ''

    naming = document.getElementById('usenaem').innerHTML = ''

    if not naming.isalpha():
        if naming.isdigit():
            display(f'Username invalid, please add letters', target='output')
    elif naming.isalpha:
        display(f'Username invalid, please add numbers', target='output')
    else:
        display(f'Username valid', target='output')


def make_account(e):
    document.getElementById('output').innerHTML = ''

    wordpass = document.getElementById('passing').innerHTML = ''

    if not wordpass.isdigit():
        if wordpass.isalpha():
            display(f'Invalid password, must contain numbers', target='output')
    elif wordpass.isdigit:
        display(f'Invalid password, must contain letters', target='output')
    else:
        display(f'Password valid', target='output')