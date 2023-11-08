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
                    tarefas = tarefas.split("\t",5)
                    tarefasA = tarefas[0]
                    if "A" == tarefasA:
                        cont +=1
                        print(f"{cont} - {tarefas[4]}")
                    
        except Exception:
            print("Algum erro foi encontrado ou a lista de tarefas está vazia")

class ControllerAlterarTarefa():
    def __init__(self, indice, nova_tarefa):
        try:
            self.indice = indice
            self.nova_tarefa = nova_tarefa
            indices = {}
            indiceInt = int(indice)

            if indiceInt <= 0:
                print("Tarefa invalida. Tente novamente")

            if nova_tarefa == "":
                print("Algo deu errado ao alterar a a trefa. Tente novamente.")

            else:
                cont = 0
                if len(TODO.ListarTarefa()) > 1:
                    for tarefas in TODO.ListarTarefa():
                        tarefas = tarefas.split()
                        tarefasA = tarefas[0]
                        if tarefasA == "A":
                            cont += 1
                            indices[cont] = tarefas[2]

                for chave, valor in indices.items():
                    if chave == indiceInt:
                        if TODO.AlterarTarefa(valor, nova_tarefa) == True:
                            print("Tarefa alterada com sucesso!")
                        else:
                            print("Algum problema foi encontrado. Tente novamente!")

        except Exception:
                print("Valor invalido")


class ControllerConcluirTarefa():
    def __init__(self, indiceAlt):
        try:
            indiceint = int(indiceAlt)

            if indiceint <= 0:
                print("Tarefa invalida. Tente novamente")

            if indiceint == "":
                print ("Falha ao alterar tarefa, tente novamente!")
            
            else:
                cont = 0
                if len(TODO.ListarTarefa()) > 1:
                    for tarefas in TODO.ListarTarefa():
                        tarefasFinal = tarefas.split("\n")
                        tarefas = tarefas.split("\t",6)
                        tarefasA = tarefas[0]
                        if "A" == tarefasA:
                            cont +=1
                        if cont == indiceint:                            
                            tarefasFinal = str(tarefasFinal[0])
                            tarefasAlter = "C" + tarefasFinal[1:]
                            if TODO.AlterarTarefa(tarefasFinal, tarefasAlter) == True:
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
                    tarefas = tarefas.split("\t",5)
                    tarefasA = tarefas[0]
                    if tarefasA == "C":
                        cont += 1
                        print(f"{cont} - {tarefas[4]}")

        except Exception:
            print ("Nenhuma tarefa foi concluída")

class ControllerExcluirTarefa():
    def __init__(self, indiceAlt):
        try:
            indiceint = int(indiceAlt)

            if indiceint <= 0:
                print("Tarefa invalida. Tente novamente")

            if indiceint == "":
                print ("Falha ao alterar tarefa, tente novamente!")
            
            else:
                cont = 0
                if len(TODO.ListarTarefa()) > 1:
                    for tarefas in TODO.ListarTarefa():
                        tarefasFinal = tarefas.split("\n")
                        tarefas = tarefas.split("\t",6)
                        tarefasA = tarefas[0]
                        if "A" == tarefasA:
                            cont +=1
                        if cont == indiceint:                            
                            tarefasFinal = str(tarefasFinal[0])
                            tarefasAlter = "E" + tarefasFinal[1:]
                            if TODO.AlterarTarefa(tarefasFinal, tarefasAlter) == True:
                                print ("Tarefa excluida com sucesso!")
                            else:
                                print (" ")
                                print ("Falha ao concluir tarefa, tente novamente!")

        except Exception:
            print(" ")
            print ("Falha ao concluir tarefa, tente novamente!")