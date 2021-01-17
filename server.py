from flask import Flask
import random

app = Flask(__name__)
CORRECT_NUM = random.randint(0, 9)


@app.route("/")
def main_page():
    return "<h1>Guess number between 0 and 9</h1>" \
           "<p>You must input your number to URL address, like this http://127.0.0.1:5000/9 where 9 is your number</p>" \
           "<img src='https://media.giphy.com/media/ne3xrYlWtQFtC/giphy.gif'>"


@app.route("/<int:guess>")
def check_guess(guess):
    if CORRECT_NUM > guess:
        return "<h1 style='color:red;'>Too low. Try again!</h1>" \
               "<img src='https://media.giphy.com/media/wViS9n0RqN2/giphy.gif'>"
    elif CORRECT_NUM < guess:
        return "<h1 style='color:orange;'>Too high. Try again!</h1>" \
               "<img src='https://media.giphy.com/media/yoJC2Olx0ekMy2nX7W/giphy.gif'>"
    else:
        return "<h1 style='color:green;'>You found it! Congratulations!</h1>" \
               "<img src='https://media.giphy.com/media/6dSwtLb9q1UuA/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
