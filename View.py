from Controller import*
import os

sair = 0
while sair == 0:
    os.system("cls")
    print ("SOFTWARE DE TO-DO LIST")
    print (" 01 -> ADICIONAR TAREFA \n 02 -> LISTAR TAREFAS \n 03 -> ALTERAR TAREFA \n 04 -> CONCLUIR TAREFA \n 05 -> LISTAR TAREFAS CONCLUIDAS \n 06 -> EXCLUIR TAREFAS \n 07 -> SAIR")
    print (" ")
    print("QUAL OPÇÃO DESEJA?")

    menu = input(">> ")

    os.system("pause")

    match menu:
        case "1":
            os.system("cls")
            tarefa = input ("Adicione uma tarefa: ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            print (" ")
            os.system("pause")

        case "2":
            os.system("cls")
            print ("Lista de tarefas:")
            print(" ")
            listarTarefa = ControllerListarTarefaA()
            print (" ")
            os.system("pause")

        case "3":
            os.system("cls")
            print ("Alterar tarefas:")
            print(" ")
            print ("Sua lista de tarefas:")
            print(" ")
            listarTarefa = ControllerListarTarefaA()
            print (" ")
            indiceAlt = input ("Qual a tarefa que deseja alterar? Adicione o índice: ")
            novaTarefa = input ("Digite a alteração que deseja fazer: ")
            alterar = ControllerAlterarTarefa(indiceAlt, novaTarefa)
            print(" ")
            listarTarefa = ControllerListarTarefaA()
            print (" ")
            os.system("pause")

        case "4":
            os.system("cls")
            print ("Concluir tarefas:")
            print(" ")
            print ("Sua lista de tarefas:")
            print(" ")
            listarTarefa = ControllerListarTarefaA()
            print (" ")
            indiceAlt = input ("Qual a tarefa que deseja concluir? Adicione o índice: ")
            alterar = ControllerConcluirTarefa(indiceAlt)
            print(" ")
            listarTarefa = ControllerListarTarefaA()
            print (" ")
            os.system("pause")

        case "5":
            os.system("cls")
            print ("Lista de tarefas concluídas:")
            print(" ")
            listarTarefa = ControllerListarTarefaC()
            print (" ")
            os.system("pause")

        # case "6":
        #     os.system("cls")
        #     print ("Lista de tarefas:")
        #     print(" ")
        #     listarTarefa = ControllerListarTarefaA()
        #     print(" ")
        #     excluir = input ("Qual o índice da tarefa que deseja excluir? ")
        #     excluirTarefa = ControllerExcluirTarefa(excluir)
        #     print(" ")
        #     print ("Lista de tarefas:")
        #     print(" ")
        #     listarTarefa = ControllerListarTarefaA()
        #     os.system("pause")

        case "7":
            print ("Saindo...")
            os.system("pause")
            sair = 1

        case _:
            print ("Opção inválida")
            os.system("pause")
