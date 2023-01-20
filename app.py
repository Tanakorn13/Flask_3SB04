from flask import Flask,render_template,redirect, url_for, request
from flask_wtf import Form 
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, AnyOf
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        form = request.form['msg']
        print("Message: %s"%(form))
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/template_in')
def template_in ():
    return render_template('template_in.html')

@app.route('/template_out')
def template_out ():
    return render_template('template_out.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000', debug=True)