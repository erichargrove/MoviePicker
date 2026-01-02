import tkinter as tk
import random
import time
import threading

# Catppuccin Mocha color scheme
COLORS = {
    "base": "#1e1e2e",
    "text": "#cdd6f4",
    "accent": "#89b4fa",
    "surface": "#313244",
    "surface_highlight": "#45475a",
}

movies = [
    "Cats (the original)",
    "Parasite",
    "Snowpiercer",
    "Your Name",
    "Josee, The Tiger, and The Fish",
    "The Last Jedi",
    "Samurai Cop",
    "Creed 2",
    "Godzilla Minus One",
    "Shin Godzilla",
    "Godzilla: King of the Monsters",
    "Godzilla vs. Kong",
    "Godzilla x Kong: The New Empire",
    "Dune",
    "Seven Brides for Seven Brothers",
    "Wicked",
    "The Swan Princess",
    "42",
    "Warrior",
    "Power Rangers",
    "Salt, Fat, Acid, Heat",
    "Beckham",
    "Big Brother",
    "The Wild Robot",
    "Dark Side of the Ring",
    "McMillions",
    "Glass Onion",
    "Cheer",
    "Death of a Unicorn",
    "The Birdcage",
    "Challengers",
    "Rings of Power",
    "The Lost City",
    "Bullet Train",
    "The Iron Claw",
    "The Boy and the Heron",
    "Edge of Tomorrow",
    "Galaxy Quest",
    "Cats (the new one)",
    "Legion",
    "Abigail",
    "Pokemon The Movie 2000",
    "Pokemon 3",
    "The Smashing Machine",
    "Mickey 17",
    "Fantastic Four (the new one)",
    "Superman (the new good one)",
]


class MoviePickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Picker")
        self.root.geometry("500x400")
        self.root.configure(bg=COLORS["base"])

        # Create main frame
        self.main_frame = tk.Frame(root, bg=COLORS["base"], padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        self.title_label = tk.Label(
            self.main_frame,
            text="Movie Picker",
            font=("Helvetica", 24, "bold"),
            bg=COLORS["base"],
            fg=COLORS["accent"],
        )
        self.title_label.pack(pady=20)

        # Movie display label
        self.movie_label = tk.Label(
            self.main_frame,
            text="Click 'Pick Movie' to start",
            font=("Helvetica", 14),
            bg=COLORS["base"],
            fg=COLORS["text"],
        )
        self.movie_label.pack(pady=20)

        # Pick movie button
        self.pick_button = tk.Button(
            self.main_frame,
            text="Pick Movie",
            command=self.start_picking,
            bg=COLORS["surface"],
            fg=COLORS["text"],
            font=("Helvetica", 12),
            activebackground=COLORS["surface_highlight"],
            activeforeground=COLORS["text"],
            relief=tk.FLAT,
            padx=20,
            pady=10,
        )
        self.pick_button.pack(pady=20)

        # Status label
        self.status_label = tk.Label(
            self.main_frame,
            text="",
            font=("Helvetica", 10),
            bg=COLORS["base"],
            fg=COLORS["text"],
        )
        self.status_label.pack(pady=10)

    def start_picking(self):
        self.pick_button.configure(state="disabled")
        self.status_label.configure(text="Picking a movie...")
        self.picking_thread = threading.Thread(target=self.pick_movie)
        self.picking_thread.start()

    def pick_movie(self):
        runs = 40
        delay = 0.1

        for i in range(runs):
            temp = random.choice(movies)
            self.root.after(0, lambda t=temp: self.movie_label.configure(text=t))
            adjusted_delay = delay * (1 + i / (runs / 2))
            time.sleep(adjusted_delay)

        final_pick = random.choice(movies)
        self.root.after(0, lambda: self.movie_label.configure(text=final_pick))
        self.root.after(0, lambda: self.status_label.configure(text="Movie selected!"))
        self.root.after(0, lambda: self.pick_button.configure(state="normal"))


def main():
    root = tk.Tk()
    MoviePickerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
