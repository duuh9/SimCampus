def investir_infraestrutura(estado):
    if estado["dinheiro"] < 20000:
        print("\nDinheiro insuficiente!")
        return

    estado["infraestrutura"] += 15
    estado["dinheiro"] -= 20000
    estado["satisfacao"] += 5
    estado["reputacao"] += 15

    print("\nVocê investiu em infraestrutura!")


def mostrar_infraestrutura(estado):
    print(f"\nInfraestrutura: {estado['infraestrutura']}")