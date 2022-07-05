''' as classes representam a estrutura de um elemento no mundo real, ela é apenas o modelo destes elementos.
Sempre que precisamos criar “algo” com base em uma classe, dizemos que estamos “instanciando objetos”.
O ato de instanciar um objeto significa que estamos criando a representação de uma classe em nosso programa.
Para instanciar um objeto no Python com base em uma classe previamente declarada,
basta indicar a classe que desejamos utilizar como base, informar os valores referentes aos seus atributos. '''

class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456")
    print(pessoa1.nome)
    



