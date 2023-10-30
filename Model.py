from Dao import *

class ToDo():

    def AdicionarTarefa(self, tarefa, x):
        daoadd = DAO_AdicionarTarefa(tarefa)
        return daoadd.AdicionarTarefa(x)

    # def ExcluirTarefa(self, excluir):
    #     self.lista.pop(excluir)
    #     return True

    def ListarTarefa(self):
        daolista = DAO_ListarTarefa()
        return daolista.ListarTarefa()
    
    def AlterarTarefa(self, tarefa_A, novaTarefa):
        daoalterar = DAO_AlterarTarefa()
        return daoalterar.AlterarTarefa(tarefa_A, novaTarefa)
    
    def ConcluirTarefa(self, statusA, statusN):
        daoconcluir = DAO_ConcluirTarefa()
        return daoconcluir.ConcluirTarefa(statusA, statusN)
    
TODO = ToDo()