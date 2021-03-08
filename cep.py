import requests

class Cep():

    def __init__(self, cep):
        self.__var_url = "https://viacep.com.br/ws/{}/json/".format(cep)

    def __str__(self):

        __obj_response = self.__pesquisa_cep()

        if __obj_response.status_code != 400:
            __var_dir_json = __obj_response.json()

            if not 'erro' in __var_dir_json:
                return "\nCEP: {} \n" \
                       "Logradouro: {} \n" \
                       "Bairro: {} \n" \
                       "Cidade: {} \n" \
                       "Estado: {}".format(__var_dir_json['cep'],
                                           __var_dir_json['logradouro'],
                                           __var_dir_json['bairro'],
                                           __var_dir_json['localidade'],
                                           __var_dir_json['uf'])
            else:
                return "Erro! CEP inválido."
        else:
            return "Erro! CEP inválido."

    def __pesquisa_cep(self):
        return requests.get(self.__var_url)