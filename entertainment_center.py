#This file will contain the instances of the Movie class.
#The instances will be grouped together in a list so that the
#fresh_tomatoes.py program will be able to do its thing.

import media
import fresh_tomatoes

i_am_legend = movie_class.Movie("I am Legend",
                                "https://upload.wikimedia.org/wikipedia/en/d/df/I_am_legend_teaser.jpg",# NOQA
                                "https://www.youtube.com/watch?v=ewpYq9rgg3w",
                                "Can one man save humanity?")

the_bourne_identity = movie_class.Movie("The Bourne Identity",
                                        "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",# NOQA
                                        "https://www.youtube.com/watch?v=FpKaB5dvQ4g",# NOQA
                                        "A super spy has his own government "
                                        "turn against him, and he doesn't"
                                        "remember why.")

lotr_return_of_the_king = movie_class.Movie("LOTR Return of the King",
                                            "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",# NOQA
                                            "https://www.youtube.com/watch?v=r5X-hFf6Bwo",# NOQA
                                            "Can two hobbits save Middle "
                                            "Earth?")


#Place all the movies into a list that will 
#be provided to the fresh_tomatoes program
movies = [i_am_legend, the_bourne_identity, lotr_return_of_the_king]

fresh_tomatoes.open_movies_page(movies)
