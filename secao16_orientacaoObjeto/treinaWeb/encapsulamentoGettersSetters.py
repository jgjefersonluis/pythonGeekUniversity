class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

    def desativar(self):
        self.__ativo = False
        print("A pessoa foi desativada com sucesso!")

    def get_nome(self):
        return self.nome

    def set_nome(self):
        self.nome = nome

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456", True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pessoa1.ativo)

    # Utilzando getters e setters
    pessoa1.set_nome("José")
    print(pessoa1.get_nome())
    
