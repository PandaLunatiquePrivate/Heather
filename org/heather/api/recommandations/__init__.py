import org.heather.api.themoviedb as TheMovieDatabase


class InvalidType(Exception):
	pass


class RecommendationAlgorithm:

	def __init__(self, age, watched_movies):

		self.age = age
		self.watched_movies = watched_movies

	@staticmethod
	def analyse_movie(movie_id):
		print(TheMovieDatabase.TheMovieDatabase.get_movie_details(movie_id))
		print("Giga analyse")

	@staticmethod
	def algorithm():

		print('Yeeeet')


class RecommendationAlgorithmDeGigaFlemmard:

	def __init__(self, age, watched_movies):
		"""

		:param age: The age of the person, to adapt the recommended movies
		:param watched_movies: A dict containing the watched movies, along with some other parameters.
		Please refer to the documentation.
		"""

		self.age = age
		self.watched_movies = watched_movies  # put a list of movies right here
		self.recommendations = {}

		"""
		
		{
		"movie_name_1": {
			movie_ID_1: X,
			nb_visionage: X,
			genre: [],
			réal: abc,
			cast: abc,
			popu: X.Y,
			keywords: [zekopez, fzefkzepo],
			date_sortie: JJ/MM/AAAA,
			trads: ['en', 'fr', ...]  # iso_639_1  
			},
			
		"movie_name_2": {
			movie_ID_1: X,
			nb_visionage: X,
			genre: [],
			réal: abc,
			cast: abc,
			popu: X.Y,
			keywords: [zekopez, fzefkzepo],
			date_sortie: JJ/MM/AAAA,
			trads: ['en', 'fr', ...]
			},
		}
		
		"""
		self.actualize_values()
		self.algorithm()

	def actualize_values(self):

		if isinstance(self.watched_movies, dict):
			pass
		else:
			raise InvalidType("Watched movies must be a dict, for actualization.")

		for movies in self.watched_movies:

			response = TheMovieDatabase.TheMovieDatabase.search_movie(movies)
			self.watched_movies[movies]["movie_ID"] = response["results"][0]["id"]
			self.watched_movies[movies]["popularity"] = response["results"][0]["popularity"]
			self.watched_movies[movies]["release"] = response["results"][0]["release_date"]

			response = TheMovieDatabase.TheMovieDatabase.get_movie_details(self.watched_movies[movies]["movie_ID"])
			self.watched_movies[movies]["genre"] = response["genres"]

			response = TheMovieDatabase.TheMovieDatabase.get_movie_credits(self.watched_movies[movies]["movie_ID"])

			i = 0
			for characters in response["cast"]:
				if i <= 4:
					self.watched_movies[movies]["cast"].append(characters["name"])

				else:
					break
				i += 1

			for peoples in response["crew"]:
				if peoples["job"].lower() == "Director".lower():
					self.watched_movies[movies]["real"] = peoples["name"]

			response = TheMovieDatabase.TheMovieDatabase.get_associated_keywords(self.watched_movies[movies]["movie_ID"])
			self.watched_movies[movies]["keywords"] = response["keywords"]

			response = TheMovieDatabase.TheMovieDatabase.get_translations(self.watched_movies[movies]["movie_ID"])
			for languages in response["translations"]:
				self.watched_movies[movies]["trads"].append(languages["iso_639_1"])

	@staticmethod
	def analyse_movie(movie_id):
		print(TheMovieDatabase.TheMovieDatabase.get_movie_details(movie_id))
		print("Giga analyse")

	def algorithm(self):

		for movie in self.watched_movies.values():

			self.recommendations[movie["movie_ID"]] = {}

			response = TheMovieDatabase.TheMovieDatabase.get_recommended_movies(movie["movie_ID"])

			nb = 1
			for movies in response["results"]:

				self.recommendations[movie["movie_ID"]].update({
					f"{nb}": {
						"id": movies["id"],
						"title": movies["title"]}
				})

				nb += 1

		recommended_list = {}
		for base_movies in self.recommendations.values():

			for recommended_movies in base_movies.values():

				if recommended_movies["title"] not in recommended_list:

					recommended_list[recommended_movies["title"]] = {
						"iterations": 1
					}

				else:
					recommended_list[recommended_movies["title"]]["iterations"] += 1

		sorted_recommendations = sorted(recommended_list.items(), key=lambda item: item[1]['iterations'], reverse=True)
		self.recommendations = dict(sorted_recommendations)
		print(self.recommendations)

		"""
		response = TheMovieDatabase.TheMovieDatabase.get_similar_movies(1726)
		print(response)
		similar = {}

		nb = 1
		for movies in response["results"]:
			similar.update({nb: {
				"id": movies["id"],
				"title": movies["title"]}
			})

			nb += 1
		"""

		# print(self.recommendations)
		# print(similar)


watched = {
		"Iron Man": {
			"movie_ID": None,
			"nb_visionage": None,
			"genre": None,
			"real": None,
			"cast": [],
			"popularity": None,
			"keywords": None,
			"release": None,
			"trads": []
			},

		"Iron Man 2": {
			"movie_ID": None,
			"nb_visionage": None,
			"genre": None,
			"real": None,
			"cast": [],
			"popularity": None,
			"keywords": None,
			"release": None,
			"trads": []
			},

		"Spider Man : HomeComing": {
			"movie_ID": None,
			"nb_visionage": None,
			"genre": None,
			"real": None,
			"cast": [],
			"popularity": None,
			"keywords": None,
			"release": None,
			"trads": []
			},

		"Avengers Endgame": {
			"movie_ID": None,
			"nb_visionage": None,
			"genre": None,
			"real": None,
			"cast": [],
			"popularity": None,
			"keywords": None,
			"release": None,
			"trads": []
			},

		"The Dark Knight : Le chevalier noir": {
			"movie_ID": None,
			"nb_visionage": None,
			"genre": None,
			"real": None,
			"cast": [],
			"popularity": None,
			"keywords": None,
			"release": None,
			"trads": []
			},

		"La liste de Schindler": {
			"movie_ID": None,
			"nb_visionage": None,
			"genre": None,
			"real": None,
			"cast": [],
			"popularity": None,
			"keywords": None,
			"release": None,
			"trads": []
			},

		"Le Seigneur des anneaux : Le retour du roi": {
			"movie_ID": None,
			"nb_visionage": None,
			"genre": None,
			"real": None,
			"cast": [],
			"popularity": None,
			"keywords": None,
			"release": None,
			"trads": []
			},

		}

instance = RecommendationAlgorithmDeGigaFlemmard(18, watched)

# Todo : System only works for movies, find a way to make it work for series
