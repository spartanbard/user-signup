from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']
    user_val = ""
    pass_val = ""
    pswrd_val = ""

    def len_check(string):
        if len(string) < 3 or len(string) > 20:
            return "must be between 3 and 20 characters"

    def verify_check(pswrd, vpass):
        if pswrd != vpass:
            return "passwords do not match"

    user_val = len_check(username)
    pass_val = len_check(password)
    pswrd_val = verify_check(password, vpassword)

    return render_template('index.html', username=username, password=password, vpassword=vpassword, email=email, user_val=user_val, pass_val=pass_val, pswrd_val=pswrd_val)

@app.route("/welcome", methods=['POST'])
def welcome():
    return "Welcome"

app.run()