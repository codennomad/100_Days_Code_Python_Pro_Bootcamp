from tkinter import Tk, Canvas, PhotoImage

class Pass(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=20, pady=20)
        
        self.canvas = Canvas(self, width =200, height=200)
        self.canvas.pack()
        
        self.image = PhotoImage(file="codennomad2.png")
        
        self.canvas.create_image(100, 100, image=self.image)
        

if __name__ == "__main__":
    app = Pass()
    app.mainloop()