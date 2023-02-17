from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)

# Desktop\hello-world\templates>


@app.route("/base")
def base(title="Templates - Base"):
    return render_template("base.html", title=title)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/third")
def third():
    return render_template("third.html")


# cd Desktop\hello-world\templates
# set FLASK_APP=main.py
# flask run

if __name__ == '__main__':
    app.run(debug=True)


# cmd: python main.py