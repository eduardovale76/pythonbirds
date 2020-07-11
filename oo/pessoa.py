class Pessoa:
    def __init__(self, nome=None, idade =35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'ola {id(p)}'

if __name__ == '__main__':
    p = Pessoa("teste")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Eduardo'
    print(p.nome, p.idade)