from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def home():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)

users = {}


@app.route('/', methods=['GET', 'POST'])
@app.route('/main', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check login
        if username in users and users[username]["password"] == password:
            firstname = users[username]["firstname"]
            return f"Welcome, {firstname}!"
        else:
            return "Invalid login. Try again."

    return render_template("home.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['firstname']
        username = request.form['username']
        password = request.form['password']

        # Save new user
        users[username] = {
            "firstname": firstname,
            "password": password
        }

        return redirect(url_for('home'))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
