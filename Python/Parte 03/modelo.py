# Arquivo Modelo

class Filme:
    # Método init parâmetros
    def __init__(self, nome, ano, duracao): ##Inicialização de valores, self = proprio object
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):  ##Inicialização de valores
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1

vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} min - Likes: {vingadores.likes}')

B99 = Serie('Brookling 99', 2010, 9)
B99.dar_like()
B99.dar_like()
print(f'Nome: {B99.nome} - Ano: {B99.ano} - Temporadas: {B99.temporadas} - Likes: {B99.likes}')
