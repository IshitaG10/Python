from flask import Flask
import random

app =  Flask(__name__)

random_number = random.randint(0,9)

#decorator function for guessing number
def higher_lower(function):
    def wrapper(*args, **kwargs):
        num = function(**kwargs)
        if num > random_number:
            return '<h1 style = "color:violet"> Too High! Try again </h1>'\
                   '<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width = "500"  height = "500">'
        
        elif num < random_number:
            return '<h1 style = "color:red"> Too Low! Try again </h1>'\
                   '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width = "500"  height = "500">'
        
        else:
            return '<h1 style = "color:green"> You found me! </h1>'\
                   '<img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width = "500"  height = "500">'
    return wrapper

#for home page
@app.route("/")
def landing_page():
    return '<h1>Guess a number between 0 and 9 </h1>' \
            '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width = "500"  height = "500">'


#for other pages and getting number
@app.route("/<int:number>")
@higher_lower
def guess_number(number):
    return number
    

if __name__ == "__main__":
    app.run(debug=True)