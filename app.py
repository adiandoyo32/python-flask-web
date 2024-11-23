from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '1a2b3c4d5e6d7g8h9i10'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mikrodeploy'
 
mysql = MySQL(app)

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
      username = request.form['username']
      print (username)
      password = request.form['password']
      print (password)
      # Check if account exists using MySQL
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
      # Fetch one record and return result
      account = cursor.fetchone()
            # If account exists in accounts table in out database
      print (account)
      if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('index'))
      else:
            # Account doesnt exist or username/password incorrect
            flash("Incorrect username/password!", "danger")
    return render_template('login.html',title="Login")
      # if (username == 'admin' and password == 'admin'):
      #   msg = 'Logged in successfully !'
      #   return redirect(url_for('index', msg = msg))
      # else:
      #   msg = 'Incorrect username / password !'
    # return render_template('login.html', msg = msg)

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
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM user''')
    data = cur.fetchall()
    print (data)
    return "halaman nama"

if __name__ == '__main__':
    app.run(debug=True)