class Node:
    def __init__(self, data):
        self.data = data
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

    def get_node(self, data, current_node):
        if current_node.data == data:
            return current_node
        else:
            for child in current_node.children:
                result = self.get_node(data, child)
                if result is not None:
                    return result

    def add_node(self, data, parent_data=None):
        node = Node(data)
        if parent_data is None:
            if self.root is None:
                self.set_root(node)
            else:
                return "A árvore já tem um nó raiz"
        else:
            parent_node = self.get_node(parent_data, self.root)
            if parent_node is not None:
                parent_node.add_child(node)
            else:
                return "Nó pai não encontrado"

    def delete_node(self, data):
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

    def delete_helper(self, node, node_to_delete):
        if node == node_to_delete:
            return node
        else:
            for child in node.children:
                result = self.delete_helper(child, node_to_delete)
                if result is not None:
                    return result

    def update_node(self, data, new_data):
        node_to_update = self.get_node(data, self.root)
        if node_to_update is not None:
            node_to_update.data = new_data
            return "Nó atualizado"
        else:
            return "Nó não encontrado"

    def print_tree(self, node, level=0):
        if node is not None:
            print("  "*level + str(node.data))
            for child in node.children:
                self.print_tree(child, level+1)




tree = Tree()

# Adicionando nós
tree.add_node("A")
tree.add_node("B", "A")
tree.add_node("C", "A")
tree.add_node("D", "B")
tree.add_node("E", "B")

# Exibindo a árvore
tree.print_tree(tree.root)

# Atualizando um nó
tree.update_node("C", "F")

# Excluindo um nó
tree.delete_node('C')

# Exibindo a árvore atualizada
tree.print_tree(tree.root)



