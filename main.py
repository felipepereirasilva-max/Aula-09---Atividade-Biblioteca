from datetime import datetime

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True


class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def devolver_livro(self):
        self.livro.devolver()
        self.data_devolucao = datetime.now()


#  Exemplo de uso
livro1 = Livro(1, "Dom Casmurro", "Machado de Assis")
usuario1 = Usuario(1, "João")

if livro1.emprestar():
    emprestimo1 = Emprestimo(livro1, usuario1)
    print("Livro emprestado!")

# Devolvendo
emprestimo1.devolver_livro()
print("Livro devolvido!")