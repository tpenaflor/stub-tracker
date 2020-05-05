from flask import Flask, os

app = Flask(__name__)

@app.route('/')
def index():
    
    name = os.environ['USER']
    return f'Hello, {name}!'

if __name__ == "__main__" :
    app.run()

