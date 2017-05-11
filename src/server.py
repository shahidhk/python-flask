from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return json.dumps({"message":"Hello World! 123456"})

@app.route("/hai")    
def hai():
    return "<h1>Hello World</h1><h2>How are you</h2>"
