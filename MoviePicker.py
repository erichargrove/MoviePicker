import random
import time
import os

movies = [
    "Jurassic Park", "Fellowship of the Ring (Extended)",
    "Cats (the original)", "Pride and Prejudice", "Parasite", "Snowpiercer",
    "A Silent Voice", "Your Name", "Josee, The Tiger, and The Fish",
    "The Last Jedi", "Rogue One"
]


def pickMovie(movies, delay=0.15):
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    print("Picking a random movie!")
    time.sleep(1)

    for i in range(20):
        clear()
        temp = random.choice(movies)
        print(temp)
        adjustedDelay = delay * (1 + i / (20 / 2))
        time.sleep(adjustedDelay)

    clear()
    finalPick = random.choice(movies)

    print("Selected movie: " + finalPick)
    return finalPick


pickMovie(movies)
