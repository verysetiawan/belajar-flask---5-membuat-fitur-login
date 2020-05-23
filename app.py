from flask import Flask, render_template, url_for, redirect, session, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "IniSecretKeyKu2020"

#buat route untuk halaman index
@app.route("/", methods=["POST", "GET"]) #memberikan hak akses untuk method POST dan GET
def index():
    if "email" in session: #jika sudah login bisa akses halaman home 
        return redirect (url_for('suksesku'))
    
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
    if "email" in session:  #menambahkan autorisasi user yang sudah login untuk bisa akses about
        return render_template ("about.html")
    else:
        return redirect (url_for('index')) #jika user belum login akan di redirect ke index

#buat route untuk halaman contact
@app.route ("/contact")
def contact():
    if "email" in session:  #menambahkan autorisasi user yang sudah login untuk bisa akses about
        return render_template("contact.html")
    else:
        return redirect (url_for('index'))  #jika user belum login akan di redirect ke index

#menambahkan fungsi logout
@app.route ("/logout")
def logout_session():
    if "email" in session : #jika login dengan email maka jika terdapat sesion email akan dihapus dan diredirect ke index
        session.pop ("email")
        return redirect (url_for('index'))
    else:    #jika belum login maka di redirect ke index
        return redirect (url_for('index'))


#menambahkan halaman redirect
@app.route ("/redirect")
def redir():
    return redirect(url_for("about"))


if __name__ == "__main__":
    app.run (host='0.0.0.0', debug=True, port=5001)