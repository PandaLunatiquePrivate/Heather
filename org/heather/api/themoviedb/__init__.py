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
        headers = {
            'Authorization': f'Bearer {TheMovieDatabase.API_TOKEN}',
            'Content-Type': 'application/json;charset=utf-8'
        }

        req = f"/3/search/movie?query={query}"

        # this will be displayed in the search GUI, and then sorted based on the selected movie
        response = requests.get(TheMovieDatabase.ENDPOINT + req, headers=headers)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def find_movie_details(movie_id):
        headers = {
            'Authorization': f'Bearer {TheMovieDatabase.API_TOKEN}',
            'Content-Type': 'application/json;charset=utf-8'
        }

        req = f"/3/movie/{movie_id}"
        response = requests.get(TheMovieDatabase.ENDPOINT + req, headers=headers)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def find_casts(film):
        pass

    #etc...


TheMovieDatabase.configure('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTAzYzhiZTE4ZDE5YjFiNGRjMTAyYzZkYzZkM2QyZCIsInN1YiI6IjYwNTc3MTE2NmUzZGViMDA1NGU4NWZmYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GflopqdlA5QCpdXuAWonQyxBFmWHz_DRUwzd0sKO9qc')
# print(TheMovieDatabase.IMAGES)

# print(TheMovieDatabase.find_movie_details("iron man"))
print(TheMovieDatabase.find_movie_details(1726))
