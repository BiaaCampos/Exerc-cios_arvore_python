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

    def exibir_capitulo(self, depth=0):
        print(" " * depth + self.title)
        for child in self.children:
            child.exibir_capitulo(depth + 2)

    def remove_chapter(self, title):
        for child in self.children:
            if child.title == title:
                self.children.remove(child)
                child.parent = None
                return True
            else:
                if child.remove_chapter(title):
                    return True
        return False

    def remove_section(self, title):
        for child in self.children:
            if child.title == title:
                self.children.remove(child)
                child.parent = None
                return True
        return False



book = Node("O Mistério da Ilha Perdida")

capitulo1 = book.add_child("O Desaparecimento")
capitulo1.add_child("1 - A Aventura Começa")
capitulo1.add_child("1.2 - O Mapa Enigmático")

capitulo2 = book.add_child("Na Busca da Ilha")
capitulo2.add_child("2 - O Naufrágio")
capitulo2.add_child("2.2 - A Descoberta da Ilha")

capitulo3 = book.add_child("Os Segredos da Ilha")
capitulo3.add_child("3 - A Caverna Misteriosa")
capitulo3.add_child("3.2 - O Encontro com os Habitantes da Ilha")

capitulo4 = book.add_child("O Conflito")
capitulo4.add_child("4 - O Ataque Surpresa")
capitulo4.add_child("4.2 - A Luta pela Sobrevivência")

capitulo5 = book.add_child("O Mistério Revelado")
capitulo5.add_child("5 - A Descoberta do Tesouro")
capitulo5.add_child("5.2 - A Fuga da Ilha")

print("Lista completa:")
print("")

book.exibir_capitulo()

# Remove um capitulo
book.remove_chapter("O Conflito")

# Remove uma seção:
capitulo1.remove_section("1.2 - O Mapa Enigmático")

print("")
print("Lista com um nó deletado:")
print("")
book.exibir_capitulo()




 