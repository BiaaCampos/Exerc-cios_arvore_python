# 1. Implemente uma árvore para representar a hierarquia de uma empresa. Cada nó pode representar um
# funcionário e seus filhos podem representar seus subordinados diretos. Adicione métodos para
# adicionar e remover funcionários, e para exibir a estrutura hierárquica da empresa.

class Node:
    def __init__(self, name):
        self.name = name
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
    def add_node(self, name, parent_name=None):
        node = Node(name)
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
            
    def remove_node(self, data):
        node_to_delete = self.get_node(data, self.root)
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

# Adicionar os nós
print("Lista completa")
tree.add_node("Gi")
tree.add_node("Bia", "Gi")
tree.add_node("Vi", "Gi")
tree.add_node("Edu", "Bia")
tree.add_node("Gabi", "Bia")
tree.add_node("Julia", "Vi")
tree.add_node("Ana", "Vi")

tree.print_tree(tree.root)

#Removendo um nó
tree.remove_node("Bia")

print("")
print("Lista com um nó deletado")
tree.print_tree(tree.root)
