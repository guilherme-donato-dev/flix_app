from movies.repository import MovieRepository

class MovieService:

    def __init__(self):
        self.movie_respository =  MovieRepository()

    def get_movies(self):
        return self.movie_respository.get_movies()
    
    def create_movie(self, title, genre, release_date, actors, resume):
        movie = dict(
            title=title,
            genre=genre,
            release_date=release_date,
            actors=actors,
            resume=resume,
        )
        return self.movie_respository.create_movie(movie)
    
    def get_movie_stats(self):
        self.movie_respository.get_movie_stats()