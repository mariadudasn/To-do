from random import randint

Arquivo = "ToDo.txt"
ids = []

class DAO_AdicionarTarefa:

    def AdicionarTarefa(self,tarefa):
        self.id = randint(1000,9999)
        ids.append(self.id)
        with open(Arquivo, "a") as arquivo:
            id = randint(1000,9999)
            if id in ids:
                return False
            else:
                arquivo.write(f"{id}\t{tarefa}\n")
                return True

class DAO_ListarTarefa:

    def ListarTarefa(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas            

