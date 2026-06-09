# Importando funções dos outros arquivos
from gustavo_infraestrutura import investir_infraestrutura, mostrar_infraestrutura
from bruno_professores import contratar_professores, mostrar_qualidade
from eduardo_financeiro import reduzir_gastos, mostrar_dinheiro
from gustavo_extensao import projetos_extensao, mostrar_reputacao


estado = {
    "dinheiro": 100000,
    "satisfacao": 70,
    "qualidade": 75,
    "infraestrutura": 60,
    "reputacao": 50
}

opcoes_menu = (
    "Investir em infraestrutura",
    "Contratar novos professores",
    "Reduzir gastos",
    "Aumentar projetos de extensão"
)

historico = []


ciclo = 1
limite_ciclos = 10


def mostrar_estado():
    print("\n===== STATUS DA UNIVERSIDADE =====")
    print(f"Dinheiro: {estado['dinheiro']}")
    print(f"Satisfação dos alunos: {estado['satisfacao']}")
    print(f"Qualidade de ensino: {estado['qualidade']}")
    print(f"Infraestrutura: {estado['infraestrutura']}")
    print(f"Reputação: {estado['reputacao']}")
    print("==================================")


while ciclo <= limite_ciclos:

    print(f"\n=========== CICLO {ciclo} ===========")
    mostrar_estado()

    print("\n===== MENU =====")
    print("1 - Investir em infraestrutura")
    print("2 - Contratar novos professores")
    print("3 - Reduzir gastos")
    print("4 - Aumentar projetos de extensão")
    print("5 - Ver histórico")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    
    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print("Opção inválida! Tente novamente.")
        continue

    
    if opcao == "1":
        investir_infraestrutura(estado)
        mostrar_infraestrutura(estado)
        historico.append(opcoes_menu[0])

    
    elif opcao == "2":
        contratar_professores(estado)
        mostrar_qualidade(estado)
        historico.append(opcoes_menu[1])

    
    elif opcao == "3":
        reduzir_gastos(estado)
        mostrar_dinheiro(estado)
        historico.append(opcoes_menu[2])

    
    elif opcao == "4":
        projetos_extensao(estado)
        mostrar_reputacao(estado)
        historico.append(opcoes_menu[3])

    
    elif opcao == "5":
        print("\n===== HISTÓRICO =====")

        if len(historico) == 0:
            print("Nenhuma ação realizada ainda.")
        else:
            for item in historico:
                print("-", item)

        continue

    
    elif opcao == "6":
        print("Encerrando o simulador...")
        break

    
    if (
        estado["reputacao"] >= 100 and
        estado["qualidade"] >= 100 and
        estado["infraestrutura"] >= 100
    ):
        print("\nPARABÉNS! A universidade virou referência nacional!")
        break

    
    if (
        estado["dinheiro"] <= 0 or
        estado["satisfacao"] <= 0
    ):
        print("\nA universidade entrou em crise e o simulador terminou.")
        break

    
    ciclo += 1


if ciclo > limite_ciclos:
    print("\nLimite de ciclos atingido!")


print("\n===== HISTÓRICO FINAL =====")

if len(historico) == 0:
    print("Nenhuma ação registrada.")
else:
    for item in historico:
        print("-", item)

print("\nObrigado por jogar o Simulador de Gestão Universitária!")