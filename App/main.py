from flask import Flask
app = Flask(__name__)

@app.route('/')
def try_app():
    return 'Trying and crying'