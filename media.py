import webbrowser

# Creating Movie Class


class Movie():
    """This is a movie class which provides information about a movie.
    self.title(str): title of the movie
    self.title(str): year in which the movie was released
    self.storyline(str): describes the storyline of the movie
    self.poster_image_url(str): provides a link to
                                capture the image of the movie
    self.trailer_youtube_url(str): provides a link
                                   of the youtube trailer of the movie
    """
    def __init__(self, movie_title, movie_year, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.year_released = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



    