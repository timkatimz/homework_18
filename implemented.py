from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from setup_db import db
from service.movie import MovieService
from service.genre import GenreService


movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_service = MovieService(movie_dao)
genre_service = GenreService(genre_dao)
director_service = DirectorService(director_dao)
