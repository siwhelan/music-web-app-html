from lib.album_repository import AlbumRepository
from lib.album import Album


# test calling all() returns all albums in list
def test_call_all(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repo = AlbumRepository(db_connection)
    albums = repo.all()
    print(albums)
    assert albums == [
        Album(1, "Demon Days", 2005, 1),
        Album(2, "Doolittle", 1989, 2),
    ]


# test calling create() adds album to list
def test_call_create(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repo = AlbumRepository(db_connection)
    repo.create(Album(None, "Voyager", 2022, 3))
    albums = repo.all()
    assert albums == [
        Album(1, "Demon Days", 2005, 1),
        Album(2, "Doolittle", 1989, 2),
        Album(3, "Voyager", 2022, 3),
    ]


# test calling find() returns album by id
def test_call_find(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repo = AlbumRepository(db_connection)
    album = repo.fetch_album_by_id(1)
    assert album == Album(1, "Demon Days", 2005, 1)


# test calling find() returns None if no album found
def test_call_find_none(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repo = AlbumRepository(db_connection)
    album = repo.fetch_album_by_id(100)
    assert album == None
