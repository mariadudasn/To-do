Arquivo = "ToDo.txt"

class DAO_AdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa
        self.status = "A"

    def AdicionarTarefa(self, x):
        with open(Arquivo, "a") as arquivo:
            tarefa_formatada = f"{self.status}\t\t\t{x}\t{self.tarefa}"

            with open(Arquivo, "r") as arquivo:
                ler = arquivo.read()

            with open(Arquivo, "a") as arquivo:
                if "STATUS: \tID: \tTAREFA:" not in ler:
                    arquivo.write(f"STATUS: \tID: \tTAREFA:\n")
                arquivo.write(f"{tarefa_formatada}\n")
                return True

class DAO_ListarTarefa:
    def ListarTarefa(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas            


class DAO_AlterarTarefa:
    def AlterarTarefa(self, tarefa_A, novaTarefa):
        with open(Arquivo, "r") as arquivo:
            texto = arquivo.read()

        textoNovo = texto.replace(tarefa_A, novaTarefa)

        with open(Arquivo, "w") as arquivo:
            arquivo.write(textoNovo)
            return True
        
class DAO_ConcluirExcluirTarefa:
    def ConcluirExcluirTarefa(self, statusA, statusN):
        with open(Arquivo, "r") as arquivo:
            status = arquivo.read()

        statusNovo = status.replace(statusA, statusN)

        with open(Arquivo, "w") as arquivo:
            arquivo.write(statusNovo)
            return True