#This file will contain the instances of the Movie class.
#The instances will be grouped together in a list so that the
#fresh_tomatoes.py program will be able to do its thing.

import media
import fresh_tomatoes
import requests

#The first movie is manually entered, the next two use an api to get their data.
i_am_legend = media.Movie("I am Legend",
                                "https://upload.wikimedia.org/wikipedia/en/d/df/I_am_legend_teaser.jpg",# NOQA
                                "https://www.youtube.com/watch?v=ewpYq9rgg3w",
                                "Can one man save humanity?")

bourne_response = requests.get("http://www.omdbapi.com/?t=The+Bourne+Identity")
bourne_data = bourne_response.json()
the_bourne_identity = media.Movie(bourne_data['Title'],
                                        bourne_data['Poster'],
                                        "https://www.youtube.com/watch?v=FpKaB5dvQ4g",# NOQA
                                        bourne_data['Plot'])

potter_response = requests.get("http://www.omdbapi.com/?t=Harry+Potter+and+the+",
    "Deathly+Hallows")
potter_data = potter_response.json()
harry_potter = media.Movie(potter_data['Title'],potter_data['Poster'], 
                                "https://www.youtube.com/watch?v=5NYt1qirBWg",
                                potter_data['Plot'])


#Place all the movies into a list that will 
#be provided to the fresh_tomatoes program
movies = [i_am_legend, the_bourne_identity, harry_potter]

fresh_tomatoes.open_movies_page(movies)
