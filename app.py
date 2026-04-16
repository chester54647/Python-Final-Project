from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/add", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        return "Form submitted"
    return render_template("add.html")

@app.route("/remove")
def remove_game():
    return render_template("remove.html")

if __name__ == "__main__":
    app.run(debug=True)