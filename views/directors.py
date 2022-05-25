from flask_restx import Resource, Namespace

from dao.model.director import director_schema
from implemented import director_dao

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        directors = director_dao.get_all()
        return director_schema.dump(directors, many=True)


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        director = director_dao.get_one(did)
        return director_schema.dump(director)
