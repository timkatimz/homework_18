class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_all(self):
        return self.genre_dao.get_all()

    def get_one(self, mid):
        return self.genre_dao.get_one(mid)
