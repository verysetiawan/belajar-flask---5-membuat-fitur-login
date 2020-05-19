from flask import Flask, render_template, url_for, redirect, session, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "IniSecretKeyKu2020"

#buat route untuk halaman index
@app.route("/", methods=["POST", "GET"])
def index():
    #jika button di klik >> akan terjadi request POST
    if request.method == 'POST' :
        email = request.form['email']   #jika pada form dimasukan email (name=email ada di index.html) maka data ditampung di vaiabel email
        password = request.form['password'] #jika pada form dimasukan password (name=password ada di index) maka data ditampung di variabel password
       
        #jika email dan password benar maka dialihkan ke halaman sukses
        if email == 'admin@gmail.com' and password == 'pass' :
            session['email'] = email
            return redirect (url_for('suksesku'))

        #jika salah maka harus login dulu
        else:
            return redirect (url_for('index'))

    return render_template ("index.html")

#buat halaman sukses
@app.route ("/sukses")
def suksesku():
    nilai = 'anda sukses login!!!'
    return render_template ("sukses.html", note_sukses = nilai)

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