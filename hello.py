from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
@app.route("/")
def hello_world():
    req = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=386')
    data = json.loads(req.content)
    return render_template("index.html",data=data)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)