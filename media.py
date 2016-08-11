# import fresh_tomotoes module in order to
# use open_movies_page method which takes list of our movies
# and display them in web brower
import fresh_tomatoes
""" create a template for our movies"""


class Movie(object):
    """ this is a class movie which holds data stracture,
    title ,trailer_youtube_url and poster_image
    """
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

# create instance objects from our class

first_movie = Movie(
    "Eritrean movie",
    "https://www.youtube.com/watch?v=zaN8jYI5m6M",
    "https://i.ytimg.com/vi/DvegFUeljKI/maxresdefault.jpg")
second_movie = Movie(
    "Wuhubtoy",
    "https://www.youtube.com/watch?v=zaN8jYI5m6M",
    "http://www.raimoq.com/wp-content/uploads/2015/01/eri-movie-wuhbtoy-490.jpg")  # noqa
third_movie = Movie(
    "Dihri Erab Tsehay",
    "https://www.youtube.com/watch?v=zaN8jYI5m6M",
    "http://www.raimoq.com/wp-content/uploads/2015/01/Dhri-Erab-Tsehay-490.jpg")  # noqa 
fourth_movie = Movie(
    "Eritrean movie",
    "https://www.youtube.com/watch?v=zaN8jYI5m6M",
    "https://i.ytimg.com/vi/DvegFUeljKI/maxresdefault.jpg")
fifth_movie = Movie(
    "American Movie",
    "https://www.youtube.com/watch?v=zaN8jYI5m6M", "https://upload.wikimedia.org/wikipedia/en/thumb/a/aa/Americanmovie.jpg/220px-Americanmovie.jpg")  # noqa 
sixth_movie = Movie(
    "Class Act",
    "https://www.youtube.com/watch?v=zaN8jYI5m6M", "http://brianorndorf.typepad.com/.a/6a00e54ee7b642883301676708f1e3970b-500wi")  # noqa 
seventh_movie = Movie(
    "Aby Eyu Emo Gezawtikum",
    "https://www.youtube.com/watch?v=zaN8jYI5m6M",
    "https://i.ytimg.com/vi/DvegFUeljKI/maxresdefault.jpg")

# create a list that store all instance 
# objects and pass them to open_movie_pages
movies = [
    first_movie,
    second_movie,
    third_movie,
    fourth_movie,
    fifth_movie,
    sixth_movie,
    seventh_movie]
fresh_tomatoes.open_movies_page(movies)
