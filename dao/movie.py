from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie.title,
                                  Movie.description,
                                  Movie.year,
                                  Movie.rating,
                                  Movie.trailer,
                                  Genre.name.label("genre"),
                                  Director.name.label("director")).join(Movie.genre).join(Movie.director)

    def get_one(self, mid):
        movies = self.get_all()
        return movies.filter(Movie.id == mid).one()

    def get_by_director(self, did):
        movies = self.get_all()
        return movies.filter(Movie.director_id == did).all()

    def get_by_genre(self, gid):
        movies = self.get_all()
        return movies.filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        movies = self.get_all()
        return movies.filter(Movie.year == year).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.session.query(Movie).get(mid)
        self.session.delete(movie)
        self.session.commit()
