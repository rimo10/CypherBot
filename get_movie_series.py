from tmdbv3api import Movie, TMDb, TV, Episode
import random

tmdb = TMDb()
tmdb.api_key = "b0f4fccbd5fddb19f5d116bb8c649be2"


def get_recommendation():
    movie = Movie()
    recommendation = random.choice(movie.top_rated())
    return {"title": recommendation.title, "overview": recommendation.overview,
            "poster": "https://image.tmdb.org/t/p/w500/" + recommendation.poster_path}


def get_similar(similar):
    movie = Movie()
    movies = movie.search(similar)
    similar_movies = movie.similar(random.choice(movies).id)
    similar_movie = random.choice(similar_movies)
    return {"title": similar_movie.title, "overview": similar_movie.overview,
            "poster": "https://image.tmdb.org/t/p/w500/" + similar_movie.poster_path}


def get_series():
    series = TV()
    recommendation = random.choice(series.top_rated(1))
    return {"title": recommendation.name, "overview": recommendation.overview,
            "poster": "https://image.tmdb.org/t/p/w500/" + recommendation.poster_path}


if __name__ == "__main__":
    print(get_recommendation())
    print("\n")
    text = input("Enter movies similar to:")
    print(get_similar(text))
    print(get_series())
