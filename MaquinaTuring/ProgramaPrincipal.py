from Ajustes import *
from Maquina import *

a = Ajustes()

while True:
    a.imprimeMenu()
    opcao = a.menuOpcao()
    if opcao == 1:
        a.menuPrincipal()
        escolha = a.menuEscolhas()
        if escolha == 1:
            dados = a.escolhaDec()
            if dados == ["0"] or dados == ["1"]:
                print("\nNão é possível realizar essa operação!\n")
            else:
                maquina = Maquina(dados)
                maquina.divisaoPorDois()

        elif escolha == 2:
            dados = a.escolhaDec()
            if dados == ["0"]:
                print("\nNão é possível realizar essa operação!\n")
            else:
                maquina = Maquina(dados)
                maquina.antecessor()

        elif escolha == 3:
            dados = a.escolhaDec()
            maquina = Maquina(dados)
            maquina.sucessor()

        elif escolha == 4:
            dados = a.escolhaDecSoma()
            maquina = Maquina(dados)
            maquina.maqQueSoma()

        elif escolha == 5:
            break

    elif opcao == 2:
        a.menuPrincipal()
        escolha = a.menuEscolhas()
        if escolha == 1:
            dados = a.escolhaBin()
            if dados != []:#Condição para evitar que a máquina execute mesmo sem ter digitado nada.
                if dados == ["0"] or dados == ["1"]:
                    print("\nNão é possível realizar essa operação!\n")
                else:
                    maquina = Maquina(dados)
                    maquina.divisaoPorDois()

        elif escolha == 2:
            dados = a.escolhaBin()
            if dados != []:#Condição para evitar que a máquina execute mesmo sem ter digitado nada.
                if dados == ["0"]:
                    print("\nNão é possível realizar essa operação!\n")
                else:
                    maquina = Maquina(dados)
                    maquina.antecessor()

        elif escolha == 3:
            dados = a.escolhaBin()
            if dados != []:#Condição para evitar que a máquina execute mesmo sem ter digitado nada.
                maquina = Maquina(dados)
                maquina.sucessor()

        elif escolha == 4:
            dados = a.escolhaBinSoma()
            if dados != []:  # Condição para evitar que a máquina execute mesmo sem ter digitado nada.
                maquina = Maquina(dados)
                maquina.maqQueSoma()

        elif escolha == 5:
            break

    elif opcao == 3:
        break