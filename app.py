from database_control import *
from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)


# Defining temporary session dictionary.
sess = {
    "user_name" : "",
    "password" : "",
    "user_id" : "",
    "user_contacts" : "",
    'test' : [1,2,3,4,5]
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
            Users = UserTable(user_name, password, 'nil')
            # Generating user id to be stored in session.
            user_id = Users.get_id()
            # Storing user session details.
            sess["user_name"] = user_name
            sess["password"] = password
            sess["user_id"] = user_id
            # Instantiating ContactTable and returning all existing user contacts
            Contacts = ContactTable(user_id)
            all_contacts = Contacts.return_all_contacts()
            sess["user_contacts"] = all_contacts
            return redirect(url_for("mainPage"))
        else:
            return redirect(url_for("signIn"))


@app.route('/mainpage/', methods= ["POST", "GET"])
def mainPage():
    if request.method == 'GET':

        # Data to be returned to main page
        user_name = sess.get('user_name').title()
        user_contacts = sess["user_contacts"]
        user_contacts = jsonify(user_contacts)

        return render_template("mainPage.html", user_name = user_name)
    else:
        # Getting new-contact details from modal.
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        number = request.form.get("phone_number")
        email = request.form.get("email")
        category = request.form.get("category")

        # User ID from session data.
        user_id = int(sess.get("user_id"))

        # Instantiating ContactTable.
        Contacts = ContactTable(user_id, first_name, last_name, number, category, email)

        # Inserting contact into table.
        Contacts.insert_contact()

        # Updating sessions contact list.
        user_contacts = Contacts.return_all_contacts()
        sess["user_contacts"] = user_contacts
        
        # Data to be returned to main page
        user_name = sess.get('user_name').title()
        user_contacts = sess["user_contacts"]
        user_contacts = jsonify(user_contacts)


        return render_template("mainPage.html", user_name = user_name)


if __name__ == '__main__':
    app.run(debug= True)