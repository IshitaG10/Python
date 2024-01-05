from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() +"<b>"
    return wrapper_function

@app.route('/bye')
@make_bold
def say_bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)