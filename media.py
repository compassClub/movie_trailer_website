
class Movie():
    """This class creates a template for storing movie attributes of your
    favorite films."""
    def __init__(self, movie_title, poster_image, trailer_url, description):
        """Inits Movie class with some attributes."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
        self.description = description

        
