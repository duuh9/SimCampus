
def contratar_professores(estado):
    estado["qualidade"] += 10
    estado["dinheiro"] -= 15000
    estado["satisfacao"] += 5
    estado["reputacao"] += 10

    print("\nNovos professores foram contratados!")


def mostrar_qualidade(estado):
    print(f"A qualidade do ensino é: {estado['qualidade']}")

    