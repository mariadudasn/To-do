from Model import *
from Dao import *
from random import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
            try:
                self.tarefa = tarefa
                id = randint(1000,9999)
                cont = -1
                if len(TODO.ListarTarefa()) > 1:
                    for tarefas in TODO.ListarTarefa():
                        cont +=1
                        if cont >= 1:
                            tarefas = tarefas [:4]
                            tarefas = int(tarefas)
                            if id != tarefas:
                                if self.tarefa == "":
                                    print ("Digite novamente, tarefa inválida")
                                else:
                                    if TODO.AdicionarTarefa(self.tarefa, id) == True: 
                                        print ("Tarefa adicionada")
                                        break
                                    else:
                                        print ("Tarefa não foi adicionada")
                                        break
                            else:
                                id = randint (1000, 9999)

                else:
                    if self.tarefa == "":
                        print ("Digite novamente, tarefa inválida")    
                    else:
                        if TODO.AdicionarTarefa(self.tarefa, id) == True: 
                            print ("Tarefa adicionada")
                        else:
                            print ("Tarefa não foi adicionada")
                            
                            
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
