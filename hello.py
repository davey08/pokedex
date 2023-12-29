from flask import Flask, render_template
import requests, json


app = Flask(__name__)
@app.route("/")
def get_names():
    req = requests.get(f'https://fakestoreapi.com/products')
    data = json.loads(req.content)
   
    return render_template("index.html",data=data)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)