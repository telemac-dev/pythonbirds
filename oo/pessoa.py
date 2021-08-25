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

    # metodo estatico com uso do decorator @staticmethod
    @staticmethod
    def metodo_estatico():
        return 42

    # metodo de class com uso de decorator @classmethod
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    # chamar do metodo estatico pela class ou pelo objeto
    print(Pessoa.metodo_estatico(), harold.metodo_estatico())
    # chamar do metodo de class pela class ou pelo objeto
    print(Pessoa.nome_e_atributos_de_classe(), harold.nome_e_atributos_de_classe())



