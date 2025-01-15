from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector as mycon

app = Flask(__name__)
app.secret_key = 'DON\'T TELL ANYONE'


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    uname = request.form.get('username')
    pword = request.form.get('password')
    try:
        global con
        con = mycon.connect(host='localhost', user=uname, password=pword)
        cur = con.cursor()
    except Exception as e:
        flash(str(e))
        return redirect(url_for('login'))
    return render_template('home.html', username=uname)

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/acct_created', methods = ['GET', 'POST'])
def signed_up():
    con = mycon.connect(host='localhost', user='root', password='carmel')
    cur = con.cursor()
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    cur.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'")
    flash('USER CREATED SUCCESSFULLY')
    return redirect(url_for('login'))
app.run()

