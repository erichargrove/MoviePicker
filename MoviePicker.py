import tkinter as tk
from tkinter import ttk
import random
import time
import threading

movies = [
    "Jurassic Park", "Cats (the original)", "Pride and Prejudice", "Parasite",
    "Snowpiercer", "A Silent Voice", "Your Name",
    "Josee, The Tiger, and The Fish", "The Last Jedi", "Rogue One",
    "Samurai Cop", "Godzilla Minus One", "Shin Godzilla",
    "Godzilla: King of the Monsters", "Godzilla vs. Kong",
    "Godzilla x Kong: The New Empire", "Dune",
    "Seven Brides for Seven Brothers", "Yentl", "Wicked", "The Swan Princess",
    "Elder Millenial", "Confirmed Kills", "Warrior"
]


class MoviePickerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Movie Picker")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')

        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        self.title_label = ttk.Label(self.main_frame,
                                     text="Movie Picker",
                                     font=('Helvetica', 24, 'bold'))
        self.title_label.pack(pady=20)

        # Movie display label
        self.movie_label = ttk.Label(self.main_frame,
                                     text="Click 'Pick Movie' to start",
                                     font=('Helvetica', 14))
        self.movie_label.pack(pady=20)

        # Pick movie button
        self.pick_button = ttk.Button(self.main_frame,
                                      text="Pick Movie",
                                      command=self.start_picking)
        self.pick_button.pack(pady=20)

        # Status label
        self.status_label = ttk.Label(self.main_frame,
                                      text="",
                                      font=('Helvetica', 10))
        self.status_label.pack(pady=10)

    def start_picking(self):
        self.pick_button.configure(state='disabled')
        self.status_label.configure(text="Picking a movie...")
        self.picking_thread = threading.Thread(target=self.pick_movie)
        self.picking_thread.start()

    def pick_movie(self):
        runs = 40
        delay = 0.1

        for i in range(runs):
            temp = random.choice(movies)
            self.root.after(0,
                            lambda t=temp: self.movie_label.configure(text=t))
            adjusted_delay = delay * (1 + i / (runs / 2))
            time.sleep(adjusted_delay)

        final_pick = random.choice(movies)
        self.root.after(0, lambda: self.movie_label.configure(text=final_pick))
        self.root.after(
            0, lambda: self.status_label.configure(text="Movie selected!"))
        self.root.after(0, lambda: self.pick_button.configure(state='normal'))


def main():
    root = tk.Tk()
    MoviePickerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
