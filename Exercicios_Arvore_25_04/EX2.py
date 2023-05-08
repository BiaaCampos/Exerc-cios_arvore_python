# Crie uma árvore para representar a estrutura de arquivos e pastas em um sistema operacional. Cada
# nó pode representar uma pasta ou um arquivo e seus filhos podem representar os arquivos e pastas
# dentro dela. Adicione métodos para adicionar e remover arquivos e pastas, e para exibir a estrutura de
# diretórios.

class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)

class Tree:
    def __init__(self):
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

    def add_node(self, name, is_file=False, parent_name=None):
        node = Node(name, is_file)
        if parent_name is None:
            if self.root is None:
                self.set_root(node)
            else:
                return "A árvore já tem um nó raiz"
        else:
            parent_node = self.get_node(parent_name, self.root)
            if parent_node is not None:
                parent_node.add_child(node)
            else:
                return "Nó pai não encontrado"

    def remove_node(self, name):
        node_to_delete = self.get_node(name, self.root)
        if node_to_delete is not None:
            parent_node = None
            for child in self.root.children:
                if child == node_to_delete:
                    self.root.remove_child(child)
                    return "Nó deletado"
                else:
                    parent_node = self.delete_helper(child, node_to_delete)
                    if parent_node is not None:
                        parent_node.remove_child(node_to_delete)
                        return "Nó deletado"
        else:
            return "Nó não encontrado"

    def print_tree(self, node, level=0):
        print("-" * level + node.name)
        for child in node.children:
            self.print_tree(child, level + 1)

tree = Tree()

# Adicionando nós
tree.add_node("C:/", False)
tree.add_node("Users", False, "C:/")
tree.add_node("Documents", False, "Users")
tree.add_node("Downloads", False, "Users")
tree.add_node("Pictures", False, "Users")
tree.add_node("Desktop", False, "Users")
tree.add_node("work.docx", True, "Documents")
tree.add_node("cat.jpg", True, "Pictures")

# Exibindo a estrutura de diretórios
tree.print_tree(tree.root)

# Removendo um nó
tree.remove_node("Users")

print("")
print("Lista com um nó deletado")
tree.print_tree(tree.root)
