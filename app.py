from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user')
def user():
    return redirect('https://github.com/lucasdevcampos')

@app.route('/config')
def config():
    return None

if __name__ =='__main__':
    app.run(debug=True)
