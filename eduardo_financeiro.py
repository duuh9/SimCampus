
def reduzir_gastos(estado):
    estado["dinheiro"] += 10000
    estado["satisfacao"] -= 10
    estado["infraestrutura"] = max(0, estado["infraestrutura"] - 5)

    print("\nOs gastos da universidade foram reduzidos.")


def mostrar_dinheiro():
    print("O caixa da universidade aumentou.") 