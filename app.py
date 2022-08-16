from database import *
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/landing/')
def landing():
    return render_template("landing.html")


@app.route('/signup/', methods= ["POST", "GET"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        # Collecting new users data
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Instantiating UserTable class
        database = UserTable(user_name, email, password)
        # Inserting new user to database(User Table).
        database.insert_user()

        return redirect(url_for('signin'))



@app.route('/signin/', methods= ["POST", "GET"])
def signin():

    if request.method == "GET":
        return render_template("signin.html")

    else:
        user_name = request.form.get("username")
        password = request.form.get("password")
        print("User name is: ",user_name)
        print("Password is: ", password)
        return (f"Thank you, '{user_name}', your login was succesful.")


data =[
    { 
        'id': 1,
        'name': 'Einstein',
        'email': 'einsteinmunachiso@gmail.com',
        'contact_list':
        [
            {'name': 'moyo','phone_num': int('08148352787'),'category': 'friend'},
            {'name': 'james','phone_num': int('08146593631'),'category': 'friend'},
            {'name': 'mama ♥','phone_num': int('08036578298'),'category': 'family'},
            {'name': 'dad 😎','phone_num': int('07046274983'),'category': 'family'},
            {'name': 'timilein','phone_num': int('090937462'),'category': 'friend'},
        ],
    }
]


@app.route('/api')
def api():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug= True)