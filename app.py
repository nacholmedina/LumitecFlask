from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sale")
def sale():
    return render_template("sale.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/tyc")
def tyc():
    return render_template("tyc.html")

@app.route("/exito")
def exito():
    return render_template("exito.html")

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
