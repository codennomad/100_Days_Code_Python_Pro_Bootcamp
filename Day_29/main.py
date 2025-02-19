from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, ttk
from ttkthemes import ThemedStyle

class Pass(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=50, pady=50)
        
        self.style = ThemedStyle()
        self.style.set_theme('equilux')
        self.configure(background="#333333")
        
        self.bg_color = "#333333"
        self.text_color = "white"
        
        
        #Canva
        self.canvas = Canvas(self, width =200, height=200, background="#333333", highlightthickness=0)
        self.canvas.grid(row=0, column=1)
        self.image = PhotoImage(file="coden.png")
        self.canvas.create_image(100, 100, image=self.image)
        
        
        #Label
        self.label_website = Label(self, text="Website:", bg=self.bg_color, fg=self.text_color)
        self.label_website.grid(row=1, column=0, sticky="w")
        
        self.label_email = Label(self, text="Email/Username:", bg=self.bg_color, fg=self.text_color)
        self.label_email.grid(row=2, column=0, sticky="w", padx=(0, 15))
        
        self.label_password = Label(self, text="Password:", bg=self.bg_color, fg=self.text_color)
        self.label_password.grid(row=3, column=0, sticky="w")
        
        
        #Inputs
        self.entry_website = Entry(self, width=35)
        self.entry_website.grid(row=1, column=1, columnspan=2, sticky="w")
        self.entry_website.focus()
        
        self.entry_email = Entry(self, width=35)
        self.entry_email.grid(row=2, column=1, columnspan=2, sticky="w")
        
        self.entry_password = Entry(self, width=30)
        self.entry_password.grid(row=3, column=1, sticky="w", padx=(0, 15))
        
        
        #Button
        self.button_generate = ttk.Button(self, text="Generate", width=16)
        self.button_generate.grid(row=3, column=2)
        
        self.button_add = ttk.Button(self, text="Add", width=36)
        self.button_add.grid(row=4, column=1, columnspan=2, sticky="w")
        
        
        #Theme
        self.style.configure("TButton", background="#333333", foreground="white", font=("Helvetica", 10))
        self.style.configure("TLabel", background="#333333", foreground="white", font=("Helvetica", 10))
        self.style.configure("TEntry", fieldbackground="#555555", background="#333333", foreground="white", font=("Helvetica", 10))
        


if __name__ == "__main__":
    app = Pass()
    app.mainloop()