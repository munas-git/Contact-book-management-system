from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/signin/', methods= ["POST", "GET"])
def home():

    if request.method == "GET":
        return render_template("signin.html")

    else:
        user_name = request.form.get("username")
        password = request.form.get("password")
        print("User name is: ",user_name)
        print("Password is: ", password)
        return f"Thank you, '{user_name}', your login was succesful."


if __name__ == '__main__':
    app.run()