from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/me')
def info():
    return render_template("me.html")


@app.route('/mypage/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "GET":
        print("GET received")
        return render_template("contact.html")
    elif request.method == "POST":
        print("POST received")
        print(request.form)
        return render_template("contact.html")