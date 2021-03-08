from validate_docbr import CNPJ

class Cnpj:

    def __init__(self, registro):

        if not self.__valida_cnpj(str(registro)):
            self.__recebe_mensagem("Erro! CNPJ inválido.")
            self.__cnpj = None
        else:
            self.__cnpj = str(registro)

    def __str__(self):
        if self.__cnpj != None:
            return "O número {} é válido!".format(self.__formata_cnpj())
        else:
            return self.__var_msg

    def __valida_cnpj(self, registro):
        return CNPJ().validate(registro)

    def __formata_cnpj(self):
        return "{}.{}.{}/{}-{}".format(self.__cnpj[0:2],
                                       self.__cnpj[2:5],
                                       self.__cnpj[5:8],
                                       self.__cnpj[8:12],
                                       self.__cnpj[12:])

    def __recebe_mensagem(self, msg):
        self.__var_msg = msg