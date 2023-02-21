import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login(title="Login"):
    # YOUR SOLUTION HERE
    if request.method == 'POST':
        user_name = request.form["username"]
        password = hash_password(request.form["password"])
        
        users = get_users()
        user_password = users[user_name]
        
        if user_name in users:
            if user_password == password:
                session['user_name'] = user_name
                return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login', error=True))
    
    return render_template("login.html", title=title)

@app.route("/dashboard")
def dashboard(title="Dashboard"):
    # YOUR SOLUTION HERE
    return render_template("dashboard.html", title=title)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # YOUR SOLUTION HERE
    session.pop('user_name', None)
    return redirect(url_for('login', error=True))


# users = get_users()
# print(users['Bob'])
if __name__ == '__main__':
    app.run(debug=True)



