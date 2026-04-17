from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.secret_key = "finalprojectkey"


def allowed_file(filename):
    filename = filename.lower()

    if filename.endswith(".jpg"):
        return True
    elif filename.endswith(".jpeg"):
        return True
    elif filename.endswith(".png"):
        return True
    elif filename.endswith(".gif"):
        return True
    else:
        return False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    if "games" not in session:
        session["games"] = []

    return render_template("games.html", games=session["games"])

@app.route("/add", methods=["GET", "POST"])
def add_game():
    if "games" not in session:
        session["games"] = []
    if request.method == "POST":
        title = request.form.get("title")
        genre = request.form.get("genre")
        platform = request.form.get("platform")
        rating = request.form.get("rating")
        image = request.files.get("image")

        if title == "" or genre == "" or platform == "" or rating == "":
            return "All text fields are required."

        if image.filename == "":
            return "Please choose an image file."

        if not allowed_file(image.filename):
            return "Only jpg, jpeg, png, and gif files are allowed."

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
        games = session["games"]
        games.append(game)
        session["games"] = games
        return redirect(url_for("games"))

    return render_template("add.html")

@app.route("/remove", methods=["GET", "POST"])
def remove_game():
    if "games" not in session:
        session["games"] = []
    if request.method == "POST":
        game_index = request.form.get("game_index")

        if game_index is not None:
            games = session["games"]
            index = int(game_index)

            if index >= 0 and index < len(games):
                games.pop(index)
            session["games"] = games

        return redirect(url_for("remove_game"))

    return render_template("remove.html", games=session["games"])

if __name__ == "__main__":
    app.run(debug=True)