class Pessoa:
    def __init__(self, *filhos, nome=None, idade =35):
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'ola {id(eduardo)}'

if __name__ == '__main__':
    rafael = Pessoa(nome='Rafael', idade=7)
    eduardo = Pessoa(rafael, nome='Eduardo', idade=44)
    print(Pessoa.cumprimentar(eduardo))
    print(rafael.cumprimentar())
    print(rafael.nome, rafael.idade)
    print(eduardo.nome, eduardo.idade)
    for filho in eduardo.filhos:
        print(f'{filho.nome} é filho de {eduardo.nome}')
    del eduardo.filhos
    rafael.sobrenome = 'Vale'
    print(rafael.sobrenome)
    print(eduardo.__dict__)
    print(rafael.__dict__)