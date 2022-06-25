import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# current balance
BALANCE = 150

class Interface:
    '''
    Class that represents a receiver.
    '''
    def checkBalance(self):
        '''
        Check current balance.
        '''
        global BALANCE
        return 'Seu saldo é R$' + str(BALANCE)


    def checkStatement(self, transfered_values):
        '''
        Check statement.
        '''
        response = ''
        for i in range(len(transfered_values)):
            response += str(i+1) + 'ª transferência: R$' + str(transfered_values[i]) + '\n'

        return response


    def makeTransfer(self, transfer):
        '''
        Make a transfer.
        '''
        global BALANCE
        BALANCE -= transfer


class Button:
    '''
    Class that represents a button invoker.
    '''
    def setCommand(self, command):
        '''
        Set button command.
        '''
        self.command = command
    

    def executeCommand(self, args):
        '''
        Execute button command.
        '''
        self.command.execute(args)


class Command:
    '''
    Class that represents a command.
    '''
    def __init__(self, interface):
        self.interface = interface
    
    def execute(self):
        '''
        Execute command.
        '''
        pass


class CommandHistory:
    '''
    Class that represents a command history.
    '''
    def __init__(self):
        self.history = []
        self.string_history = []
    

    def getStringHistory(self):
        '''
        Get history in string format for printing.
        '''
        return self.string_history


    def push(self, command, value):
        '''
        Push data to command history.
        '''
        self.history.append(command)
        if command.name == 'transfer':
            self.string_history.append('Transferência R$' + str(value))
        elif command.name == 'balance':
            self.string_history.append('Consulta de saldo')
        else:
            self.string_history.append('Extrato')


class CheckBalanceCommand(Command):
    '''
    Class that represents a check balance command.
    '''
    def __init__(self, interface):
        super().__init__(interface)
        self.name = 'balance'

    def execute(self, _):
        response = self.interface.checkBalance()
        showinfo('Saldo', response)

class CheckStatementCommand(Command):
    '''
    Class that represents a check statement command.
    '''
    def __init__(self, interface):
        super().__init__(interface)
        self.name = 'statement'
    
    def execute(self, transfered_values):
        response = self.interface.checkStatement(transfered_values)
        showinfo('Extrato', response)


class MakeTransferCommand(Command):
    '''
    Class that represents a make transfer command.
    '''
    def __init__(self, interface):
        super().__init__(interface)
        self.name = 'transfer'

    
    def execute(self, args):
        self.interface.makeTransfer(args)   


class Application(ttk.Frame):
    '''
    Class that represents the application.
    '''
    def __init__(self, container):
        super().__init__(container)
        self.executed_commands = CommandHistory()
        self.commands_var = tk.StringVar(value=self.executed_commands.getStringHistory())

        self.transfer_value = tk.StringVar()
        self.transfered_values = []

        self.interface = Interface()
        self.balance = CheckBalanceCommand(self.interface)
        self.statement = CheckStatementCommand(self.interface)
        self.transfer = MakeTransferCommand(self.interface)

        self.button_1 = Button()
        self.button_1.setCommand(self.balance)
        self.button_2 = Button()
        self.button_2.setCommand(self.statement)
        self.button_3 = Button()
        self.button_3.setCommand(self.transfer)        

    
    def createUI(self):
        '''
        Create UI using Tkinter.
        '''
        initial_text_1 = 'Bem-vindo ao nosso serviço online!'
        initial_text_2 = 'Escolha alguma opção abaixo para continuar.'

        ttk.Label(self, text=initial_text_1, font=('Arial', 12)).grid(column=0, row=0, padx=5, pady=15)
        ttk.Label(self, text=initial_text_2, font=('Arial', 10)).grid(column=0, row=1, padx=5, pady=15)
        ttk.Button(self, text='Consultar saldo', command=lambda: self.executeCommand(1)).grid(column=0, row=2, padx=5, pady=15, ipadx=20, ipady=10)
        ttk.Button(self, text='Extrato', command=lambda: self.executeCommand(2)).grid(column=0, row=3, padx=5, pady=15, ipadx=20, ipady=10)
        ttk.Entry(self, textvariable=self.transfer_value).grid(column=0, row=4, padx=5, pady=15, ipadx=10, ipady=5)
        ttk.Button(self, text='Realizar transferência', command=lambda: self.executeCommand(3)).grid(column=0, row=5, padx=5, pady=0, ipadx=20, ipady=10)


        ttk.Label(self, text='Histórico', font=('Arial', 10)).grid(column=0, row=6, padx=5, pady=25)
        history_frame = ttk.Frame(self)
        history_frame.grid(column=0, row=7, padx=5, pady=0)
        listbox = tk.Listbox(history_frame, listvariable=self.commands_var, height=4, width=25)
        listbox.grid(column=0, row=0, padx=5, pady=0)

        scrollbar = ttk.Scrollbar(history_frame, orient='vertical', command=listbox.yview)
        scrollbar.grid(column=1, row=0, sticky='ns')

        listbox['yscrollcommand'] = scrollbar.set

        self.grid(column=0, row=0, padx=5, pady=5)


    def executeCommand(self, button):
        '''
        Execute a command given a certain button.
        '''
        if button == 1:
            self.button_1.executeCommand(None)
            self.executed_commands.push(self.balance, 0)
        elif button == 2:
            self.button_2.executeCommand(self.transfered_values)
            self.executed_commands.push(self.statement, 0)
        else:
            if (self.transfer_value.get() != '' and float(self.transfer_value.get()) > 0):
                self.transfered_values.append(self.transfer_value.get())
                self.button_3.executeCommand(float(self.transfer_value.get()))
                self.executed_commands.push(self.transfer, self.transfer_value.get())
        self.commands_var = tk.StringVar(value=self.executed_commands.getStringHistory())
        self.transfer_value = tk.StringVar()
        self.createUI()


class Root(tk.Tk):
    '''
    Class that represents the root page, i.e., the default screen.
    '''
    def __init__(self):
        super().__init__()

        window_width = 500
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)

        self.title('Banco')
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)


# Initialize program
root = Root()
app = Application(root)
app.createUI()
root.mainloop()