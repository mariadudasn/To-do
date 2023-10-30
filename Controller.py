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
                        tarefas = tarefas.split()
                        tarefass = int(tarefas[1])
                        if id != tarefass:
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

class ControllerListarTarefaA():
    def __init__(self):
        try:
            cont = 0
            if len(TODO.ListarTarefa()) > 1:
                for tarefas in TODO.ListarTarefa():
                    tarefas = tarefas.split()
                    tarefasA = tarefas[0]
                    if "A" == tarefasA:
                        cont +=1
                        print(f"{cont} - {tarefas[2]}")
            
            else:
                if TODO.ListarTarefa() == "":
                    print("A lista de tarefas está vazia")
                    
        except Exception:
            print("Algum erro foi encontrado")


class ControllerAlterarTarefa():
    def __init__(self, indiceAlt, novaTarefa):
        try:
            self.indiceAlt = indiceAlt
            self.novaTarefa = novaTarefa
            indices = {}
            indiceint = int(indiceAlt)

            if novaTarefa == "":
                print ("Falha ao alterar tarefa, tente novamente!")
            
            else:
                cont = 0
                if len(TODO.ListarTarefa()) > 1:
                    for tarefas in TODO.ListarTarefa():
                        tarefas = tarefas.split()
                        tarefasA = tarefas[0]
                        if "A" == tarefasA:
                            cont +=1
                            indices[cont] = tarefas[2]

                for chave, valor in indices.items():
                    if chave == indiceint:
                        if TODO.AlterarTarefa(valor, novaTarefa) == True:
                            print ("Tarefa alterada com sucesso!")
                        else:
                            print (" ")
                            print ("Falha ao alterar tarefa, tente novamente!")
                
        except Exception:
            print(" ")
            print ("Falha ao alterar tarefa, tente novamente!")

class ControllerConcluirTarefa():
    def __init__(self, indiceAlt):
        try:
            statusN = "C"
            indices = {}
            indiceint = int(indiceAlt)

            if indiceint == "":
                print ("Falha ao alterar tarefa, tente novamente!")
            
            else:
                cont = 0
                if len(TODO.ListarTarefa()) > 1:
                    for tarefas in TODO.ListarTarefa():
                        tarefas = tarefas.split()
                        tarefasA = tarefas[0]
                        if "A" == tarefasA:
                            cont +=1
                            indices[cont] = tarefas[0]

                for chave, valor in indices.items():
                    if chave == indiceint:
                        if TODO.ConcluirExcluirTarefa(valor, statusN) == True:
                            print ("Tarefa concluída com sucesso!")
                        else:
                            print (" ")
                            print ("Falha ao concluir tarefa, tente novamente!")

        except Exception:
            print(" ")
            print ("Falha ao concluir tarefa, tente novamente!")

class ControllerListarTarefaC():
    def __init__(self):
        try:
            cont = 0
            if len(TODO.ListarTarefa()) > 1:
                for tarefas in TODO.ListarTarefa():
                    tarefas = tarefas.split()
                    tarefasC = tarefas[0]
                    if "C" == tarefasC:
                        cont +=1
                        print(f"{cont} - {tarefas[2]}")
        except Exception:
            print ("Nenhuma tarefa foi concluída")

class ControllerExcluirTarefa():
    def __init__(self, indiceAlt):
        try:
            statusN = "E"
            indices = {}
            indiceint = int(indiceAlt)

            if indiceint == "":
                print ("Falha ao alterar tarefa, tente novamente!")
            
            else:
                cont = 0
                if len(TODO.ListarTarefa()) > 1:
                    for tarefas in TODO.ListarTarefa():
                        tarefas = tarefas.split()
                        tarefasA = tarefas[0]
                        if "A" == tarefasA:
                            cont +=1
                            indices[cont] = tarefas[0]

                for chave, valor in indices.items():
                    if chave == indiceint:
                        if TODO.ConcluirExcluirTarefa(valor, statusN) == True:
                            print ("Tarefa excluída com sucesso!")
                        else:
                            print (" ")
                            print ("Falha ao excluir tarefa, tente novamente!")

        except Exception:
            print(" ")
            print ("Falha ao concluir tarefa, tente novamente!")