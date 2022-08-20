from database_control import *
from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)


# Defining temporary session dictionary.
sess = {
    'user_name' : '',
    'password' : '',
    'user_id' : ''
}

@app.route('/landing/')
def landing():
    return render_template("landing.html")


@app.route('/signup/', methods= ["POST", "GET"])
def signUp():
    if request.method == "GET":
        return render_template("signUp.html")
    else:
        # Collecting new users data
        user_name = request.form.get("user_name")
        password = request.form.get("password")
        email = request.form.get("email")
        # Instantiating UserTable class
        User = UserTable(user_name, password, email)
        # Inserting new user to database(User Table).
        User.insert_user()
        return redirect(url_for("signIn"))



@app.route('/signin/', methods= ["POST", "GET"])
def signIn():
    if request.method == "GET":
        return render_template("signIn.html")

    else:
        user_name = request.form.get("username")
        password = request.form.get("password")

        # Check if the user exists in the data base. redorects to main page if existing,
        # Else, redirects to signIn page
        if UserTable(user_name, password).user_exists() == True:
            # Instantiating UserTable class
            Users = UserTable(user_name, password)
            # Generating user id to be stored in session.
            user_id = Users.get_id()
            # Instantiating ContactTable class
            Contact = ContactTable(user_id)

            # Storing user log-in details into session.
            sess["user_name"] = user_name
            sess["password"] = password
            sess["user_id"] = user_id
            return redirect(url_for("mainPage"))
        else:
            return redirect(url_for("signIn"))


@app.route('/mainpage/', methods= ["POST", "GET"])
def mainPage():
    if request.method == 'GET':
        user_name = sess.get('user_name').title()
        return render_template("mainPage.html", user_name = user_name)
    else:
        user_name = sess.get('user_name').title()
        contacts = ContactTable()
        # contact_list = 
        return render_template("mainPage.html", user_name = user_name)

if __name__ == '__main__':
    app.run(debug= True)