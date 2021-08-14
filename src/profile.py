class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourite_movies = []

    def add_favourite_movie(self, movie):
        self.favourite_movies.append(movie)

    def remove_favourite_movie(self, movie):
        self.favourite_movies.remove(movie)

    # def return_favourite_movies(self):
    #     return profile.favourite_movies