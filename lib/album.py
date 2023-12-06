class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = self.convert_to_int_or_none(release_year)
        self.artist_id = self.convert_to_int_or_none(artist_id)

    @staticmethod
    def convert_to_int_or_none(value):
        try:
            return int(value) if value not in ["", None] else None
        except ValueError:
            return None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"

    def is_valid(self):
        if self.title == "" or self.title == None:
            return False
        if self.release_year == "" or self.release_year == None:
            return False
        if self.artist_id == "" or self.artist_id == None:
            return False

        return True

    def generate_errors(self):
        errors = []
        if self.title == "" or self.title == None:
            errors.append("Title can't be blank")
        if self.release_year == None or self.release_year == "":
            errors.append("Release Year can't be blank")
        if self.artist_id == None or self.artist_id == "":
            errors.append("Id can't be blank")
        if len(errors) == 0:
            return None

        return ", ".join(errors)
