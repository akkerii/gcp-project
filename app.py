from flask import Flask



app=Flask(__name__)

@app.route('/')

def helloWorld() : 
    return 'hello , simple flask app'
