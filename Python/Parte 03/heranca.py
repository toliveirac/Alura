# Classe mãe, que contem os atributos comuns as classes Filmes e Séries
class Programa:
    # Método init parâmetros
    def __init__(self, nome, ano): ##Inicialização de valores, self = proprio object
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

class Filme(Programa):
    # Método init parâmetros
    def __init__(self, nome, ano, duracao): ##Inicialização de valores, self = proprio object
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):    
    # Método init parâmetros
    def __init__(self, nome, ano, temporadas):  ##Inicialização de valores
        super().__init__(nome, ano) # chama parâmetros da classe mãe
        self.temporadas = temporadas


## Criando objetos 

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} min - Likes: {vingadores.likes}')

B99 = Serie('Brookling 99', 2010, 9)
B99.dar_like()
B99.dar_like()
print(f'Nome: {B99.nome} - Ano: {B99.ano} - Temporadas: {B99.temporadas} - Likes: {B99.likes}')
