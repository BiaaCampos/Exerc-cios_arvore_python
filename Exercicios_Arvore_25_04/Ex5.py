# Implemente uma árvore para representar a estrutura de uma organização sem fins lucrativos, com
# cada nó representando um projeto e seus filhos representando as atividades dentro do projeto.
# Adicione métodos para adicionar e remover projetos e atividades, e para exibir a estrutura da
# organização.

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def __str__(self):
        return self.name

class Organizacao_project:
    def __init__(self, name):
        self.root = Node(name)

    def add_project(self, project_name):
        project_node = Node(project_name)
        self.root.add_child(project_node)
        return project_node

    def remove_project(self, project_node):
        self.root.remove_child(project_node)

    def add_atividade(self, project_node, activity_name):
        activity_node = Node(activity_name)
        project_node.add_child(activity_node)
        return activity_node

    def remove_atividade(self, project_node, activity_node):
        project_node.remove_child(activity_node)

    def organizacao_estrutura(self):
        self._display_node(self.root)

    def _display_node(self, node, level=0):
        print('    ' * level + str(node))
        for child in node.children:
            self._display_node(child, level + 1)


org = Organizacao_project("Organize sua vida financeira!")

project1 = org.add_project("Projeto 1")
atividade1_1 = org.add_atividade(project1, "Carteira Digital - 1")
atividade2_2 = org.add_atividade(project1, "Carteira Digital - 2")
atividade3_3 = org.add_atividade(project1, "Carteira Digital - 3")

project2 = org.add_project("Projeto 2")
atividade1_1 = org.add_atividade(project2, "Banco Digital - 1.2")
atividade2_2 = org.add_atividade(project2, "Banco Empresarial - 2.3")
atividade3_3 = org.add_atividade(project2, "Banco Individual - 4.8")

project3 = org.add_project("Projeto 3")
atividade1_1 = org.add_atividade(project3, "Banco Digital - 1")
atividade2_2 = org.add_atividade(project3, "Banco Empresarial - 3")
atividade3_3 = org.add_atividade(project3, "Banco Individual - 4")

org.organizacao_estrutura()


org.remove_project(project2)

print("")
print("Lista com um nó deletado")
org.organizacao_estrutura()
