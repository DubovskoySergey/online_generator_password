from flask import Flask, request, render_template, send_from_directory
from flask_script import Manager
import string
import random
import os

app = Flask(__name__)
manager = Manager(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['post', 'get'])
def index():
    pass_list = ''
    if request.method == 'POST':
        num = request.form.get('num')
        special_char = request.form.get('special_char')
        len_num = request.form.get('len_num')
        if len_num.isdigit() != True:
            error = "Для создания пароля нужно указать целое число."
            return render_template('index.html', error=error)
        pass_list = gen_pass(num, special_char, len_num)
    return render_template('index.html', passwords=pass_list, )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico')

def gen_pass(num=False, special_char=False, len_num=8):
    if bool(num) == False and bool(special_char) == False:
        LETTERSYMB = string.ascii_letters
        passwords = []
        password = ''
        for i in range(10):
            password = ''
            for i in range(int(len_num)):
                pas_symb = random.choice(LETTERSYMB)
                password += pas_symb
            passwords.append(password)
        return passwords
    elif bool(num) == True and bool(special_char) == False:
        LETTERSYMB = string.ascii_letters
        NUMSYMB = string.digits
        passwords = []
        password = ''
        for i in range(10):
            password = ''
            for i in range(int(len_num)):
                pas_symb = random.choice(LETTERSYMB + NUMSYMB)
                password += pas_symb
            passwords.append(password)
        return passwords
    else:
        LETTERSYMB = string.ascii_letters
        NUMSYMB = string.digits
        CHARSSYMB = '%*()?@#$~'
        passwords = []
        password = ''
        for i in range(10):
            password = ''
            for i in range(int(len_num)):
                pas_symb = random.choice(LETTERSYMB + NUMSYMB + CHARSSYMB)
                password += pas_symb
            passwords.append(password)
        return passwords

if __name__ == "__main__":
    manager.run()
