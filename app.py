from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
      username = request.form['username']
      password = request.form['password']
      if (username == 'admin' and password == 'admin'):
        msg = 'Logged in successfully !'
        return redirect(url_for('index', msg = msg))
      else:
        msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    myFunction(processed_text)
    return processed_text
  
def myFunction(value):
  print('this is my value')
  print(value)

@app.route('/nama')
def nama():
    return "halaman nama"

if __name__ == '__main__':
    app.run(debug=True)