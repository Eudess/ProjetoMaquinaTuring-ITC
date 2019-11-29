class ControleFinito:
    def __init__(self):
        self.__estado = "q0"
        self.__posicao = 0
        self.__posicaoFitaDois = 1

    def setEstado(self, novoEstado):
        self.__estado = novoEstado

    def getEstado(self):
        return self.__estado

    def setPosicao(self, novaPosicao):
        self.__posicao += novaPosicao

    def getPosicao(self):
        return self.__posicao

    def setPosicaoFitaDois(self, novaPosicao):
        self.__posicaoFitaDois += novaPosicao

    def getPosicaoFitaDois(self):
        return self.__posicaoFitaDois