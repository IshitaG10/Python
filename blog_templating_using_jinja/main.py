from flask import Flask, render_template
from post import Post

Posts = Post()
all_posts = Posts.blogs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = all_posts)

@app.route('/post/<int:num>')
def posts(num):
    return render_template("post.html", all_posts = all_posts, blog_id = num)

if __name__ == "__main__":
    app.run(debug=True)
