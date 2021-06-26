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
    def image_request(url, size="original"):

        headers = {
            'Authorization': f'Bearer {TheMovieDatabase.API_TOKEN}',
            'Content-Type': 'application/json;charset=utf-8'
        }

        return requests.get(TheMovieDatabase.IMAGES["endpoint"]["base_url"] + size + url, headers=headers)

    @staticmethod
    def search_movie(query, language=None, include_adult=False, region=None, year=None, primary_release_year=None):

        req = f"/3/search/movie?query={query}"

        if language is not None:
            req += f"&language={language}"

        if include_adult:
            req += f"&include_adult=True"

        if region is not None:
            req += f"&region={region}"

        if year is not None:
            req += f"&year={year}"

        if primary_release_year is not None:
            req += f"&primary_release_year={primary_release_year}"

        # this will be displayed in the search GUI, and then sorted based on the selected movie
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def search_tv_show(query, language=None, include_adult=False, first_air_date_year=None):

        req = f"/3/search/tv?query={query}"

        if language is not None:
            req += f"&language={language}"

        if include_adult:
            req += f"&include_adult=True"

        if first_air_date_year is not None:
            req += f"&first_air_date_year={first_air_date_year}"

        # this will be displayed in the search GUI, and then sorted based on the selected movie
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_movie_details(movie_id):

        req = f"/3/movie/{movie_id}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def search_person(query):

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
    def search_keyword(query):

        query = query.replace(" ", "%")
        req = f"/3/search/company?query={query}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def search_company(query):

        query = query.replace(" ", "%")
        print(query)
        req = f"/3/search/company?query={query}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def search_collection(query):

        query = query.replace(" ", "%")
        req = f"/3/search/company?query={query}"
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

    @staticmethod
    def get_recommended_movies(movie_id):

        req = f"/3/movie/{movie_id}/recommendations"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_similar_movies(movie_id):

        req = f"/3/movie/{movie_id}/similar"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_now_playing(country_code):

        req = f"/3/movie/now_playing?region={country_code}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_upcoming_movies(country_code):

        req = f"/3/movie/upcoming?region={country_code}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_reviews(movie_id):

        req = f"/3/movie/{movie_id}/reviews"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_translations(movie_id):

        req = f"/3/movie/{movie_id}/translations"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_additional_videos(movie_id):

        req = f"/3/movie/{movie_id}/videos"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_belonging_lists(movie_id):

        req = f"/3/movie/{movie_id}/lists"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_images(movie_id):

        req = f"/3/movie/{movie_id}/images"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_tv_images(tv_id):

        req = f"/3/tv/{tv_id}/images"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_first_image(response, language="en"):

        url = ""

        for pictures in response["backdrops"]:
            if pictures["iso_639_1"] == language:
                url = pictures["file_path"]
                break

        if url == "":
            TheMovieDatabase.get_first_image(response, language="en")
            return

        filename = url.replace("/", "")
        response = TheMovieDatabase.image_request(url)

        with open(filename, 'wb') as f:
            f.write(response.content)

        print('Image successfully downloaded as : ', filename)

    @staticmethod
    def get_first_poster(response, language="en"):

        url = ""

        for pictures in response["posters"]:
            if pictures["iso_639_1"] == language:
                url = pictures["file_path"]
                break

        if url == "":
            TheMovieDatabase.get_first_poster(response, language="en")
            return

        filename = url.replace("/", "")
        response = TheMovieDatabase.image_request(url)

        with open(filename, 'wb') as f:
            f.write(response.content)

        print('Poster successfully downloaded as : ', filename)

    @staticmethod
    def get_person_details(person_id):

        req = f"/3/person/{person_id}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_review_details(review_id):

        req = f"/3/review/{review_id}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_tv_details(tv_id):

        req = f"/3/tv/{tv_id}"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_alternatives_tv_titles(tv_id):

        req = f"/3/tv/{tv_id}/alternative_titles"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_tv_credits(tv_id):

        req = f"/3/tv/{tv_id}/credits"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_associated_tv_keywords(tv_id):

        req = f"/3/tv/{tv_id}/keywords"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_recommended_tv_shows(tv_id):

        req = f"/3/tv/{tv_id}/recommendations"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_tv_review(tv_id):

        req = f"/3/tv/{tv_id}/reviews"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_similar_tv_shows(tv_id):

        req = f"/3/tv/{tv_id}/similar"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_tv_translations(tv_id):

        req = f"/3/tv/{tv_id}/translations"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")

    @staticmethod
    def get_additional_tv_videos(tv_id):

        req = f"/3/tv/{tv_id}/videos"
        response = TheMovieDatabase.r(req)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            raise AuthenticationFailed("Authentication failed: You do not have permissions to access the service.")

        elif response.status_code == 404:
            raise InvalidID("Invalid id: The pre-requisite id is invalid or not found.")


TheMovieDatabase.configure('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTAzYzhiZTE4ZDE5YjFiNGRjMTAyYzZkYzZkM2QyZCIsInN1YiI6IjYwNT'
                           'c3MTE2NmUzZGViMDA1NGU4NWZmYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GflopqdlA5QCpd'
                           'XuAWonQyxBFmWHz_DRUwzd0sKO9qc')

# print(TheMovieDatabase.IMAGES)

# print(TheMovieDatabase.search_movie("iron man"))
# print(TheMovieDatabase.get_movie_details(1726))
# print(TheMovieDatabase.get_film_genres())
# print(TheMovieDatabase.get_tv_genres())
# print(TheMovieDatabase.search_tv_show("Chernobyl"))
# print(TheMovieDatabase.search_person("Emma Watson"))
# print(TheMovieDatabase.get_movie_credits(1726))
# print(TheMovieDatabase.get_alternatives_titles(1726))
# print(TheMovieDatabase.get_releases_dates(1726))
# print(TheMovieDatabase.get_associated_keywords(1726))
# print(TheMovieDatabase.get_similar_movies(1726))
# print(TheMovieDatabase.get_now_playing("FR"))
# print(TheMovieDatabase.get_upcoming_movies("FR"))
# print(TheMovieDatabase.get_reviews(1726))
# print(TheMovieDatabase.get_translations(1726))
# print(TheMovieDatabase.get_additional_videos(1726))
# print(TheMovieDatabase.get_belonging_lists(1726))#
# print(TheMovieDatabase.get_person_details(10990))
# print(TheMovieDatabase.get_review_details("59cc634fc3a3682aa30065a3"))
# print(TheMovieDatabase.search_company("Columbia Pictures"))
# print(TheMovieDatabase.search_collection("Marvel"))
# print(TheMovieDatabase.search_keyword("Mission"))
# print(TheMovieDatabase.get_tv_details(87108))
# print(TheMovieDatabase.get_alternatives_tv_titles(87108))
# print(TheMovieDatabase.get_tv_credits(87108))
# print(TheMovieDatabase.get_associated_tv_keywords(87108))
# print(TheMovieDatabase.get_recommended_movies(1726))
# print(TheMovieDatabase.get_recommended_tv_shows(87108))
# print(TheMovieDatabase.get_tv_review(87108))
# print(TheMovieDatabase.get_similar_tv_shows(87108))
# print(TheMovieDatabase.get_tv_translations(87108))
# print(TheMovieDatabase.get_additional_tv_videos(87108))

# returned = TheMovieDatabase.get_images(1726)
# TheMovieDatabase.get_first_poster(returned)
# TheMovieDatabase.get_first_image(returned)


# returned = TheMovieDatabase.get_tv_images(87108)
# TheMovieDatabase.get_first_poster(returned, language="fr")
# TheMovieDatabase.get_first_image(returned, language="fr")


# Todo : Add additional parameters
# Todo : Split class between TheMovieDatabaseMovies and TheMovieDatabaseTV ?
