import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# ========== Artist Routes ========== #


@app.route("/artists", methods=["POST"])
def post_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = Artist(None, request.form["artist"])
    repo.create(artist)
    return "", 200


@app.route("/artists")
def get_artists_dynamic():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.all()
    return render_template("artists/artists.html", artists=artists)


@app.route("/artists/<int:artist_id>")
def get_artist(artist_id):
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = repo.find_by_id(artist_id)
    # print(album)
    return render_template("artists/artist.html", artist=artist)


# ========== Album Routes ========== #


@app.route("/albums")
def get_albums_dynamic():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.all()
    return render_template("albums/index.html", albums=albums)


@app.route("/albums/<int:album_id>")
def get_album(album_id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = repo.fetch_album_by_id(album_id)
    print(album)
    return render_template("albums/album.html", album=album)


@app.route("/albums/new", methods=["GET"])
def get_new_album_page():
    return render_template("albums/new.html")


@app.route("/albums", methods=["POST"])
def add_album():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    title = request.form["title"]
    release_year = request.form["release_year"]
    artist_id = request.form["artist_id"]
    album = Album(None, title, release_year, artist_id)
    if not album.is_valid():
        return (
            render_template(
                "albums/new.html", album=album, errors=album.generate_errors()
            ),
            400,
        )
    album = repo.create(album)
    return redirect(f"/albums/{album.id}")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
