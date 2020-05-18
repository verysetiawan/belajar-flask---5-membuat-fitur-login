from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "IniSecretKeyKu2020"

#buat route untuk halaman index
@app.route("/")
def index():
    return render_template ("index.html")

#buat route untuk halaman about
@app.route ("/about")
def about():
    return render_template ("about.html")

#buat route untuk halaman contact
@app.route ("/contact")
def contact():
    return render_template("contact.html")

#menambahkan halaman redirect
@app.route ("/redirect")
def redir():
    return redirect(url_for("about"))


if __name__ == "__main__":
    app.run (host='0.0.0.0', debug=True, port=5001)