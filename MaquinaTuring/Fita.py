class Fita:
    def __init__(self, cadeia):
        self.__listaFita = [">", "u"]
        self.__listaComp = ["u","u","u","u","u"]
        self.setlistaFita(cadeia)
        self.setlistaFitaDois(cadeia)

    def setlistaFita(self, novaFita):
        self.__fita = []
        self.__fita.extend(self.__listaFita)
        self.__fita.extend(novaFita)
        self.__fita.extend(self.__listaComp)

    def getlistaFita(self):
        return self.__fita

    def setlistaFitaDois(self, novaFita):
        tamanho = 1 + (len(novaFita) // 2)
        self.__fitaDois = []
        self.__fitaDois.extend(self.__listaFita)
        self.__fitaDois.extend(["u"] * tamanho)

    def getlistaFitaDois(self):
        return self.__fitaDois