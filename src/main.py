import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from utils.icon_utils import IconManager
class MenuScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Menu")
        self.root.geometry("500x400")
        
        # Set window icon using our utility
        # IconManager.auto_set_icon(self.root)
        
        
        self.root.resizable(False, False)
        
        
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
       
        self.title_label = ttk.Label(
            self.main_frame, 
            text="🎮 Guess My Car 🎮",
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=30)
        
       
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(expand=True)
        
        # Create buttons
        self.create_buttons()
        
        
        self.status_bar = ttk.Label(
            self.main_frame,
            text="Ready to play!",
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
    
    def create_buttons(self):
        button_style = {'width': 20, 'padding': 10}
        
        buttons = [
            ("▶ PLAY GAME", self.play_game),
            ("⚙ OPTIONS", self.open_options),
            ("ℹ ABOUT", self.show_about),
            ("✖ QUIT", self.quit_game)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(
                self.button_frame,
                text=text,
                command=command,
                **button_style
            )
            btn.pack(pady=5)
    
    def play_game(self):
        self.status_bar.config(text="Starting game...")
        messagebox.showinfo("Play", "Game would start here!")
        self.status_bar.config(text="Game ready!")
    
    def open_options(self):
        self.status_bar.config(text="Opening options...")
        options_window = tk.Toplevel(self.root)
        options_window.title("Options")
        options_window.geometry("300x200")
        
        ttk.Label(options_window, text="Settings", font=("Arial", 14)).pack(pady=10)
        ttk.Label(options_window, text="Volume:").pack()
        ttk.Scale(options_window, from_=0, to=100, orient=tk.HORIZONTAL).pack(pady=5)
        ttk.Button(options_window, text="Save", command=options_window.destroy).pack(pady=10)
        
        self.status_bar.config(text="Options closed")
    
    def show_about(self):
        self.status_bar.config(text="Showing about info...")
        messagebox.showinfo(
            "About", 
            "Guess My Car\nVersion 1.0\n\nCreated with Python and Tkinter!\n© 2024"
        )
        self.status_bar.config(text="About info displayed")
    
    def quit_game(self):
        self.status_bar.config(text="Quitting...")
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.quit()
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuScreen(root)
    root.mainloop()