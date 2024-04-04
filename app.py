from flask import Flask, request, jsonify
from data import users, movies, ratings


app = Flask(__name__)



registered_movie_names = {} # Registered movie names. 
movie_id_counter = 0
user_id_counter = 0 

logged_in_user = None


def is_authenticated():
    return logged_in_user is not None


@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("phone")

    # Validate required fields
    if not all(field in data for field in ["name", "email", "password", "phone"]):
        return jsonify({"message": "Missing required fields"}), 400

    # Check if the user already exists
    if any(user["email"] == email for user in users):
        return jsonify({"message": "User already registered"}), 400

    # Auto-increment user ID
    global user_id_counter
    user_id_counter += 1

    # Create user dictionary
    user_data = {"id": user_id_counter, "name": name, "email": email, "password": password, "phone": phone}

    users.append(user_data)
    return jsonify({"message": "User registered successfully", "id": user_id_counter}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = next((user for user in users if user["email"] == email and user["password"] == password), None)
    if user:
        global logged_in_user
        logged_in_user = user 

        return jsonify({"message": "Login successful", "user": user}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    

@app.route("/logout", methods=["GET"])
def logout():
    global logged_in_user
    if not logged_in_user:
        return jsonify({"message": "No user is logged In"})
    
    logged_in_user = None
    return jsonify({"message": "Logged out successfully"}), 200

@app.route("/movies", methods=["GET"])
def get_movies():
    if not is_authenticated():
        return jsonify({"message": "Login first"}), 401
    
    return jsonify({"movies": movies}), 200

@app.route("/add_movie", methods=["POST"])
def add_movie():
    data = request.get_json()

    if not is_authenticated():
        return jsonify({"message": "Login first"}), 401

    name = data.get("name")

    if name.lower() in registered_movie_names:
        return jsonify({"message": "Movie already exists"})
# clauid.ai    
    global movie_id_counter
    movie_id_counter += 1
    data["id"] =   movie_id_counter
    movies.append(data)
    registered_movie_names[name.lower()] = True

    return jsonify({"message": "Movie added successfully"}), 400

@app.route("/rate_movie/<int:movie_id>", methods=["POST"])
def rate_movie(movie_id):
    data = request.get_json()
    rating = data.get("rating")

    if not is_authenticated():
        return jsonify({"message": "Login first"}), 401
    
    global logged_in_user
    user_id = logged_in_user["id"]

    # Check if the movie ID exists
    if not any(movie["id"] == movie_id for movie in movies):
        return jsonify({"message": "Movie not found"}), 404
    
    if rating < 1 or rating > 5:
        return jsonify({"message": "Invalid rating"}), 404

    # Add rating if movie exists
    ratings.append({"user_id": user_id, "movie_id": movie_id, "rating": rating})
    return jsonify({"message": "Rating added successfully"}), 201


import re 
@app.route("/movie_details/<string:search_keyword>", methods=["GET"])
def get_movie_details(search_keyword = ""):
    matching_movies = []

    # Search for movies that match the search keyword
    for movie in movies:
        if re.search(search_keyword, movie["name"], re.IGNORECASE):
            movie_ratings = [rating["rating"] for rating in ratings if rating["movie_id"] == movie["id"]]
            average_rating = sum(movie_ratings) / len(movie_ratings) if movie_ratings else 0
            movie["average_rating"] = average_rating
            matching_movies.append(movie)

    if not matching_movies:
        return jsonify({"message": "No movies found"}), 404

    return jsonify({"movies": matching_movies}), 200

if __name__ == "__main__":

    movie_id_counter = len(movies)
    user_id_counter = len(users)

    app.run(debug=True)
