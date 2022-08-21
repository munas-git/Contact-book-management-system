from database_control import *
from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)


# Defining temporary session dictionary.
sess = {
    "user_name" : "",
    "password" : "",
    "user_id" : "",
    "table_name" : "",
    "user_contacts" : "",
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
            # Generating user id and retreiving table name to be stored in session.
            user_id = Users.get_id()
            table_name = 'user_'+str(user_id)+'_contacts'

            # Storing user session details.
            sess["user_name"] = user_name
            sess["password"] = password
            sess["user_id"] = user_id
            sess["table_name"] = table_name

            # Instantiating ContactTable and returning all existing user contacts
            Contacts = ContactTable(user_id)
            all_contacts = Contacts.return_all_contacts(table_name)
            sess["user_contacts"] = all_contacts

            return redirect(url_for("mainPage"))
        else:
            return redirect(url_for("signIn"))


@app.route('/mainpage/', methods= ["POST", "GET"])
def mainPage():
    if request.method == 'GET':

        # Data to be returned to main page
        user_name = sess.get('user_name').title()
        contacts = sess["user_contacts"]
        contacts_amount = len(sess.get("user_contacts"))

        return render_template("mainPage.html", user_name = user_name, contacts_amount = contacts_amount, user_contacts = contacts)
    else:
        # Getting new-contact details from modal.
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        number = request.form.get("phone_number")
        email = request.form.get("email")
        category = request.form.get("category")

        # User ID from session data.
        user_id = sess.get("user_id")

        # Instantiating ContactTable.
        Contacts = ContactTable(user_id, first_name, last_name, number, category, email)

        # Inserting contact into table.
        Contacts.insert_contact()

        # Updating sessions contact list.
        table_name = sess["table_name"]
        user_contacts = Contacts.return_all_contacts(table_name)
        sess["user_contacts"] = user_contacts
        
        # Data to be returned to main page
        user_name = sess.get('user_name').title()
        contacts = sess["user_contacts"]
        contacts_amount = len(contacts)


        return render_template("mainPage.html", user_name = user_name, user_contacts = contacts, contacts_amount = contacts_amount)


if __name__ == '__main__':
    app.run(debug= True)