class Ajustes:

    def imprimeMenu(self):
        print("\nMáquina de turing\n")
        print()
        print("Escolha uma das opções a seguir:")
        print()
        print("1. Decimal.\n2. Binário.\n3. Encerrar a Máquina.\n")

    def menuPrincipal(self):
        print("Menu Principal")
        print()
        print("Escolha uma das opções a seguir:")
        print()
        print("1. Divisão por 2.\n2. Antecessor.\n3. Sucessor.\n4. Máquina que Soma.\n5. Sair.\n")

    def menuOpcao(self):
        while True:
            try:
                num = int(input(". "))
                break
            except:
                print("\nOpção inválida, tente novamente.\n")
        if num not in range(1, 4):
            print("\nSua escolha não está entre as opções!\nTente novamente!\n")
        else:
            return num
    def menuEscolhas(self):
        while True:
            try:
                num = int(input(". "))
                break
            except:
                print("\nOpção inválida, tente novamente.\n")
        if num not in range(1, 6):
            print("\nSua escolha não está entre as opções!\nTente novamente!\n")
        else:
            return num

    def escolhaDec(self):
        while True:
            try:
                dados = int(input("\nDigite o número: "))
                print()
                break
            except:
                print("\nDigite apenas números!\n")
        novosDados = bin(dados)
        novosDados = novosDados[2:]
        listaDados = []
        for num in novosDados:
            listaDados.append(num)
        return listaDados

    def escolhaBin(self):
        while True:
            try:
                dados = input("\nDigite o número: ")
                print()
                break
            except:
                print("\nDigite apenas números!\n")
        listaDados = []
        for num in dados:
            if num not in "10":
                print("Digite apenas 1's ou 0's!\n")
            else:
                listaDados.append(num)
        return listaDados

    def escolhaDecSoma(self):
        while True:
            try:
                dados = int(input("\nDigite o primeiro número: "))
                break
            except:
                print("\nDigite apenas números!\n")
        while True:
            try:
                dados2 = int(input("Digite o primeiro número: "))
                print()
                break
            except:
                print("\nDigite apenas números!\n")
        numeros = ""
        listaDados = []
        novosDados = bin(dados)
        novosDados = novosDados[2:]
        novosDados2 = bin(dados2)
        novosDados2 = novosDados2[2:]
        if len(novosDados) > len(novosDados2):
            numeros += novosDados + "+" + novosDados2
        else:
            numeros += novosDados2 + "+" + novosDados
        for elemento in numeros:
            listaDados.append(elemento)
        return listaDados

    def escolhaBinSoma(self):
        while True:
            try:
                dados = input("\nDigite o primeiro número: ")
                break
            except:
                print("\nDigite apenas números!\n")
        while True:
            try:
                dados2 = input("Digite o primeiro número: ")
                print()
                break
            except:
                print("\nDigite apenas números!\n")
        for num in dados:
            if num not in "10":
                print("Digite apenas 1's ou 0's!\n")
        for num2 in dados2:
            if num2 not in "10":
                print("Digite apenas 1's ou 0's!\n")
        numeros = ""
        listaDados = []
        if len(dados) > len(dados2):
            numeros += dados + "+" + dados2
        else:
            numeros += dados2 + "+" + dados
        for elemento in numeros:
            listaDados.append(elemento)
        return listaDados