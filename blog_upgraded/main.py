from flask import Flask, render_template,request
import requests
import smtplib
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

EMAIL = os.getenv("MY_GMAIL")
PASSWORD = os.getenv("MY_PASSWORD")

response = requests.get(url = "https://api.npoint.io/06c65bdd142f5601b372")
blogs = response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = blogs)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr= EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject: New Message\n\nName:{name}\nEmail:{email}\nPhone no.:{phone}\nMessage:{message}"
                )
        return render_template("contact.html", msg_sent = True)
    
    return render_template("contact.html", msg_sent = False)

@app.route('/posts/<int:num>')
def posts(num):
    return render_template("post.html", post = blogs[num-1])

if __name__ == "__main__":
    app.run(debug=True)
