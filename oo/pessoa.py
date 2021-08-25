class Pessoa:
    # atributo de class
    olhos = 2

    # atributos de instância
    # função dunder init __init__ (para inicialização dos atributo de instância)
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
    # chamar atributo de class
    print(Pessoa.olhos)
    # modificando o atributo de class, ele passa a ser um atributo do objeto
    harold.olhos = 1
    # acesso no atributo de class pelo objeto
    print(harold.olhos)
    print(jordan.olhos)
    print(id(Pessoa.olhos), id(harold.olhos), id(jordan.olhos))
    print(harold.__dict__)
    print(jordan.__dict__)





