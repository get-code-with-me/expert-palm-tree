import tkinter as tk
import random
import time

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the Button Game")
        self.root.geometry("400x300")

        # Game variables
        self.score = 0
        self.game_duration = 30  # Game duration in seconds
        self.start_time = None

        # UI Elements
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text=f"Time Left: {self.game_duration}", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        self.click_button = tk.Button(root, text="Click Me!", font=("Arial", 20), command=self.on_click)
        self.click_button.pack(pady=30)

        self.start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        """Start the game and begin the timer."""
        self.score = 0
        self.update_score()
        self.time_left = self.game_duration
        self.update_timer()

        # Hide the start button and show the click button
        self.start_button.pack_forget()
        self.click_button.pack(pady=30)

        self.start_time = time.time()
        self.update_game_timer()

    def update_score(self):
        """Update the score label."""
        self.score_label.config(text=f"Score: {self.score}")

    def update_timer(self):
        """Update the timer label."""
        self.timer_label.config(text=f"Time Left: {self.time_left}")

    def on_click(self):
        """Update the score each time the button is clicked."""
        if self.start_time is None:
            return  # Game has not started yet

        self.score += 1
        self.update_score()
        # Move the button to a random location on the screen after each click
        self.move_button_randomly()

    def move_button_randomly(self):
        """Move the click button to a random position within the window."""
        max_x = self.root.winfo_width() - self.click_button.winfo_width()
        max_y = self.root.winfo_height() - self.click_button.winfo_height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.click_button.place(x=new_x, y=new_y)

    def update_game_timer(self):
        """Update the timer each second and end the game when time is up."""
        if self.time_left > 0:
            elapsed_time = time.time() - self.start_time
            self.time_left = self.game_duration - int(elapsed_time)
            self.update_timer()
            self.root.after(1000, self.update_game_timer)
        else:
            self.end_game()

    def end_game(self):
        """End the game and show the final score."""
        self.click_button.pack_forget()
        self.timer_label.config(text="Time's Up!")
        self.final_score_label = tk.Label(self.root, text=f"Final Score: {self.score}", font=("Arial", 14))
        self.final_score_label.pack(pady=20)
        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Arial", 14), command=self.restart_game)
        self.restart_button.pack(pady=10)

    def restart_game(self):
        """Restart the game by resetting all variables."""
        self.final_score_label.pack_forget()
        self.restart_button.pack_forget()
        self.start_button.pack(pady=10)


# Create the main window
root = tk.Tk()

# Create the game instance
game = ClickGame(root)

# Run the Tkinter event loop
root.mainloop()
