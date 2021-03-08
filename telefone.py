import re

class Telefone:

    def __init__(self, numero):

        self.__padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

        if not self.__valida_telefone(str(numero)):
            self.__recebe_mensagem("Erro! Telefone inválido.")
            self.__numero = None
        else:
            self.__numero = str(numero)

    def __str__(self):

        if self.__numero != None:
            return "O número {} é válido!".format(self.__formata_telefone())
        else:
            return self.__var_msg

    def __valida_telefone(self, numero):
        return re.search(self.__padrao, str(numero))

    def __formata_telefone(self):

        __var_pesquisa = re.search(self.__padrao, self.__numero)

        if __var_pesquisa.group(1) != None:
            return "+{} ({}) {}-{}".format(__var_pesquisa.group(1),
                                           __var_pesquisa.group(2),
                                           __var_pesquisa.group(3),
                                           __var_pesquisa.group(4))
        else:
            return "({}) {}-{}".format(__var_pesquisa.group(2),
                                       __var_pesquisa.group(3),
                                       __var_pesquisa.group(4))

    def __recebe_mensagem(self, msg):
        self.__var_msg = msg