from flask import Flask, render_template, request

app = Flask(__name__)

games_list = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    return render_template("games.html", games=games_list)

@app.route("/add", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        title = request.form.get("title")
        genre = request.form.get("genre")
        platform = request.form.get("platform")
        rating = request.form.get("rating")
        game = {
            "title": title,
            "genre": genre,
            "platform": platform,
            "rating": rating
        }
        games_list.append(game)

    return render_template("add.html")

@app.route("/remove")
def remove_game():
    return render_template("remove.html")

if __name__ == "__main__":
    app.run(debug=True)