from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route('/guess/<name>')
def home(name):
    param = {
    "name" : name
}
    genderize = requests.get(url="https://api.genderize.io", params=param)
    gender  = genderize.json()["gender"]

    agify = requests.get(url="https://api.agify.io", params=param)
    age = agify.json()["age"]
    return render_template("index.html",name = name, age = age, gender = gender)

if __name__ == "__main__":
    app.run(debug=True)