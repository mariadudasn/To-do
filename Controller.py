from Model import *
from Dao import *
from random import *

indices = {}
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


class ControllerListarTarefaA():
    def __init__(self):
        cont = -1
        if len(TODO.ListarTarefa()) > 1:
            for tarefas in TODO.ListarTarefa():
                cont +=1
                if cont >= 1:
                    tarefas = tarefas.split()
                    tarefasA = tarefas[0]
                    if "A" == tarefasA:
                        print(f"{cont} - {tarefas[2]}")
                        indices[cont] = tarefas[1]

lista = ControllerListarTarefaA()

class ControllerAlterarTarefa():
    def __init__(self, indiceAlt, novaTarefa):
        try:
            self.indiceAlt = indiceAlt
            self.novaTarefa = novaTarefa

            if self.indiceAlt in indices:
                for tarefas in TODO.ListarTarefa():
                    lista_L = tarefas.split()
                    tarefasId = lista_L[1]
                    if tarefasId == indices[self.indiceAlt]:
                        tarefa_A = tarefas [9:-1]
                        TODO.AlterarTarefa(tarefa_A, novaTarefa)
        except Exception:
            print("Opção inválida")