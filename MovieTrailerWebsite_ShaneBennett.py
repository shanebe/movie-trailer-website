import media
import new_fresh_tomatoes

#Define Movie objects
interstellar = media.Movie("Interstellar",
                           "With our time on Earth coming to an end, a team of explorers undertakes the most important mission in human history; traveling beyond this galaxy to discover whether mankind has a future among the stars.",
                           "http://images.redbox.com/Images/EPC/Detail370/7739.jpg",
                           "http://www.redbox.com/images.redbox.com/Images/EPC/Kiosk/7738.jpg",
                           2)
wild_card = media.Movie("Wild Card",
                        "A hired bodyguard decides to help a friend after she is attacked. ",
                        "http://images.redbox.com/Images/EPC/Kiosk/8217.jpg",
                        "https://www.youtube.com/watch?v=7fJGbTfFPkM",
                        3)
the_imitation_game = media.Movie("The Imitation Game",
                                 "During the winter of 1952, British authorities entered the home of mathematician, cryptanalyst and war hero Alan Turing to investigate a reported burglary. They instead ended up arresting Turing himself on charges of 'gross indecency', an accusation that would lead to his devastating conviction for the criminal offense of homosexuality - little did officials know, they were actually incriminating the pioneer of modern-day computing. Famously leading a motley group of scholars, linguists, chess champions and intelligence officers, he was credited with cracking the so-called unbreakable codes of Germany's World War II Enigma machine. Based on the book 'Alan Turing: The Enigma'",
                                 "http://images.redbox.com/Images/EPC/Kiosk/8130.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM",
                                 2)

into_the_woods = media.Movie("Into The Woods",
                             "This all-star cast with Meryl Streep, Anna Kendrick, Emily Blunt, and Chris Pine tell the magical story about a couple desperate to have a child who embark on a perilous journey into the Woods to lift an evil witch's curse. On their journey they encounter Jack, Red Riding Hood, and Cinderella who are on their own quests to make their wishes come true. ",
                             "http://images.redbox.com/Images/EPC/Kiosk/7886.jpg",
                             "https://www.youtube.com/watch?v=sNVGDZHRJXM",
                             1)

dumb_and_dumber_to = media.Movie("Dumb & Dumber to",
                                 "Twenty years after dimwits Lloyd and Harry set out on their first adventure, they head out in search of Harry's long lost daughter in the hope of gaining a new kidney. ",
                                 "http://images.redbox.com/Images/EPC/Kiosk/7831.jpg",
                                 "http://www.youtube.com/watch?v=lGXHVlEklgQ",
                                 2)

movies = [interstellar,wild_card,the_imitation_game,into_the_woods,dumb_and_dumber_to]
#Put movie objects into array

new_fresh_tomatoes.open_movies_page(movies)
#Call class function open_movies_page with array of movies

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
#Print out built in class functions just because
