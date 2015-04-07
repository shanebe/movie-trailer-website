import webbrowser


class Movie():
    """ The Movie Class - Contains the blueprint for Movie instances.
    
        Attributes: 
        movie_title: A string containing the movie's title
        movie_storyline: A string containing the movie's synopsis
        poster_image: A string containing the URL of the movie poster image file
        trailer_youtube: A string containing the URL of the movie's trailer on youtube
        movie_rating: An integer of the movie's rating (Class variable VALID_RATINGS)
        
        Usage: Movie('Movie Title', 'Storyline', 'Poster Image URL', 'Youtube Trailer URL', 'Rating 0-3 (G, PG, PG13, R)' """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Constant Class Variable "VALID_RATINGS", capitalized as Class Variable
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating):
        """ Inits the Movie class with 5 attributes """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_rating = movie_rating

    def show_trailer(self):
        """ Shows the trailer for the Movie object """
        webbrowser.open(self.trailer_youtube_url)
