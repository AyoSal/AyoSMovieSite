import fresh_tomatoes
import media

print ( "Some Great James Bond Movies")


dieanotherday = media.Movie("Die Another Day",
                            "The 20th spy film in the James Bond series based on Ian Flemmings work",
                            "https://upload.wikimedia.org/wikipedia/en/3/3d/Die_another_Day_-_UK_cinema_poster.jpg",
                            "https://www.youtube.com/watch?v=Aq0f1wYo6Vk")
print(dieanotherday.storyline)
#dieanotherday.show_trailer()

casinoroyale = media.Movie("Casino Royale",
                            "The 21st spy film in the James Bond series based on Ian Flemmings work",
                            "https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg",
                            "https://www.youtube.com/watch?v=36mnx8dBbGE")
print(casinoroyale.storyline)
#casinoroyale.show_trailer()

quantumofsolace = media.Movie("Quantum of Solace",
                              "The 22nd spy film in the James Bond series based on Ian Flemmings work",
                              "https://upload.wikimedia.org/wikipedia/en/2/2d/Quantum_of_Solace_-_UK_cinema_poster.jpg",
                              "https://www.youtube.com/watch?v=Ecq4uC0RHIs")
print(quantumofsolace.storyline)
#quantumofsolace.show_trailer()

skyfall = media.Movie("SkyFall",
                      "The 23rd spy film in the James Bond series based on Ian Flemmings work",
                      "https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
                      "https://www.youtube.com/watch?v=6kw1UVovByw")
print(skyfall.storyline)
#skyfall.show_trailer()

spectre = media.Movie("Spectre",
                      "The 24th spy film in the James Bond series based on Ian Flemmings work",
                      "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                      "https://www.youtube.com/watch?v=vBnGxAkdh_k")
print(spectre.storyline)
#spectre.show_trailer()

risico = media.Movie("Risico",
                     "The 25th spy film in the James Bond series based on Ian Flemmings work",
                     "/Users/AyoSal/Documents/Python Tins/risico.tiff",
                     "https://www.youtube.com/watch?v=hUu6juQpLIs")
print(risico.storyline)
#risico.show_trailer()


movies = [dieanotherday, casinoroyale, quantumofsolace, skyfall, spectre, risico]
fresh_tomatoes.open_movies_page(movies)

