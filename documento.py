from cpf import Cpf
from cnpj import Cnpj

class Documento:

    def __init__(self, registro):

        __var_retorno = self.__valida_tamanho(str(registro))

        if not __var_retorno:
            self.__documento = None
            self.__recebe_mensagem("Erro! Tamanho do número inválido.")
        elif __var_retorno == "CPF":
            self.__documento = Cpf(registro)
        else:
            self.__documento = Cnpj(registro)

    def __str__(self):

        if self.__documento != None:
            return self.__documento.__str__()
        else:
            return self.__var_msg

    def __valida_tamanho(self, registro):

        if len(registro) == 11:
            return "CPF"
        elif len(registro) == 14:
            return "CNPJ"
        else:
            return False

    def __recebe_mensagem(self, msg):
        self.__var_msg = msg
