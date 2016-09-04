from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/login')
def login():
    return 'Please login'

if __name__ == '__main__':
    app.run()
