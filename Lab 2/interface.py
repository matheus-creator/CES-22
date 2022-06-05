class Interface:
    '''
    Class that cares about the terminal interface of the library.
    '''
    def __init__(self, library):
        self.type = ''
        self.client = True
        self.options = ''
        self.library = library
        self.current_item = ''
        self.current_item_value = None

    def loop_interface(self, options, next_functions):
        self.options = ''

        for i in range(len(options)):
            self.options += '[' + str(i+1) + '] ' + options[i] + '    '

        loop_options = eval(input(self.options + '\n\nSua opção: ')) - 1
        while(loop_options not in range(len(options))):
            print('Opção inválida. Tente novamente.\n')
            loop_options = eval(input(self.options + '\n\nSua opção: ')) - 1
        
        self.type = loop_options + 1

        if next_functions[loop_options] != None:
            next_functions[loop_options]()
        

    def show_initial_interface(self):
        print()
        print('*------------------------------------------------------------------------------*\n')
        print('Seja bem-vindo à nossa livraria! Selecione uma das opções abaixo para continuar.\n')
        print('*------------------------------------------------------------------------------*')

        options = ['Consulte nossos produtos', 'Contatos', 'Admnistração']
        next_functions = [self.show_products_interface, self.show_contacts_interface, self.show_login_admin_interface]

        self.loop_interface(options, next_functions)

    def show_products_interface(self):
        print()
        print('Selecione uma das opções de consulta abaixo:')
        print()

        options = ['Título', 'Autor']
        next_functions = [self.show_find_product_by_name_interface, self.show_find_product_by_author_interface]

        self.loop_interface(options, next_functions)
    
    def show_contacts_interface(self):
        contacts = self.library.get_library_contacts()
        print()
        print('----- Nossos contatos -----')
        print()
        for i in contacts:
            print('->', i)
    
    def show_login_admin_interface(self):
        print()
        print('----- Login -----')
        print()
        username = input('Digite o username: ')
        password = input('Digite a senha: ')
        
        if (self.library.check_library_admin(username, password)):
            self.show_admin_interface()
        else:
            print()
            print('Credenciais inválidas.')

    def show_admin_interface(self):
        self.client = False
        print()
        print('*----------------------------------------------------------*\n')
        print('Bem-vindo administrador! Selecione alguma das opções abaixo.\n')
        print('*----------------------------------------------------------*')

        options = ['Livro', 'Cliente']
        next_functions = 2*[self.show_admin_crud_interface]

        self.loop_interface(options, next_functions)

    def show_admin_crud_interface(self):
        print()
        print('Escolha uma das opções abaixo:')
        print()

        options = ['Adicionar', 'Alterar', 'Consultar', 'Remover']

        next_functions = []

        if self.type == 1:
            next_functions = [self.show_admin_add_product, self.show_admin_update_product, self.show_products_interface, self.show_admin_remove_product]
        elif self.type == 2:
            next_functions = [self.show_admin_add_client, self.show_admin_update_client, self.show_admin_find_client, self.show_admin_remove_client]

        self.loop_interface(options, next_functions)

    def show_admin_add_product(self):
        print()
        print('Forneça os dados do livro: ')
        print()
        title = input('Título: ')
        author = input('Autor: ')
        email = input('Email do autor: ')
        genre = input('Gênero: ')
        edition = input('Edição: ')
        publishing_company = input('Editora: ')
        purchase_price = eval(input('Preço de compra: '))
        selling_price = eval(input('Preço de venda: '))

        self.library.add_library_book(title, [author, email], genre, edition, publishing_company, purchase_price, selling_price)

    def show_admin_update_product(self):
        print()        
        title = input('Digite o título: ')
        property = input('Digite a propriedade que gostaria de alterar: ')
        property_value = input('Digite o novo valor: ')
    
    def show_find_product_by_name_interface(self):
        print()
        title = input('Digite o título: ')
        found, price = self.library.find_library_book('title', title) 
        if self.client == True and found == True:
            print()
            print('Comprar?')
            print()
            self.current_item = title
            self.current_item_value = price
            options = ['Sim', 'Não']
            next_functions = [self.show_identification_interface, self.show_keep_buying_interface]

            self.loop_interface(options, next_functions)
    
    def show_identification_interface(self):
        print()
        name = input('Digite seu nome: ')
        found = self.library.find_library_client(name)
        if found:
            print()
            self.library.add_library_client_purchase(name, self.current_item, self.current_item_value)
            self.show_confirmation_interface()

    def show_keep_buying_interface(self):
        print()
        print('Deseja continuar comprando?')
        print()

        options = ['Sim', 'Não']
        next_functions = [self.show_products_interface, None]

        self.loop_interface(options, next_functions)
    
    def show_confirmation_interface(self):
        print('Item comprado!')
        self.show_keep_buying_interface()
    
    def show_find_product_by_author_interface(self):
        print()
        author = input('Digite o autor: ')
        self.library.find_library_book('author', author)    

    def show_admin_remove_product(self):
        print()
        title = input('Digite o título: ')
        self.library.remove_library_book(title)
    
    def show_admin_add_client(self):
        print()
        name = input('Digite o nome do cliente: ')
        email = input('Digite o email do cliente: ')
        self.library.add_library_client(name, email) 
    
    def show_admin_update_client(self):
        print()
        name = input('Digite o nome do cliente: ')
        property = input('Digite a propriedade que gostaria de alterar: ')
        property_value = input('Digite o novo valor: ')
        self.library.update_library_client(name, property, property_value)
    
    def show_admin_find_client(self):
        print()
        name = input('Digite o nome do cliente: ')
        self.library.find_library_client(name)
    
    def show_admin_remove_client(self):
        print()
        name = input('Digite o nome do cliente: ')
        self.library.remove_library_client(name)