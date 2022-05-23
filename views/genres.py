from flask_restx import Resource, Namespace

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        genres = genre_dao.get_all()
        return genre_schema.dump(genres, many=True)


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid):
        genre = genre_dao.get_one(gid)
        return genre_schema.dump(genre)
