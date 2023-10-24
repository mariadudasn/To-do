from Model import *
from Dao import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        m = 0
        while m == 0:
            try:
                self.tarefa = tarefa
                
                if self.tarefa == "":
                    print("Informe uma tarefa válida")
                else:
                    if TODO.AdicionarTarefa(self.tarefa) == True:
                        print ("Tarefa adicionada")
                        m = 1
                    else:
                        print ("Algum problema foi encontrado ao tentar adicionar tarefa")
            except Exception:
                print("Opção inválida")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        s = 0
        while s == 0:
            try:
                x = int(excluir)
                self.excluir = x - 1

                if TODO.ExcluirTarefa(self.excluir) == True:
                        print ("Tarefa excluída")
                        s = 1
                else:
                    print ("Algum problema foi encontrado ao tentar excluir tarefa")

            except Exception:
                print("Opção inválida")
                excluir = input ("Qual o índice da tarefa que deseja excluir? ")


class ControllerListarTarefa():
    def __init__(self):
        cont = -1
        for tarefa in TODO.ListarTarefa():
            cont += 1
            if cont >= 1:
                tarefa = tarefa[5:-1]
                print(f"{cont} - {tarefa}")
