import random
import time
import os

movies = [
    "Jurassic Park", "Fellowship of the Ring (Extended)",
    "Cats (the original)", "Pride and Prejudice", "Parasite", "Snowpiercer",
    "A Silent Voice", "Your Name", "Josee, The Tiger, and The Fish",
    "The Last Jedi", "Rogue One", "Dungeons & Dragon: Honor Among Thieves",
    "Samurai Cop", "Godzilla Minus One", "Shin Godzilla",
    "Godzilla: King of the Monsters", "Godzilla vs. Kong",
    "Godzilla x Kong: The New Empire", "Dune",
    "Seven Brides for Seven Brothers", "Yentl", "Wicked", "The Swan Princess",
    "Elder Millenial", "Confirmed Kills", "True Lies"
]


def pickMovie(movies, runs=40, delay=0.1):
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    print("Picking a random movie!")
    time.sleep(1)

    for i in range(runs):
        clear()
        temp = random.choice(movies)
        print(temp)
        adjustedDelay = delay * (1 + i / (runs / 2))
        time.sleep(adjustedDelay)

    clear()
    finalPick = random.choice(movies)

    print("Selected movie: " + finalPick)
    return finalPick


if __name__ == "__main__":
    pickMovie(movies)
