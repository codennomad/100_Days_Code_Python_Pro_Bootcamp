from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, ttk, StringVar, Frame
from ttkthemes import ThemedStyle
import random
import string

class Pass(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=20, pady=20)
        
        # Configuração do tema
        self.style = ThemedStyle()
        self.style.set_theme('equilux')
        self.configure(background="#333333")
        
        # Configuração de cores
        self.bg_color = "#333333"
        self.text_color = "white"
        
        # Inicializar dados de senhas
        self.passwords_data = [
            {"website": "exemplo.com", "email": "usuario@email.com", "password": "S3nh@F0rt3!", "hidden": True},
            {"website": "meubanco.com", "email": "meu.nome", "password": "87aZxY!#45", "hidden": True},
            {"website": "redesocial.com", "email": "perfil.user", "password": "P@ssw0rd123", "hidden": True}
        ]
        
        # Criar notebook (sistema de abas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)
        
        # Criar primeira aba (Generate)
        self.tab_generate = Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.tab_generate, text='Generate')
        
        # Criar segunda aba (Passwords)
        self.tab_passwords = Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.tab_passwords, text='Passwords')
        
        # Configurar a aba Generate
        self.setup_generate_tab()
        
        # Configurar a aba Passwords
        self.setup_passwords_tab()
        
        # Estilizar elementos ttk
        self.setup_styles()
    
    def setup_styles(self):
        """Configura todos os estilos dos elementos ttk"""
        self.style.configure("TButton", background="#333333", foreground="white", font=("Helvetica", 10))
        self.style.configure("TLabel", background="#333333", foreground="white", font=("Helvetica", 10))
        self.style.configure("TEntry", fieldbackground="#555555", background="#333333", foreground="white", font=("Helvetica", 10))
        self.style.configure("TNotebook", background="#333333", tabmargins=[2, 5, 2, 0])
        self.style.configure("TNotebook.Tab", background="#555555", foreground="white", padding=[10, 2])
        self.style.map("TNotebook.Tab", background=[("selected", "#666666")])
        self.style.configure("Treeview", 
                             background="#444444", 
                             foreground="white", 
                             fieldbackground="#444444", 
                             font=("Helvetica", 9))
        self.style.map("Treeview", background=[("selected", "#666666")])
    
    def setup_generate_tab(self):
        """Configura a interface da aba Generate"""
        # Canvas com logo
        self.canvas = Canvas(self.tab_generate, width=200, height=200, background=self.bg_color, highlightthickness=0)
        self.canvas.grid(row=0, column=1, pady=(10, 20))
        try:
            self.image = PhotoImage(file="coden.png")
            self.canvas.create_image(100, 100, image=self.image)
        except:
            # Fallback se a imagem não for encontrada
            self.canvas.create_text(100, 100, text="Logo", fill="white", font=("Helvetica", 16))
        
        # Labels
        self.label_website = Label(self.tab_generate, text="Website:", bg=self.bg_color, fg=self.text_color)
        self.label_website.grid(row=1, column=0, sticky="w", pady=5)
        
        self.label_email = Label(self.tab_generate, text="Email/Username:", bg=self.bg_color, fg=self.text_color)
        self.label_email.grid(row=2, column=0, sticky="w", padx=(0, 15), pady=5)
        
        self.label_password = Label(self.tab_generate, text="Password:", bg=self.bg_color, fg=self.text_color)
        self.label_password.grid(row=3, column=0, sticky="w", pady=5)
        
        # Inputs
        self.entry_website = Entry(self.tab_generate, width=35, bg="#555555", fg="white")
        self.entry_website.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)
        self.entry_website.focus()
        
        self.entry_email = Entry(self.tab_generate, width=35, bg="#555555", fg="white")
        self.entry_email.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)
        
        self.entry_password = Entry(self.tab_generate, width=30, bg="#555555", fg="white")
        self.entry_password.grid(row=3, column=1, sticky="w", padx=(0, 15), pady=5)
        
        # Buttons
        self.button_generate = ttk.Button(self.tab_generate, text="Generate Password", 
                                         width=14, command=self.generate_password)
        self.button_generate.grid(row=3, column=2, pady=5)
        
        self.button_add = ttk.Button(self.tab_generate, text="Add", width=36, command=self.add_password)
        self.button_add.grid(row=4, column=1, columnspan=2, sticky="w", pady=10)
    
    def setup_passwords_tab(self):
        """Configura a interface da aba Passwords"""
        # Criar treeview (tabela)
        columns = ('website', 'email', 'password')
        self.tree = ttk.Treeview(self.tab_passwords, columns=columns, show='headings', height=15)
        
        # Definir cabeçalhos
        self.tree.heading('website', text='Website')
        self.tree.heading('email', text='Email/Username')
        self.tree.heading('password', text='Password')
        
        # Definir larguras das colunas
        self.tree.column('website', width=150)
        self.tree.column('email', width=200)
        self.tree.column('password', width=150)
        
        # Vincular evento de clique na tabela
        self.tree.bind('<ButtonRelease-1>', self.handle_click)
        
        # Adicionar scrollbar
        scrollbar = ttk.Scrollbar(self.tab_passwords, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Posicionar elementos
        self.tree.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        scrollbar.pack(side='right', fill='y', pady=10)
        
        # Carregar dados iniciais
        self.load_password_data()
    
    def handle_click(self, event):
        """Gerencia cliques na tabela"""
        # Obter o item selecionado
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return
            
        column = self.tree.identify_column(event.x)
        if column != "#3":  # Coluna da senha (#3 é a terceira coluna)
            return
            
        item = self.tree.focus()
        if not item:
            return
            
        # Obter valores
        item_id = self.tree.index(item)
        if item_id < 0 or item_id >= len(self.passwords_data):
            return
            
        # Alternar visibilidade da senha
        self.passwords_data[item_id]["hidden"] = not self.passwords_data[item_id]["hidden"]
        self.load_password_data()
    
    def generate_password(self):
        """Gera uma senha aleatória e a insere no campo de senha"""
        length = 12
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Limpar campo atual e inserir nova senha
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password)
    
    def add_password(self):
        """Adiciona uma nova senha à lista de senhas"""
        # Obter dados dos campos
        website = self.entry_website.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        # Validação simples
        if not website or not email or not password:
            # Aqui poderia mostrar um aviso
            return
        
        # Adicionar aos dados
        self.passwords_data.append({
            "website": website,
            "email": email,
            "password": password,
            "hidden": True
        })
        
        # Atualizar tabela
        self.load_password_data()
        
        # Limpar campos
        self.entry_website.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_website.focus()
    
    def load_password_data(self):
        """Carrega os dados de senha na tabela"""
        # Limpar tabela atual
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Verificar se há dados para carregar
        if not hasattr(self, 'passwords_data') or not self.passwords_data:
            return
            
        # Recarregar dados
        for data in self.passwords_data:
            password_display = data["password"]
            if data["hidden"]:
                password_display = "•" * len(data["password"])
            
            self.tree.insert('', 'end', values=(
                data["website"],
                data["email"],
                password_display
            ))


if __name__ == "__main__":
    app = Pass()
    app.mainloop()