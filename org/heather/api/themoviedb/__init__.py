import requests


class AuthenticationFailed(Exception):
    pass


class InvalidID(Exception):
    pass


class TheMovieDatabase:

    API_TOKEN = None

    ENDPOINT = "https://api.themoviedb.org"
    IMAGES = {}

    @staticmethod
    def configure(api_token):

        TheMovieDatabase.API_TOKEN = api_token

        res = TheMovieDatabase.r('/3/configuration').json()

        TheMovieDatabase.IMAGES = {
            'endpoint': {
                'base_url': res['images']['base_url'],
                'secure_base_url': res['images']['base_url'],
            },
            'backdrop_sizes': res['images']['backdrop_sizes'],
            'logo_sizes': res['images']['logo_sizes'],
            'poster_sizes': res['images']['poster_sizes'],
            'still_sizes': res['images']['still_sizes']
        }

    @staticmethod
    def r(req):

        headers = {
            'Authorization': f'Bearer {TheMovieDatabase.API_TOKEN}',
            'Content-Type': 'application/json;charset=utf-8'
        }

        return requests.get(TheMovieDatabase.ENDPOINT + req, headers=headers)

    @staticmethod
    def find_movie(query):

        req = f"/3/search/movie?query={query}"

        # this will be displayed in the search GUI, and then sorted based on the selected movie
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def find_tv_show(query):

        req = f"/3/search/tv?query={query}"

        # this will be displayed in the search GUI, and then sorted based on the selected movie
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def find_movie_details(movie_id):

        req = f"/3/movie/{movie_id}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def find_person(query):

        req = f"/3/search/person?query={query}"
        # this will be displayed in the search GUI, and then sorted based on the selected movie
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_film_genres():

        req = f"/3/genre/movie/list"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_tv_genres():

        req = f"/3/genre/tv/list"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_movie_credits(movie_id):

        req = f"/3/movie/{movie_id}/credits"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_alternatives_titles(movie_id):

        req = f"/3/movie/{movie_id}/credits"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_releases_dates(movie_id):

        req = f"/3/movie/{movie_id}/release_dates"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_associated_keywords(movie_id):

        req = f"/3/movie/{movie_id}/keywords"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")
    # etc...


TheMovieDatabase.configure('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTAzYzhiZTE4ZDE5YjFiNGRjMTAyYzZkYzZkM2QyZCIsInN1YiI6IjYwNTc3MTE2NmUzZGViMDA1NGU4NWZmYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GflopqdlA5QCpdXuAWonQyxBFmWHz_DRUwzd0sKO9qc')
# print(TheMovieDatabase.IMAGES)

# print(TheMovieDatabase.find_movie("iron man"))
# print(TheMovieDatabase.find_movie_details(1726))
# print(TheMovieDatabase.get_film_genres())
# print(TheMovieDatabase.get_tv_genres())
# print(TheMovieDatabase.find_tv_show("Chernobyl"))
# print(TheMovieDatabase.find_person("Emma Watson"))
# print(TheMovieDatabase.get_movie_credits(1726))
# print(TheMovieDatabase.get_alternatives_titles(1726))
# print(TheMovieDatabase.get_releases_dates(1726))
print(TheMovieDatabase.get_associated_keywords(1726))

# Todo : Add additional parameters
