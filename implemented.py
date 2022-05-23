# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from setup_db import db
from service.movie import MovieService


movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_service = MovieService(movie_dao)
# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)