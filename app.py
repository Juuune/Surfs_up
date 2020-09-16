from flask import Flask
app = Flask(__name__)
@app.route('/')
def moody():
    return 'I am moody'