from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/mypage')
def index():
    return render_template('index.html')


@app.route("/mypage/me")
def me():
    return render_template("about.html")
    
@app.route("/mypage/contact")
def contact():
    return render_template("contact.html")

@app.route('/message', methods=['POST'])
def message():
        data = request.form.get('data')  
        return f'Dane odebrane: {data}'