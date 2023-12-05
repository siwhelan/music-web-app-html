from lib.album import Album


# test album construct
def test_album_init_state():
    album = Album(5, "Album Title", 2002, 4)
    assert album.id == 5
    assert album.title == "Album Title"
    assert album.release_year == 2002
    assert album.artist_id == 4


# test eq method for album
def test_album_eq():
    album1 = Album(5, "Album Title", 2002, 4)
    album2 = Album(5, "Album Title", 2002, 4)
    assert album1 == album2


# test repr method for album
def test_album_repr():
    album = Album(5, "Album Title", 2002, 4)
    assert repr(album) == "Album(5, Album Title, 2002, 4)"
