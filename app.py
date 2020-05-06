from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    
    name = os.environ['USER']
    return f'Hello, {name}!'


@app.route('/page')
def page():
    return f'Another Page!'

if __name__ == "__main__" :
    app.run()

