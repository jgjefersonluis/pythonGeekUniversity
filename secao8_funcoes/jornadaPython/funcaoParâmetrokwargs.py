def dados_pessoa(**kwargs):
    print(type(kwargs))

    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


dados_pessoa(nome='João', idade=35, carreira='Desenvolvedor Fullstack')

funcoesRetornoDados