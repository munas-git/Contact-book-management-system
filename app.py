from database_control import *
from flask import Flask, render_template, request, redirect, url_for


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
        # Checking if user details already exist.
        if UserTable(user_name, password).user_exists() == True:
            message = 'access-denied'
            return render_template("signUp.html", message = message)
        else:
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
            Contacts = ContactTableSetUp(user_id)
            all_contacts = Contacts.return_all_contacts(table_name)
            sess["user_contacts"] = all_contacts

            return redirect(url_for("mainPage"))
        else:
            return redirect(url_for("signIn"))


@app.route('/mainpage/', methods= ["POST", "GET"])
def mainPage():
    if request.method == 'GET':

        # End-points to be returned to main page.
        user_name = sess.get('user_name').title()
        contacts = sess["user_contacts"]
        contacts_amount = len(sess.get("user_contacts"))

        return render_template("mainPage.html", user_name = user_name, contacts_amount = contacts_amount, user_contacts = contacts)
    else:
        # Getting new-contact details from modal.
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        address = request.form.get("address")
        organization = request.form.get("organization")
        number = request.form.get("phone_number")
        email = request.form.get("email")
        social_handle = request.form.get("social_handle")
        category = request.form.get("category")
        update_contact = request.form.get("update_contact")
        contact_id = request.form.get("saved_contact_id")

        # User ID from session data.
        user_id = sess.get("user_id")

        # Contact table id generation
        table_id = 'user_'+str(sess["user_id"])+'_contacts'

        # Instantiating ContactTable and ContactTableManipulation classes.
        ContactSetUp = ContactTableSetUp(user_id, first_name, last_name, address, organization, number, email, social_handle, category)
        # ContactManipulation = ContactTableManipulation(table_id,)


        # Handling different contact CRUD operations.....
        if update_contact == "Add Contact":
            # Inserting contact into table.
            ContactSetUp.insert_contact()
        # elif update_contact == "Update Contact":
            # ContactManipulation.update_contact()

        
        # Updating sessions contact-list data.
        table_name = sess["table_name"]
        user_contacts = ContactSetUp.return_all_contacts(table_name)
        sess["user_contacts"] = user_contacts
        
        # End-points to be returned to main page.
        user_name = sess.get('user_name').title()
        contacts = sess["user_contacts"]
        contacts_amount = len(contacts)


        return render_template("mainPage.html", user_name = user_name, user_contacts = contacts, contacts_amount = contacts_amount)


if __name__ == '__main__':
    app.run(debug= True)