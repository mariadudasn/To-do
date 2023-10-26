from Dao import *

class ToDo():

    def AdicionarTarefa(self, tarefa, x):
        dao = DAO_AdicionarTarefa(tarefa)
        return dao.AdicionarTarefa(x)

    def ExcluirTarefa(self, excluir):
        self.lista.pop(excluir)
        return True

    def ListarTarefa(self):
        daolista = DAO_ListarTarefa()
        return daolista.ListarTarefa()
    
    def AlterarTarefa(self, tarefa_A, novaTarefa):
        daoalterar = DAO_AlterarTarefa()
        return daoalterar.AlterarTarefa(tarefa_A, novaTarefa)
    
TODO = ToDo()