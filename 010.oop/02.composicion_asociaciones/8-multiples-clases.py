"""
Archivo python con clases y asociaciones
"""

# 1. Crear la clase
class Movie:
    # Atributos de clase

    # Método constructor
    def __init__(self, title, sinopsis, duration, genres, rate, ratings, director, downloads_num, release_year):
        self.title = title
        self.sinopsis = sinopsis
        self.duration = duration
        self.genres = genres
        self.rate = rate
        self.ratings = ratings
        self.director = director
        self.downloads_num = downloads_num
        self.release_year = release_year

    # Métodos (Comportamiento)
    def __str__(self):
        return f"Movie(title={self.title}, " \
               f"sinopsis= {self.sinopsis}, " \
               f"duration= {self.duration}, " \
               f"genres= {self.genres}, " \
               f"rate= {self.rate}, " \
               f"ratings= {self.ratings}, " \
               f"director= {self.director}, " \
               f"downloads_num= {self.downloads_num}, " \
               f"release_year= {self.release_year}" \
               f")"

    def __repr__(self):
        return self.__str__()


class Director:
    def __init__(self, first_name, last_name, num_movies, active_years):
        self.first_name = first_name
        self.last_name = last_name
        self.num_movies = num_movies
        self.active_years = active_years

    def __str__(self):
        return f"Director(first_name={self.first_name}, " \
               f"last_name={self.last_name}, " \
               f"num_movies={self.num_movies}, " \
               f"active_years={self.active_years}" \
               f")"

    def __repr__(self):
        return self.__str__()


class Genre:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Cinema:
    def __init__(self, name, current_movies, num_rooms, num_places, street, province):
        self.name = name
        self.current_movies = current_movies
        self.num_rooms = num_rooms
        self.num_places = num_places
        self.street = street
        self.province = province

    def __str__(self):
        return f"Cinema(name={self.name}, " \
               f"current_movies={self.current_movies}, " \
               f"num_rooms={self.num_rooms}, " \
               f"num_places={self.num_places}, " \
               f"street={self.street}, " \
               f"province={self.province}" \
               f")"

    def __repr__(self):
        return self.__str__()


# 2. Crear objetos

# 2.1 Crear un director
alan_smith = Director("Alan", "Smith", 43, 20)
mark_macina = Director("Mark", "Macina", 38, 18)

# 2.2 Crear géneros para las películas
action = Genre("Action")
scifi = Genre("Sci-Fi")
drama = Genre("Drama")
horror = Genre("Horror")
comedia = Genre("Comedia")

movie1_genres = [action, scifi, drama]
movie2_genres = [comedia, action]

# 2.3 Crear películas
movie1 = Movie("Fast and Furious 9", "Lorem ipsum dolor", 160, movie1_genres, 9, [6, 9, 4, 7, 8, 8, 7, 6],
               alan_smith, 5600000, 2021)

movie2 = Movie("Bad Boys", "Will smith ....", 130, movie2_genres, 10, [10, 9, 9.5, 10, 10, 8, 10, 10],
               mark_macina, 8100000, 2020)

# 2.4 Crear cine

cinema = Cinema("Odeon", [movie1, movie2], 4, 100, "Calle falsa", "Madrid")
print(cinema)