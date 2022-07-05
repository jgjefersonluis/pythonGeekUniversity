'''o time de desenvolvimento criou as Properties
para prover um meio mais “elegante” para obter e enviar
novos dados aos atributos de uma classe:'''

class Pessoa:
    def __int__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

    def desativar(self):
        self.__ativo = False
        print("A pessoa foi desativada com sucesso!")

        def get_nome(self):
            return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456", True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pessoa1.ativo)

    #Utilizando properties
    pessoa1.nome = "José"
    print(pessoa1.nome)
