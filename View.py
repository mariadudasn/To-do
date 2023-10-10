from Controller import*
import os

sair = 0
while sair == 0:
    os.system("cls")
    print ("SOFTWARE DE TO-DO")
    print ("01 -> ADICIONAR TAREFA")
    print ("02 -> LISTAR TAREFAS")
    print ("03 -> EXCLUIR TAREFA")
    print ("04 -> SAIR")
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
            listarTarefa = ControllerListarTarefa()
            print (" ")
            os.system("pause")
        # case "3":
        #     os.system("cls")
        #     print ("Lista de tarefas:")
        #     print(" ")
        #     listarTarefa = ControllerListarTarefa()
        #     print(" ")
        #     excluir = input ("Qual o índice da tarefa que deseja excluir? ")
        #     excluirTarefa = ControllerExcluirTarefa(excluir)
        #     print(" ")
        #     print ("Lista de tarefas:")
        #     print(" ")
        #     listarTarefa = ControllerListarTarefa()
        #     os.system("pause")
        case "4":
            print ("Saindo...")
            os.system("pause")
            break
        case _:
            print ("Opção inválida")
            os.system("pause")
