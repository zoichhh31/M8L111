#Импорт
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')


#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python') 
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)

# Form feedback
@app.route('/submit', methods=['GET','POST'])
def feedback_form():
    email = request.form['email']
    text = request.form['text']
	# Kamu bisa menyimpan data atau mengirimkannya melalui email
    with open('form.txt', 'a',) as f:
        f.write(email + '\n')
        f.write(text + '\n')
