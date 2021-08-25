class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    jordan = Pessoa(nome='Jordan', idade=12)
    harold = Pessoa(jordan, nome='Harold', idade=50)
    print(Pessoa.comprimentar(harold))
    print(id(harold))
    print(harold.comprimentar())
    print(harold.nome)
    print((harold.idade))
    for filho in harold.filhos:
        print(filho.nome)
    # Criar atributos dinãmico
    harold.sobrenome = 'Gautschi'
    # Apagar um atributo
    del jordan.filhos
    # Mostrar os atributos de instancia objeto.__dict__
    print(harold.__dict__)
    print(jordan.__dict__)





