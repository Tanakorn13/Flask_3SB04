from flask import Flask,render_template,redirect, url_for, request

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

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000', debug=True)