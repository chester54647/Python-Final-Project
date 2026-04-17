from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

games_list = []

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
    return render_template("games.html", games=games_list)

@app.route("/add", methods=["GET", "POST"])
def add_game():
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

        if allowed_file(image.filename) == False:
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
        games_list.append(game)
        return redirect(url_for("games"))

    return render_template("add.html")

@app.route("/remove")
def remove_game():
    return render_template("remove.html")

if __name__ == "__main__":
    app.run(debug=True)