from flask import Flask, render_template
import requests

response = requests.get(url = "https://api.npoint.io/06c65bdd142f5601b372")
blogs = response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = blogs)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/posts/<int:num>')
def posts(num):
    return render_template("post.html", post = blogs[num-1])

if __name__ == "__main__":
    app.run(debug=True)
