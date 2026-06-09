
def projetos_extensao(estado):
    estado["satisfacao"] += 10
    estado["qualidade"] += 5
    estado["dinheiro"] -= 5000
    estado["reputacao"] += 10

    print("\nProjetos de extensão foram ampliados!")


def mostrar_reputacao(estado):
    print(f"A reputação da universidade é: {estado['reputacao']}") 