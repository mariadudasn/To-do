Arquivo = "ToDo.txt"

class DAO_AdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa

    def AdicionarTarefa(self, x):
        with open(Arquivo, "a") as arquivo:
            tarefa_formatada = f"{x}\t{self.tarefa}"

            with open(Arquivo, "r") as arquivo:
                ler = arquivo.read()

            with open(Arquivo, "a") as arquivo:
                if "ID: \tTAREFA:" not in ler:
                    arquivo.write(f"ID: \tTAREFA:\n")
                arquivo.write(f"{tarefa_formatada}\n")
                return True

class DAO_ListarTarefa:

    def ListarTarefa(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas            

