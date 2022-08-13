from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/landing/')
def landing():
    return render_template("landing.html")


@app.route('/signup/', methods= ["POST", "GET"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password = request.form.get("password")

        print(f'username is "{user_name}", passsword is "{password}", email is {email}')
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


if __name__ == '__main__':
    app.run()