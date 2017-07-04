from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_signup.html', title='Sign-up')

@app.route("/signup")
def welcom():
    return render_template('welcome.html', title='Welcome')


app.run()