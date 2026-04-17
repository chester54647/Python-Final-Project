from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

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
        image = request.files.get("image")

        image_name = ""

        if image:
            image_name = image.filename
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_name)
            image.save(image_path)

        game = {
            "title": title,
            "genre": genre,
            "platform": platform,
            "rating": rating,
            "image": image_name
        }
        games_list.append(game)

    return render_template("add.html")

@app.route("/remove")
def remove_game():
    return render_template("remove.html")

if __name__ == "__main__":
    app.run(debug=True)