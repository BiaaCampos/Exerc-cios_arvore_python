# 4. Crie uma árvore para representar a estrutura de um livro, com cada nó representando um capítulo e
# seus filhos representando as seções dentro do capítulo. Adicione métodos para adicionar e remover
# capítulos e seções, e para exibir a estrutura do livro.

class Node:
    def __init__(self, title, parent=None):
        self.title = title
        self.parent = parent
        self.children = []

    def add_child(self, title):
        child = Node(title, self)
        self.children.append(child)
        return child

    def remove_child(self, node):
        self.children.remove(node)
        node.parent = None

    def exibir_book(self, depth=0):
        print(" " * depth + self.title)
        for child in self.children:
            child.exibir_book(depth + 2)



book = Node("As Aventuras de João e Maria")

chapter1 = book.add_child("O Começo da Aventura")
chapter1.add_child("O Encontro com a Bruxa")
chapter1.add_child("A Fuga da Casa de Doces")

chapter2 = book.add_child("Na Floresta Escura")
chapter2.add_child("O Encontro com o Lobo")
chapter2.add_child("A Ajuda da Fada")

chapter3 = book.add_child("O Resgate do Rei")
chapter3.add_child("A Batalha Final")
chapter3.add_child("O Retorno para Casa")


book.exibir_book()



