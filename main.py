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
    space_val = ""
    email_val = ""

    def len_check(string):
        if len(string) < 3 or len(string) > 20:
            return " *Must be between 3 and 20 characters*"
        else:
            return ""

    def verify_check(pswrd, vpass):
        if pswrd != vpass:
            return " *Passwords do not match*"
        else:
            return ""

    def space_check(string):
        for i in string:
            if i == " ":
                return " *Cannot contain spaces*"
        return ""

    user_val = len_check(username)
    pass_val = len_check(password)
    pswrd_val = verify_check(password, vpassword)
    space_val = space_check(password)

    if len(email) > 0:
        email_val += space_check(email)
        email_val += len_check(email)
        if "@" not in email:
            email_val += """ *Contains no "@" symbol"""
        if "." not in email:
            email_val += """ *Contains no "." symbol"""

    if user_val == "" and pass_val == "" and pswrd_val == "" and space_val == "" and email_val == "":
        return render_template('welcome.html', username=username)

    return render_template('index.html', username=username, password=password, vpassword=vpassword, email=email, user_val=user_val, pass_val=pass_val, pswrd_val=pswrd_val, space_val=space_val, email_val=email_val)


app.run()