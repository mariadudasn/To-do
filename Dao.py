Arquivo = "ToDo.txt"

class DAO_AdicionarTarefa:

    def AdicionarTarefa(self,tarefa):
        with open(Arquivo, "a") as arquivo:
            arquivo.write(f"{tarefa}\n")
        return True

class DAO_ListarTarefa:

    def ListarTarefa(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas            

