import fresh_tomatoes
import media

# Creating movie instances
toy_story = media.Movie("Toy Story", "1995",
                        "American computer-animated "
                        "buddy comedy adventure film",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Ny_hRfvsmU8")
speed = media.Movie("Speed", "1994",
                    "American Action thriller film",
                    "https://upload.wikimedia.org/wikipedia/en/4/45/Speed_movie_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=J6eWoTuZfFk")
chak_de = media.Movie("Chak de", "2007",
                      "Indian Sports film",
                      "https://upload.wikimedia.org/wikipedia/en/0/0c/Chak_De%21_India.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=6a0-dSMWm5g")
avatar = media.Movie("Avatar", "2009",
                     "American epic science fiction film",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://youtu.be/5PSNL1qE6VY")
midnight_in_paris = media.Movie("Midnight in Paris", "2011",
                                "Fantasy Comedy film",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
frozen = media.Movie("Frozen", "2013",
                     "3D computer animated musical fantasy film",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=L0MK7qz13bU")
dangal = media.Movie("Dangal", "2016",
                     "Indian Hindi-language biographical sports drama film",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=91ZI3IrojMU")
the_jungle_book = media.Movie("The Jungle Book", "2016",
                              "Fantasy Adventure film",
                              "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=eZGFBKpQ3_I")

# Creating a list of movie instances
movies = [speed, toy_story, chak_de, avatar, midnight_in_paris,
          frozen, dangal, the_jungle_book]

# Calling open_movies_page function to create or overwrite the webpage
fresh_tomatoes.open_movies_page(movies)

