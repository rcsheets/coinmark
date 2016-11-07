from flask import Flask

app = Flask(__name__)

def init_db():
    """Initializes the database"""
    pass

@app.route('/')
def hello_world():
    return 'Hello, world!'
