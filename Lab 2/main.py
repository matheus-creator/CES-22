from library import Library
from interface import Interface

# Chamadas inicias, com admins e contatos configurados manualmente

library = Library()
library.add_library_contact('994719012')
library.add_library_contact('981029382')
library.add_library_admin('victor', 'thisismypassword')
library.add_library_admin('carlos', 'herecomesthesun')
library.add_library_client('matheus', 'matheus@gmail.com')
library.add_library_book('a casa de papel', ['marcos', 'marcos@gmail'], 'terror', '2', 'sao paulo', 120, 150)

interface = Interface(library)
interface.show_initial_interface()