from lib.artist import Artist


# test artits construction
def test_artist_construct():
    artist = Artist(2, "Artist 1")
    assert artist.id == 2
    assert artist.artist == "Artist 1"


# test eq method
def test_artist_eq():
    artist1 = Artist(1, "Artist 1")
    artist2 = Artist(1, "Artist 1")
    assert artist1 == artist2


# test repr method
def test_repr_method():
    artist = Artist(2, "Artist 2")
    assert repr(artist) == "Artist(2, Artist 2)"
