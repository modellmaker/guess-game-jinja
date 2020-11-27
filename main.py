import random
from flask import Flask, render_template, request, make_response

app = Flask(__name__)
interval = 5
s_number = random.randint(1, interval)
print(s_number)


@app.route("/")
def index():
    return render_template("index.html", interval=interval)


@app.route("/guess", methods=["POST"])
def guess():
    number = int(request.form.get("number"))
    if number == s_number:
        winner = "Congrats! You guessed right!"
        response = make_response(render_template("index.html", winner=winner, interval=interval))
    elif number < s_number:
        winner = "Try a bigger number."
        response = render_template("index.html", winner=winner, interval=interval)
    elif number > s_number:
        winner = "Try a smaller number."
        response = render_template("index.html", winner=winner, interval=interval)
    return response


if __name__ == "__main__":
    app.run()
