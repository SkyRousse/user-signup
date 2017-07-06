from flask import Flask, request, redirect, render_template
from helpers import is_blank, check_length, find_space
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('user_signup.html', title='Sign-up')

    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirmation = request.form['password_confirmation']

        email_error = ''
        username_error = ''
        password_error = ''
        confirmation_error = ''

        if is_blank(username) or check_length(username) or find_space(username):
            username_error = 'please enter a valid username (3 characters or longer & no spaces)'  

        if not is_blank(email):
            if "@" not in email or "." not in email or check_length(email) or find_space(email):
                email_error = 'please enter a valid email address'

        if is_blank(password):
            password_error = 'please enter a password between 3 and 20 characters'
        elif check_length(password) or find_space(password):
            password_error = "your password must be between 3 and 20 characters long with no spaces"
        elif password != password_confirmation:
            confirmation_error = "passwords don't match"

        if not email_error and not username_error and not password_error and not confirmation_error:
            return redirect('/welcome?username={username}'.format(username=username))
        else:
            return render_template('user_signup.html', 
                username=username, 
                email=email,
                email_error=email_error,
                username_error=username_error,
                password_error=password_error,
                confirmation_error=confirmation_error,
                )

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', title='Welcome', username=username)


app.run()
