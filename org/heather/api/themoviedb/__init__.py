import requests


class TheMovieDatabase():

    API_TOKEN = None

    ENDPOINT = "https://api.themoviedb.org"

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
    def find_movie_detais(query):
        pass

    @staticmethod
    def find_casts(film):
        pass

    #etc...


TheMovieDatabase.configure('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTAzYzhiZTE4ZDE5YjFiNGRjMTAyYzZkYzZkM2QyZCIsInN1YiI6IjYwNTc3MTE2NmUzZGViMDA1NGU4NWZmYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GflopqdlA5QCpdXuAWonQyxBFmWHz_DRUwzd0sKO9qc')