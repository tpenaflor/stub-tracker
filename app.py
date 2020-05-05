from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


# app.run(host='0.0.0.0',port=5000) #run app in debug mode on port 5000