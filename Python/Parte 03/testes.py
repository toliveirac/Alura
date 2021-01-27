class dadosCliente:
    # Atributos de Classe
    tamanho_CPF = 11

    # Atributos de instancias
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

Aluno1 = dadosCliente('Thais', 25, 42891225821)
print(dadosCliente.tamanho_CPF)


class programa:
    def __init__(self, nome, ano):
        self._meuNome = nome
        self.ano = ano

    @property
    def meuNome(self):
        return self._meuNome.title() 

    def __str__(self):
        return f'Meu nome é Thais'

class serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self.temporadas} temporadas')

class filme(programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self.duracao} min')  

el_Dorado = filme('O Caminho para el-dorado', 2002, 90)
B99 = serie('Brookling Nine Nine', 2012, 7)

list_filmes_series = [el_Dorado, B99]

for prog in list_filmes_series:
    prog.imprime()


    # Verificando se existe atributo com o nome duração ou temporadas em cada objeto
    #detalhe = programa.temporadas if hasattr(programa, 'temporadas') else programa.duracao
    #print(f'{programa.nome} - {programa.ano} - {detalhe}')


