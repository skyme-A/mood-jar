import tkinter as tk
import random

# --- Data: Quotes & Themes ---
NOTES = [
    ("Take a deep breath, you are doing amazing! 🌸", "💖"),
    ("Late-night coding magic is real, but don't forget to hydrate! 💧", "✨"),
    ("Time for a cozy break and a warm cup of coffee ☕", "🫧"),
    ("Small steady progress beats perfection every time 🌷", "🍀"),
    ("Sending you warm hugs and 100% sparkling vibes! 🎀", "🥰"),
    ("Drop your shoulders, relax your jaw, and smile! 🧸", "🌟")
]

THEMES = [
    {"bg": "#FFF0F5", "card": "#FFE4E1", "accent": "#D1527A", "btn": "#FFB6C1", "btn_hover": "#FF69B4"},  # Rose Mist
    {"bg": "#F4F0FF", "card": "#EAE4F8", "accent": "#8A64D0", "btn": "#C7B2E8", "btn_hover": "#A27CE6"},  # Lavender
    {"bg": "#F0FFF0", "card": "#E2F6E2", "accent": "#438A5E", "btn": "#A3E4B8", "btn_hover": "#6AC98A"},  # Mint Matcha
    {"bg": "#FFF9E6", "card": "#FFF0C2", "accent": "#C98A2C", "btn": "#FFE28A", "btn_hover": "#F5C84C"}   # Warm Honey
]

class CuteJarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pocket Sunshine 🌸")
        self.root.geometry("340x450")
        self.root.resizable(False, False)

        self.current_theme = THEMES[0]
        self.root.configure(bg=self.current_theme["bg"])

        self.setup_ui()

    def setup_ui(self):
        self.title_lbl = tk.Label(
            self.root,
            text="✨ Daily Sunshine Jar ✨",
            font=("Comic Sans MS", 15, "bold"),
            bg=self.current_theme["bg"],
            fg=self.current_theme["accent"]
        )
        self.title_lbl.pack(pady=15)

        # Rounded-feeling card container
        self.card = tk.Frame(
            self.root, 
            bg=self.current_theme["card"], 
            padx=20, 
            pady=20,
            highlightbackground=self.current_theme["accent"],
            highlightthickness=1
        )
        self.card.pack(padx=25, fill="both", expand=True)

        self.icon_lbl = tk.Label(
            self.card,
            text="🌸",
            font=("Arial", 50),
            bg=self.current_theme["card"]
        )
        self.icon_lbl.pack(pady=10)

        self.text_lbl = tk.Label(
            self.card,
            text="Tap below to reveal a sweet little reminder! (｡♥‿♥｡)",
            font=("Comic Sans MS", 11),
            bg=self.current_theme["card"],
            fg="#4A4A4A",
            wraplength=230,
            justify="center"
        )
        self.text_lbl.pack(pady=10)

        # Action Button with hover & click feel
        self.btn = tk.Button(
            self.root,
            text="Open Note 💖",
            font=("Comic Sans MS", 11, "bold"),
            bg=self.current_theme["btn"],
            fg="white",
            activebackground=self.current_theme["btn_hover"],
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=18,
            pady=9,
            command=self.show_new_note
        )
        self.btn.pack(pady=20)

    def show_new_note(self):
        text, icon = random.choice(NOTES)
        self.current_theme = random.choice(THEMES)

        # Smooth theme transitions
        self.root.configure(bg=self.current_theme["bg"])
        self.title_lbl.configure(bg=self.current_theme["bg"], fg=self.current_theme["accent"])
        self.card.configure(
            bg=self.current_theme["card"],
            highlightbackground=self.current_theme["accent"]
        )
        self.icon_lbl.configure(text=icon, bg=self.current_theme["card"])
        self.text_lbl.configure(text=text, bg=self.current_theme["card"])
        self.btn.configure(
            bg=self.current_theme["btn"],
            activebackground=self.current_theme["btn_hover"]
        )

if __name__ == "__main__":
    window = tk.Tk()
    app = CuteJarApp(window)
    window.mainloop()