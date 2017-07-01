# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,songs,movie_box_of_collection,movie_genre):
        # initialize instance of class Movie

        # this init function initialises space for several strings as input that are Movie Title, Storyline, Link to poster Image, Link to youtube trailer,songs, movie's box office collecton and genre of the movie
        # this function does not return anything
        
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.songs_name=songs
        self.box_of_collection=movie_box_of_collection
        self.genre=movie_genre
    def show_trailer(self):
        #it justs opens youtube trailer of the movie instance for which this fuction is called.
        webbrowser.open(self.trailer_youtube_url)
