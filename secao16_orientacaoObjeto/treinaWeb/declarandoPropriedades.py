class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.__ativo =  ativo

    def desativar(self):
        self.__ativo = False
        print("A pessoa foi desativada com sucesso!")

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456", True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pesseoa1.ativo)