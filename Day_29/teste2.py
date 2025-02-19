import sqlite3
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, ttk, StringVar, Frame
from ttkthemes import ThemedStyle
import random
import string

class Pass(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=20, pady=20)
        
        self.style = ThemedStyle()
        self.style.set_theme('equilux')
        self.configure(background="#333333")
        
        self.db_connection = sqlite3.connect("passwords.db")
        self.cursor = self.db_connection.cursor()
        self.create_table()
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)
        
        self.tab_generate = Frame(self.notebook, bg="#333333")
        self.notebook.add(self.tab_generate, text='Generate')
        
        self.tab_passwords = Frame(self.notebook, bg="#333333")
        self.notebook.add(self.tab_passwords, text='Passwords')
        
        self.setup_generate_tab()
        self.setup_passwords_tab()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                website TEXT NOT NULL,
                                email TEXT NOT NULL,
                                password TEXT NOT NULL)''')
        self.db_connection.commit()
    
    def setup_generate_tab(self):
        Label(self.tab_generate, text="Website:", bg="#333333", fg="white").grid(row=0, column=0, pady=5)
        self.entry_website = Entry(self.tab_generate, width=35)
        self.entry_website.grid(row=0, column=1, pady=5)
        
        Label(self.tab_generate, text="Email:", bg="#333333", fg="white").grid(row=1, column=0, pady=5)
        self.entry_email = Entry(self.tab_generate, width=35)
        self.entry_email.grid(row=1, column=1, pady=5)
        
        Label(self.tab_generate, text="Password:", bg="#333333", fg="white").grid(row=2, column=0, pady=5)
        self.entry_password = Entry(self.tab_generate, width=30)
        self.entry_password.grid(row=2, column=1, pady=5)
        
        Button(self.tab_generate, text="Generate", command=self.generate_password).grid(row=2, column=2)
        Button(self.tab_generate, text="Add", command=self.add_password).grid(row=3, column=1, pady=10)
    
    def setup_passwords_tab(self):
        columns = ('website', 'email', 'password')
        self.tree = ttk.Treeview(self.tab_passwords, columns=columns, show='headings', height=15)
        
        self.tree.heading('website', text='Website')
        self.tree.heading('email', text='Email/Username')
        self.tree.heading('password', text='Password')
        
        self.tree.column('website', width=150)
        self.tree.column('email', width=200)
        self.tree.column('password', width=150)
        
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)
        self.load_password_data()
    
    def generate_password(self):
        length = 12
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(random.choice(chars) for _ in range(length))
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password)
    
    def add_password(self):
        website = self.entry_website.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if website and email and password:
            self.cursor.execute("INSERT INTO passwords (website, email, password) VALUES (?, ?, ?)", (website, email, password))
            self.db_connection.commit()
            self.load_password_data()
            self.entry_website.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            self.entry_password.delete(0, 'end')
    
    def load_password_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.cursor.execute("SELECT website, email, password FROM passwords")
        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    app = Pass()
    app.mainloop()