import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(500,300)

my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")




window.mainloop()