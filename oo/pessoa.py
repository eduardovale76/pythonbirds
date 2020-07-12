class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade =35):
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'ola {id(eduardo)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    rafael = Pessoa(nome='Rafael', idade=7)
    eduardo = Pessoa(rafael, nome='Eduardo', idade=44)
    print(Pessoa.cumprimentar(eduardo))
    print(rafael.cumprimentar())
    print(rafael.nome, rafael.idade)
    print(eduardo.nome, eduardo.idade)
    for filho in eduardo.filhos:
        print(f'{filho.nome} é filho de {eduardo.nome}')
    eduardo.olhos = 4
    print(eduardo.olhos)
    del eduardo.olhos
    print(eduardo.olhos)
    print(rafael.olhos)
    print(Pessoa.olhos)
    rafael.sobrenome = 'Vale'
    print(rafael.sobrenome)
    print(eduardo.__dict__)
    print(rafael.__dict__)
    print(f'{Pessoa.metodo_estatico(), eduardo.metodo_estatico()}')
    print(f'{Pessoa.nome_e_atributo_de_classe(), eduardo.nome_e_atributo_de_classe()}')