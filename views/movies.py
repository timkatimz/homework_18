from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import movie_schema
from implemented import movie_service

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)
        if director_id is not None:
            movies = movie_service.get_by_director(director_id)
        elif genre_id is not None:
            movies = movie_service.get_by_genre(genre_id)
        elif year is not None:
            movies = movie_service.get_by_year(year)
        else:
            movies = movie_service.get_all()
        return movie_schema.dump(movies, many=True), 200

    def post(self):
        data = request.json
        movie_service.create(data)
        return "", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data["id"] = mid
        movie_service.update(data)
        return "Success", 201

    def delete(self, mid):
        movie_service.delete(mid)
        return "Success", 204
