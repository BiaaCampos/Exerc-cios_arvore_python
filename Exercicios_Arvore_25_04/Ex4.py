# 4. Crie uma árvore para representar a estrutura de um livro, com cada nó representando um capítulo e
# seus filhos representando as seções dentro do capítulo. Adicione métodos para adicionar e remover
# capítulos e seções, e para exibir a estrutura do livro.

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)

class Livro:
    def __init__(self, title):
        self.title = title
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_node(self, name, current_node):
        if current_node.name == name:
            return current_node
        else:
            for child in current_node.children:
                result = self.get_node(name, child)
                if result is not None:
                    return result

    def add_capitulo(self, name, parent_name=None):
        capitulo = Node(name)
        if parent_name is None:
            if self.root is None:
                self.set_root(capitulo)
            else:
                return "O livro já tem um capítulo raiz"
        else:
            parent_node = self.get_node(parent_name, self.root)
            if parent_node is not None:
                parent_node.add_child(capitulo)
            else:
                return "Capítulo pai não encontrado"

    def add_section(self, name, parent_name):
        section = Node(name)
        parent_node = self.get_node(parent_name, self.root)
        if parent_node is not None:
            parent_node.add_child(section)
        else:
            return "Capítulo pai não encontrado"

    def remove_capitulo(self, name):
        capitulo_node = self.get_node(name, self.root)
        if capitulo_node is not None:
            parent_node = self.get_node(name, self.root)
            parent_node.remove_child(capitulo_node)
        else:
            return "Capítulo não encontrado"

    def remove_section(self, name, parent_name):
        parent_node = self.get_node(parent_name, self.root)
        if parent_node is not None:
            section_node = self.get_node(name, parent_node)
            if section_node is not None:
                parent_node.remove_child(section_node)
            else:
                return "Seção não encontrada"
        else:
            return "Capítulo pai não encontrado"

    def print_livro(self, node, level=0):
        if node is not None:
            print("-"*level + str(node.name))
            for child in node.children:
                self.print_livro(child, level+1)


livro = Livro("Biblioteca")

livro.add_capitulo("Livros")
livro.add_capitulo("Capítulo 1")
livro.add_section("Luciana Souza", "Livros")
livro.add_section("Como criar uma fazenda", "Livros")
livro.add_section("Seção 1.1 - Início", "Capítulo 1")
livro.add_section("Seção 1.2 - Desenvolvimento", "Capítulo 1")
livro.add_capitulo("Capítulo 2")
livro.add_section("Seção 2.1 - Final", "Capítulo 2")

livro.print_livro(livro.root)



