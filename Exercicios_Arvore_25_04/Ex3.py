# Implemente uma árvore de decisão para classificar diferentes tipos de flores com base em suas
# características, como cor, tamanho e aroma. Adicione métodos para inserir novas flores na árvore,
# percorrer a árvore para classificar novas flores e exibir a estrutura da árvore.|

class Flor:
    def __init__(self, cor, tamanho, aroma):
        self.cor = cor
        self.tamanho = tamanho
        self.aroma = aroma


class No:
    def __init__(self, caracteristica, filhos, classificacao):
        self.caracteristica = caracteristica
        self.filhos = filhos
        self.classificacao = classificacao


class Arvore_classificacao:
    def __init__(self):
        self.raiz = None

    def inserir_flor(self, flor, classificacao):
        if self.raiz is None:
            self.raiz = No('cor', {}, None)
        no_atual = self.raiz
        while True:
            if flor.cor not in no_atual.filhos:
                no_atual.filhos[flor.cor] = No('tamanho', {}, None)
            no_atual = no_atual.filhos[flor.cor]
            if flor.tamanho not in no_atual.filhos:
                no_atual.filhos[flor.tamanho] = No('aroma', {}, None)
            no_atual = no_atual.filhos[flor.tamanho]
            if flor.aroma not in no_atual.filhos:
                no_atual.filhos[flor.aroma] = No(None, {}, classificacao)
                return

    def classificar_flor(self, flor):
        no_atual = self.raiz
        while no_atual.filhos:
            if flor.cor not in no_atual.filhos:
                return None
            no_atual = no_atual.filhos[flor.cor]
            if flor.tamanho not in no_atual.filhos:
                return None
            no_atual = no_atual.filhos[flor.tamanho]
            if flor.aroma not in no_atual.filhos:
                return None
            no_atual = no_atual.filhos[flor.aroma]
        return no_atual.classificacao

    def exibir_arvore(self, no=None, profundidade=0):
        if no is None:
            no = self.raiz
        print(' ' * profundidade, end='')
        if no.caracteristica is None:
            print('Classificação:', no.classificacao)
        for valor, filho in no.filhos.items():
            print(' ' * profundidade, end='')
            print(valor)
            self.exibir_arvore(filho, profundidade + 2)
        return

arvore = Arvore_classificacao()

arvore.inserir_flor(Flor('vermelho', 'grande', 'doce'), 'rosa')
arvore.inserir_flor(Flor('amarelo', 'pequeno', 'amargo'), 'girassol')
arvore.inserir_flor(Flor('rosa', 'pequeno', 'doce'), 'tulipa')
arvore.inserir_flor(Flor('branca', 'médio', 'adocicada'), 'margarida')

print("")
arvore.exibir_arvore()

