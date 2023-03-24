from flask import Flask, redirect, render_template, request, url_for, flash
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "sjl3uwre93wpuasfhewiorhewrhnsak"
Bootstrap(app)


@app.route("/")
def home():
    movies_endpoint = "https://api.potterdb.com/v1/movies"
    movies = requests.get(movies_endpoint).json()['data']
    all_movies = [movie for movie in movies if movie['attributes']['order'] != 3]
    return render_template("index.html", movies=all_movies)


@app.route("/characters")
def get_characters():
    characters_endpoint = "https://hp-api.onrender.com/api/characters"
    characters = requests.get(characters_endpoint).json()
    harry = [character for character in characters if character["name"] == "Harry Potter"]
    ron = [character for character in characters if character["name"] == "Ron Weasley"]
    hermione = [character for character in characters if character["name"] == "Hermione Granger"]
    draco = [character for character in characters if character["name"] == "Draco Malfoy"]
    return render_template("character.html", harry=harry, ron=ron, hermione=hermione, draco=draco, characters=True)


@app.route("/get-character-details", methods=["GET", "POST"])
def get_character_details():
    if request.method == "POST":
        name = request.form.get("character-name")
        slug_name = name.lower().replace(" ", "-")
        character_endpoint = f"https://api.potterdb.com/v1/characters/{slug_name}"
        try:
            character_details = requests.get(character_endpoint).json()["data"]
            return render_template("character_details.html", character=character_details)
        except KeyError:
            flash("Please kindly try another name.")
            return redirect(url_for("get_characters"))


@app.route("/books")
def get_books():
    books_endpoint = "https://api.potterdb.com/v1/books"
    all_books = requests.get(books_endpoint).json()["data"]
    return render_template("books.html", books=all_books)


@app.route("/spells/1")
def get_spells_1():
    spells_endpoint = "https://api.potterdb.com/v1/spells"
    all_spells = requests.get(spells_endpoint).json()["data"]
    spells = [spell for spell in all_spells if spell["attributes"]["image"] is not None
              and spell["attributes"]["incantation"] is not None]
    even_spells = []
    odd_spells = []
    for i in range(len(spells)):
        if i % 2 == 0:
            even_spells.append(spells[i])
        else:
            odd_spells.append(spells[i])
    return render_template("spells.html", even_spells=even_spells, odd_spells=odd_spells, page1=True)


@app.route("/spells/2")
def get_spells_2():
    spells_endpoint = "https://api.potterdb.com/v1/spells?page[number]=2"
    all_spells = requests.get(spells_endpoint).json()["data"]
    spells = [spell for spell in all_spells if spell["attributes"]["image"] is not None
              and spell["attributes"]["incantation"] is not None]
    even_spells = []
    odd_spells = []
    for i in range(len(spells)):
        if i % 2 == 0:
            even_spells.append(spells[i])
        else:
            odd_spells.append(spells[i])
    return render_template("spells.html", even_spells=even_spells, odd_spells=odd_spells, page2=True)


@app.route("/spells/3")
def get_spells_3():
    spells_endpoint = "https://api.potterdb.com/v1/spells?page[number]=3"
    all_spells = requests.get(spells_endpoint).json()["data"]
    spells = [spell for spell in all_spells if spell["attributes"]["image"] is not None
              and spell["attributes"]["incantation"] is not None]
    even_spells = []
    odd_spells = []
    for i in range(len(spells)):
        if i % 2 == 0:
            even_spells.append(spells[i])
        else:
            odd_spells.append(spells[i])
    return render_template("spells.html", even_spells=even_spells, odd_spells=odd_spells, page3=True)


@app.route("/spells/4")
def get_spells_4():
    spells_endpoint = "https://api.potterdb.com/v1/spells?page[number]=4"
    all_spells = requests.get(spells_endpoint).json()["data"]
    spells = [spell for spell in all_spells if spell["attributes"]["image"] is not None
              and spell["attributes"]["incantation"] is not None]
    even_spells = []
    odd_spells = []
    for i in range(len(spells)):
        if i % 2 == 0:
            even_spells.append(spells[i])
        else:
            odd_spells.append(spells[i])
    return render_template("spells.html", even_spells=even_spells, odd_spells=odd_spells, page4=True)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
