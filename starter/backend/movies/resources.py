from flask import jsonify, request
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
}


class Movies(MethodView):
    def get(self, movie_id=None):
        if movie_id is None:
            payload = [{
                "id": int(movie_key),
                "title": movie["title"],
                "description": movie["description"],
            } for movie_key, movie in movies.items()]
            return jsonify({"movies": payload})

        movie = movies.get(str(movie_id))
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404

        return jsonify({"movie": {"id": int(movie_id), **movie}})

    def post(self):
        payload = request.get_json(silent=True) or {}
        title = payload.get("title")
        description = payload.get("description")

        if not title or not description:
            return jsonify({"error": "title and description are required"}), 400

        new_id = str(max((int(movie_id) for movie_id in movies.keys()), default=0) + 1)
        movies[new_id] = {"title": title, "description": description}
        return jsonify({"movie": {"id": int(new_id), **movies[new_id]}}), 201

    def put(self, movie_id):
        movie = movies.get(str(movie_id))
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404

        payload = request.get_json(silent=True) or {}
        movie["title"] = payload.get("title", movie["title"])
        movie["description"] = payload.get("description", movie["description"])

        return jsonify({"movie": {"id": int(movie_id), **movie}})

    def delete(self, movie_id):
        if str(movie_id) not in movies:
            return jsonify({"error": "Movie not found"}), 404

        del movies[str(movie_id)]
        return jsonify({"deleted": True})
