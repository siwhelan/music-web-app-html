from lib.artist import Artist


class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        artists = []
        for row in rows:
            item = Artist(row["id"], row["artist"])
            artists.append(item)
        return artists

    def create(self, artist):
        self._connection.execute(
            "INSERT INTO artists (artist) VALUES (%s)", [artist.artist]
        )
        return None

    def find_by_id(self, artist_id):
        rows = self._connection.execute(
            "SELECT * FROM artists WHERE id = %s", [artist_id]
        )

        if rows:
            row = rows[0]
            return Artist(row["id"], row["artist"])
        else:
            return None
