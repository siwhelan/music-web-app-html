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


# test is_valid
def test_album_is_valid():
    assert Album(1, "", "", "").is_valid() == False
    assert Album(1, "Album 2", "", "").is_valid() == False
    assert Album(1, "Album 2", 2002, "").is_valid() == False
    assert Album(1, "Album 2", "", 1).is_valid() == False
    assert Album(1, "", 1989, 2).is_valid() == False
    assert Album(1, "Album Title", 1989, 2).is_valid() == True
    assert Album(None, "Album Title", 1989, 2).is_valid() == True


# test generate errors
def test_generate_errors():
    assert (
        Album(1, "", "", "").generate_errors()
        == "Title can't be blank, Release Year can't be blank, Id can't be blank"
    )
    assert (
        Album(1, "Album 2", "", "").generate_errors()
        == "Release Year can't be blank, Id can't be blank"
    )
    assert Album(1, "Album 2", 2002, "").generate_errors() == "Id can't be blank"
    assert Album(1, "Album 2", "", 1).generate_errors() == "Release Year can't be blank"
    assert Album(1, "", 1989, 2).generate_errors() == "Title can't be blank"
    assert Album(1, "Album Title", 1989, 2).generate_errors() == None
    assert Album(None, "Album Title", 1989, 2).generate_errors() == None
