from documento import Documento
from telefone import Telefone
from cep import Cep
from datetime import datetime
import os

#Captura o nome do usuário do computador, USERNAME para Windows, USER para Linux
var_usuario = os.getenv("USERNAME")
if var_usuario  == None: var_usuario = os.getenv("USER")

print("*********************************")
print("***** Utilitários do Brasil *****")
print("*********************************", end="\n\n")

#Utilização da classe datetime, com formato de data Brasil
print("Entrada: {}".format(datetime.today().strftime("%d/%m/%Y %H:%M")))
print("Usuário: {}".format(var_usuario.capitalize()), end="\n\n")

#Menu
print("Escolha a validação de sua preferência:")
print(" (1) CPF")
print(" (2) CNPJ")
print(" (3) Telefone")
print(" (4) CEP", end="\n\n")

while(True):

    var_opcao = int(input("Digite a sua opção de validação: "))

    if(var_opcao >= 1 and var_opcao <=4):
        print("", end="\n")

        if (var_opcao == 1):

            #Cria uma instância da classe Documento
            obj_documento = Documento(input("Digite um número de CPF: "))
            print(obj_documento)


        elif (var_opcao == 2):

            #Cria uma instância da classe Documento
            obj_documento = Documento(input("Digite um número de CNPJ: "))
            print(obj_documento)

        elif (var_opcao == 3):

            #Cria uma instância da classe Telefone
            obj_telefone = Telefone(input("Digite um número de Telefone: "))
            print(obj_telefone)

        else:

            #Cria uma instância da classe Cep
            obj_cep = Cep(input("Digite um número de CEP: "))
            print(obj_cep)

        print("", end="\n")

        var_opcao = input("Deseja continuar usando? (S) (N) ")

        if (var_opcao.upper() == 'N'):
            break
        elif (var_opcao.upper() == 'S'):
            print("", end="\n")
        else:
            print("Opção inválida!", end="\n\n")
    else:
        print("Opção inválida!", end="\n\n")
