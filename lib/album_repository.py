from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def create(self, album):
        self._connection.execute(
            "INSERT into albums (title, release_year, artist_id) VALUES (%s, %s, %s)",
            [album.title, album.release_year, album.artist_id],
        )
        return None

    def fetch_album_by_id(self, album_id):
        rows = self._connection.execute(
            "SELECT * FROM albums WHERE id = %s", [album_id]
        )

        # Check if any row is returned
        if rows:
            # Assuming the first row is the desired album
            row = rows[0]
            return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        else:
            return None
