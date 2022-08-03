"""
@property
    def nome(self):
        return self.__nome

    def raca(self):
        return self.__raca

    def cor(self):
        return self.__cor

    def respondida(self):
        return self.__respondida

        cao = Cachorro('fabio','vira-lata','branco')
        print(f'O {this.nome} é um {this.raca} {this.cor}')

        class Cachorro:

    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.respondida = False

        class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

usuario = Acesso('fabinho@gmail.com', '1203456')
print(usuario.mostra_senha())
cao = Cachorro('fabio', 'vira-lata', 'branca')
print(f'O nome é {cao.nome}, da raça {cao.raca}, cor {cao.cor}')

print(usuario.email)
print(cao.nome)
print(cao)
print(usuario)
print(dir(usuario))
"""

class Questao:
        alternativas = [0,1]
        def __init__(self, id, numero, enunciado, figura, alternativas):
            self.id = id #Questao.resolvidas
            self.__numero = numero
            self.enunciado = enunciado
            self.figura = figura
            self.alternativas = {0:'certo',1:'errado'}
            self.respondida = False
        def apresenta_questao(self):
            return f'{self.__numero} - {self.enunciado} /n {self.alternativas}'

q1 = Questao(1, 1,'O que é blue?', '', 0)
print(q1.apresenta_questao())
print(type(Questao.alternativas))
print(q1.__dict__)
