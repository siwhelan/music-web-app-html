from lib.artist_repository import ArtistRepository
from lib.artist import Artist


# test call all artists returns a list of artists
def test_call_all(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repo = ArtistRepository(db_connection)
    albums = repo.all()
    assert albums == [Artist(1, "Gorillaz"), Artist(2, "Pixies")]


# test calling create method adds artist to the db
def test_call_create(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repo = ArtistRepository(db_connection)
    repo.create(Artist(None, "Oasis"))
    artists = repo.all()
    assert artists == [Artist(1, "Gorillaz"), Artist(2, "Pixies"), Artist(3, "Oasis")]


# test find artist by id
def test_call_find_by_id(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repo = ArtistRepository(db_connection)
    result = repo.find_by_id(1)
    assert result == Artist(1, "Gorillaz")
