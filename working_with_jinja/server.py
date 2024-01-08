from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.today().year
    random_number = random.randint(0,10)
    return render_template("index.html", num=random_number, year = current_year )

if __name__ == "__main__":
    app.run(debug=True)
