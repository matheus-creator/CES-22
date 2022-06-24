import tkinter as tk
from tkinter import ttk

# Database

IDS = []
USERNAMES = []
PASSWORDS = []
NAMES = []
EMAILS = []
ADDRESSES = []
NUMBERS = []

# Global variables

current_frame = 0
current_id = 0

class Participant:
    '''
    Class that contains methods for checking user credentials and registering them.
    '''
    @staticmethod
    def registerParticipant(username, password, name, email, address, number):
        '''
        Register an user on database.
        '''
        global current_id
        IDS.append(current_id)
        USERNAMES.append(username)
        PASSWORDS.append(password)
        NAMES.append(name)
        EMAILS.append(email)
        ADDRESSES.append(address)
        NUMBERS.append(number)

    
    @staticmethod
    def checkCredentials(username, password):
        '''
        Check login credentials.
        '''
        found = USERNAMES.count(username)
        if found != 0:
            index = USERNAMES.index(username)
            if PASSWORDS[index] == password:
                return True
        
        return False


    @staticmethod
    def checkRegisterData(username, email):
        '''
        Check for conflicts on database in registering.
        '''
        return USERNAMES.count(username) or EMAILS.count(email)


class InitialFrame(ttk.Frame):
    '''
    Class that represents the initial page of the program.
    '''
    def __init__(self, container, control):
        super().__init__(container)
        self.control = control

        s = ttk.Style()
        s.configure('my.TButton', font=('Segoe UI', 12))

        welcomeMessage = ttk.Label(self, text='Bem vindo ao Leilão!', font=('Segoe UI', 14))
        welcomeMessage.grid(column=0, row=0, padx=5, pady=10)

        help = ttk.Label(self, text='Selecione uma das opções abaixo para continuar', font=('Segoe UI', 12))
        help.grid(column=0, row=1, padx=5, pady=10)

        buttonLogin = ttk.Button(self, text='Entrar', command=self.goToLogin, style='my.TButton')
        buttonLogin.grid(column=0, row=2, padx=5, pady=20, ipadx=20, ipady=10)

        buttonSignUp = ttk.Button(self, text='Registrar', command=self.goToSignUp, style='my.TButton')
        buttonSignUp.config()
        buttonSignUp.grid(column=0, row=3, padx=5, pady=20, ipadx=20, ipady=10)

        self.grid(column=0, row=0, padx=5, pady=5)

    
    def goToLogin(self):
        '''
        Go to login page.
        '''
        global current_frame
        current_frame = 1
        self.control.change_frame()


    def goToSignUp(self):
        '''
        Go to sign up page.
        '''
        global current_frame
        current_frame = 2
        self.control.change_frame()


class LoginFrame(ttk.Frame):
    '''
    Class that represents the login page.
    '''
    def __init__(self, container, control):
        super().__init__(container)
        self.control = control
        self.validate = Participant.checkCredentials

        s = ttk.Style()
        s.configure('my.TButton', font=('Segoe UI', 12))

        self.message = ttk.Label(self)
        self.message.grid(column=0, row=5, padx=5, pady=5)

        login = ttk.Label(self, text='Usuário', font=('Segoe UI', 12))
        login.grid(column=0, row=0, padx=5, pady=5)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        usernameField = ttk.Entry(self, textvariable=self.username, font=('Segoe UI', 12))
        usernameField.grid(column=0, row=1, padx=5, pady=5)

        login = ttk.Label(self, text='Senha', font=('Segoe UI', 12))
        login.grid(column=0, row=2, padx=5, pady=5)

        passField = ttk.Entry(self, textvariable=self.password, show='*', font=('Segoe UI', 12))
        passField.grid(column=0, row=3, padx=5, pady=5)

        buttonLogin = ttk.Button(self, text='Entrar', command=self.validateCredentials, style='my.TButton')
        buttonLogin.grid(column=0, row=4, padx=5, pady=20, ipadx=20, ipady=10)

        signupMessage = ttk.Label(self, text='Não possui conta?', font=('Segoe UI', 12))
        signupMessage.grid(column=0, row=6, padx=5, pady=25)

        buttonSignUp = ttk.Button(self, text='Registrar', command=self.goToSignUp, style='my.TButton')
        buttonSignUp.grid(column=0, row=7, padx=5, pady=0, ipadx=20, ipady=10)

        self.grid(column=0, row=0, padx=5, pady=5)


    def goToSignUp(self):
        '''
        Go to sign up page.
        '''
        global current_frame
        current_frame = 2
        self.control.change_frame()


    def validateCredentials(self):
        '''
        Validate login credentials.
        '''
        self.message.destroy()

        username = self.username.get()
        password = self.password.get()

        if self.validate(username, password):
            response = 'Bem-vindo ' + username + '!'
        else:
            response = 'Credenciais inválidas.'

        self.message = ttk.Label(self, text=response)
        self.message.grid(column=0, row=5, padx=5, pady=5)


class SignUpFrame(ttk.Frame):
    '''
    Class that represents the sign up page.
    '''
    def __init__(self, container, control):
        super().__init__(container)
        self.control = control
        self.register = Participant.registerParticipant
        self.validate = Participant.checkRegisterData

        s = ttk.Style()
        s.configure('my.TButton', font=('Segoe UI', 12))

        self.message = ttk.Label(self)
        self.message.grid(column=0, row=14, padx=5, pady=5)

        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.address = tk.StringVar()
        self.number = tk.StringVar()

        name = ttk.Label(self, text='Nome', font=('Segoe UI', 12))
        name.grid(column=0, row=0, padx=5, pady=5)

        nameField = ttk.Entry(self, textvariable=self.name, font=('Segoe UI', 12))
        nameField.grid(column=0, row=1, padx=5, pady=5)

        email = ttk.Label(self, text='Email', font=('Segoe UI', 12))
        email.grid(column=0, row=3, padx=5, pady=5)

        emailField = ttk.Entry(self, textvariable=self.email, font=('Segoe UI', 12))
        emailField.grid(column=0, row=4, padx=5, pady=5)

        username = ttk.Label(self, text='Nome de usuário', font=('Segoe UI', 12))
        username.grid(column=0, row=5, padx=5, pady=5)

        usernameField = ttk.Entry(self, textvariable=self.username, font=('Segoe UI', 12))
        usernameField.grid(column=0, row=6, padx=5, pady=5)

        password = ttk.Label(self, text='Senha', font=('Segoe UI', 12))
        password.grid(column=0, row=7, padx=5, pady=5)

        passwordField = ttk.Entry(self, textvariable=self.password, font=('Segoe UI', 12), show='*')
        passwordField.grid(column=0, row=8, padx=5, pady=5)

        address = ttk.Label(self, text='Endereço', font=('Segoe UI', 12))
        address.grid(column=0, row=9, padx=5, pady=5)

        addressField = ttk.Entry(self, textvariable=self.address, font=('Segoe UI', 12))
        addressField.grid(column=0, row=10, padx=5, pady=5)

        number = ttk.Label(self, text='Número', font=('Segoe UI', 12))
        number.grid(column=0, row=11, padx=5, pady=5)

        numberField = ttk.Entry(self, textvariable=self.number, font=('Segoe UI', 12))
        numberField.grid(column=0, row=12, padx=5, pady=5)
        
        buttonSignUp = ttk.Button(self, text='Cadastrar', command=self.registerUser, style='my.TButton')
        buttonSignUp.grid(column=0, row=13, padx=5, pady=25, ipadx=20, ipady=10)

        signupMessage = ttk.Label(self, text='Já possui conta?', font=('Segoe UI', 12))
        signupMessage.grid(column=0, row=15, padx=5, pady=10)

        buttonLogin = ttk.Button(self, text='Entrar', command=self.goToLogin, style='my.TButton')
        buttonLogin.grid(column=0, row=16, padx=5, pady=0, ipadx=20, ipady=10)

        self.grid(column=0, row=0, padx=5, pady=5)


    def goToLogin(self):
        '''
        Go to login page.
        '''
        global current_frame
        current_frame = 1
        self.control.change_frame()
    
    def registerUser(self):
        '''
        Register an user.
        '''
        global current_id
        self.message.destroy()

        name = self.name.get()
        email = self.email.get()
        username = self.username.get()
        password = self.password.get()
        address = self.address.get()
        number = self.number.get()

        if self.validate(username, email):
            response = 'Usuário ou email já existe.'
        else:
            self.register(username, password, name, email, address, number)
            current_id += 1
            response = 'Você foi cadastrado!'

        self.message = ttk.Label(self, text=response)
        self.message.grid(column=0, row=14, padx=5, pady=5)


class ControlFrame(ttk.LabelFrame):
    '''
    Class to control which page will be shown.
    '''
    def __init__(self, container):
        super().__init__(container)

        self.container = container

        self.frame = InitialFrame(container, self)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.change_frame()
    
    def change_frame(self):
        '''
        Switch pages.
        '''
        global current_frame
        self.frame.destroy()

        if current_frame == 0:
            self.frame = InitialFrame(self.container, self)
        elif current_frame == 1:
            self.frame = LoginFrame(self.container, self)
        else:
            self.frame = SignUpFrame(self.container, self)

        self.frame.tkraise()


class App(tk.Tk):
    '''
    Class that represents the root page, i.e., the default screen.
    '''
    def __init__(self):
        super().__init__()

        window_width = 600
        window_height = 700

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)

        self.title('Portal do participante')
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

# Initialize program

app = App()
ControlFrame(app)
app.mainloop()