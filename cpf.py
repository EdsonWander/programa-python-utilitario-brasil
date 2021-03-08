from validate_docbr import CPF

class Cpf():

    def __init__(self, registro):

        if not self.__valida_cpf(str(registro)):
            self.__recebe_mensagem("Erro! CPF inválido.")
            self.__cpf = None
        else:
            self.__cpf = str(registro)

    def __str__(self):
        if self.__cpf != None:
            return "O número {} é válido!".format(self.__formata_cpf())
        else:
            return self.__var_msg

    def __valida_cpf(self, registro):
        return CPF().validate(registro)

    def __formata_cpf(self):
        return "{}.{}.{}-{}".format(self.__cpf[0:3],
                                    self.__cpf[3:6],
                                    self.__cpf[6:9],
                                    self.__cpf[9:])

    def __recebe_mensagem(self, msg):
        self.__var_msg = msg