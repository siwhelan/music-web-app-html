class Artist:
    def __init__(self, id, artist):
        self.id = id
        self.artist = artist

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Artist({self.id}, {self.artist})"
