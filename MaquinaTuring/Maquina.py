from ControleFinito import *
from Fita import *

class Maquina:
    def __init__(self, cadeia):
        self.__fita = Fita(cadeia)
        self.__controle = ControleFinito()
        self.__controle.setPosicao(len(cadeia) + 2)

    def Lu(self):
        # Maquina que encontra o primeiro espaço em branco e para. Indo para a esquerda.
        self.imprimir()
        while self.__controle.getEstado() != "Lh":
            if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "q0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("q1")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "q1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q1")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "q1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("Lh")
                self.__controle.setPosicao(0)
                self.imprimir()

    def Ru(self):
        # Maquina que encontra o primeiro espaço em branco e para. Indo para a Direita.
        if self.__controle.getEstado() == "Th":
            self.imprimirSoma()
        else:
            self.imprimir()
        while self.__controle.getEstado() != "Rh":
            if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "Lh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("q2")
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "Lnh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q2")
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "qs" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q2")
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "Ap" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("q2")
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "q2" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q2")
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "q2" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("Rh")
                self.__controle.setPosicao(0)
                self.imprimir()
            elif self.__controle.getEstado() == "Th" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("qr1")
                self.__controle.setPosicao(1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qr1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setPosicao(1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qr1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("Rh")
                self.imprimirSoma()

    def Lnu(self):
        # Maquina que encontra o primeiro espaço não branco e para. Indo para a Esquerda.
        self.imprimir()
        while self.__controle.getEstado() != "Lnh":
            if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "qdc0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q3")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "qdc1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q3")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "Rh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("q3")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "Rh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q3")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "q3" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("q4")
                self.__controle.setPosicao(-1)
                if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                    self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "q4" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("q3")
                self.imprimir()
            elif self.__controle.getEstado() == "q4" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("Lnh")
                self.__controle.setPosicao(0)
                self.imprimir()
            elif self.__controle.getEstado() == "q3" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.__controle.setEstado("Lnh")
                self.__controle.setPosicao(0)
                self.imprimir()

    def maqApagar(self):
        # Maquina que apaga
        if self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
            self.__fita.getlistaFita()[self.__controle.getPosicao()] = "u"
            self.__controle.setEstado("Ap")

    def sucessor(self):
        # Maquina que diz o sucessor
        self.Lu()
        self.Ru()
        while self.__controle.getEstado() != "Sh":
            if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "Rh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("qs")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "qs" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1":
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.imprimir()
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "qs" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0":
                self.__controle.setEstado("Sh")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimir()
            elif self.__controle.getEstado() == "qs" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimir()
                self.deslocarDir()

    def antecessor(self):
        # Maquina que diz o antecessor
        self.Lu()
        self.Ru()
        while self.__controle.getEstado() != "Ah":
            if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "Rh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("q3")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "q3" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0":
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimir()
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "q3" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1":
                self.__controle.setEstado("Ah")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.imprimir()

    def deslocarDir(self):
        # Maquina que desloca para direita
        self.Ru()
        while self.__fita.getlistaFita()[self.__controle.getPosicao()] != "qdh":
            if self.__controle.getEstado() == "Lnh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] != "u":
                self.Ru()
            elif self.__controle.getEstado() == "Rh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("qd")
                self.__controle.setPosicao(-1)
                self.imprimir()
            elif self.__controle.getEstado() == "qd" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0":
                self.__controle.setEstado("qdl0")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "u"
                self.imprimir()
            elif self.__controle.getEstado() == "qdl0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("qdc0")
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "qdc0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.Lnu()
            elif self.__controle.getEstado() == "qd" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1":
                self.__controle.setEstado("qdl1")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "u"
                self.imprimir()
            elif self.__controle.getEstado() == "qdl1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("qdc1")
                self.__controle.setPosicao(1)
                self.imprimir()
            elif self.__controle.getEstado() == "qdc1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.Lnu()
            elif self.__controle.getEstado() == "Lnh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setPosicao(0)
                self.__controle.setEstado("qdh")
                self.imprimirSuc()

    def divisaoPorDois(self):
        # Maquina que divide por dois
        self.Lu()
        self.Ru()
        self.Lnu()
        self.maqApagar()
        self.imprimir()
        self.__controle.setEstado("divh")
        self.imprimir()

    def ajustarPrint(self, argumento):
        # pega uma lista e converte em string
        saida = ""
        ajuste = argumento
        for item in ajuste:
            saida += str(item)
        return saida

    def maqTransicao(self):#Máquina que escreve 0 na fita um e passa o que tinha na fita um para a fita 2.
        self.imprimirSoma()
        while self.__controle.getEstado() != "Th":
            if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                self.__controle.setPosicao(1)
                self.imprimirSoma()
            elif self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == ">":
                self.__controle.setPosicaoFitaDois(1)
            elif self.__controle.getEstado() == "Lh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("qt2")
                self.__controle.setPosicao(1)
                self.__controle.setPosicaoFitaDois(1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qt2" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "u":
                self.__controle.setEstado("qt0")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] = "0"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qt2" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "u":
                self.__controle.setEstado("qt1")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] = "1"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qt0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] != "u":
                self.__controle.setEstado("qt2")
                self.__controle.setPosicao(1)
                self.__controle.setPosicaoFitaDois(1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qt1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] != "u":
                self.__controle.setEstado("qt2")
                self.__controle.setPosicao(1)
                self.__controle.setPosicaoFitaDois(1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qt2" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "+":
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.__controle.setEstado("Th")
                self.imprimirSoma()

    def maqQueSoma(self):#Máquina que soma
        self.Lu()
        self.maqTransicao()
        self.Ru()
        while self.__controle.getEstado() != "SMh":
            if self.__fita.getlistaFita()[self.__controle.getPosicao()] == ">":
                self.__controle.setPosicao(1)
                self.imprimirSoma()
            elif self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == ">":
                self.__controle.setPosicaoFitaDois(1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "Rh" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "u":
                self.__controle.setEstado("qs0")
                self.__controle.setPosicao(-1)
                self.__controle.setPosicaoFitaDois(-1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "1":
                self.__controle.setEstado("qs4")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs4":
                self.__controle.setEstado("qs1")
                self.__controle.setPosicao(-1)
                self.__controle.setPosicaoFitaDois(-1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "0":
                self.__controle.setEstado("qs2")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "1":
                self.__controle.setEstado("qs2")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "0":
                self.__controle.setEstado("qs2")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs2":
                self.__controle.setEstado("qs0")
                self.__controle.setPosicao(-1)
                self.__controle.setPosicaoFitaDois(-1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "1":
                self.__controle.setEstado("qs3")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "0":
                self.__controle.setEstado("qs3")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "1":
                self.__controle.setEstado("qs3")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "1" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "0":
                self.__controle.setEstado("qs3")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "0"
            elif self.__controle.getEstado() == "qs3":
                self.__controle.setEstado("qs1")
                self.__controle.setPosicao(-1)
                self.__controle.setPosicaoFitaDois(-1)
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs1" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "u":
                self.__controle.setEstado("SMh")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimirSoma()
            elif self.__controle.getEstado() == "qs0" and self.__fita.getlistaFita()[self.__controle.getPosicao()] == "0" and self.__fita.getlistaFitaDois()[self.__controle.getPosicaoFitaDois()] == "u":
                self.__controle.setEstado("SMh")
                self.__fita.getlistaFita()[self.__controle.getPosicao()] = "1"
                self.imprimirSoma()

    def imprimirSuc(self):
        retorno = self.ajustarPrint(self.__fita.getlistaFita())
        print("-> ", self.__controle.getEstado() + " - ",retorno[:self.__controle.getPosicao()] + "[" + retorno[self.__controle.getPosicao()] + "]" + retorno[self.__controle.getPosicao() + 1:-3])

    def imprimir(self):
        retorno = self.ajustarPrint(self.__fita.getlistaFita())
        print("-> ", self.__controle.getEstado() + " - ", retorno[:self.__controle.getPosicao()] + "[" + retorno[self.__controle.getPosicao()] + "]" + retorno[self.__controle.getPosicao() + 1:-4])

    def imprimirSoma(self):
        retorno = self.ajustarPrint(self.__fita.getlistaFita())
        retorno2 = self.ajustarPrint(self.__fita.getlistaFitaDois())
        print("-> ", self.__controle.getEstado() + " - ",retorno[:self.__controle.getPosicao()] + "[" + retorno[self.__controle.getPosicao()] + "]" + retorno[self.__controle.getPosicao() + 1:-4],"   ","|"," ","-> ",retorno2[:self.__controle.getPosicaoFitaDois()] + "[" + retorno2[self.__controle.getPosicaoFitaDois()] + "]" + retorno2[self.__controle.getPosicaoFitaDois() + 1:])