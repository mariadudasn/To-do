from Dao import *

class ToDo():

    def AdicionarTarefa(self, tarefa, x):
        dao = DAO_AdicionarTarefa(tarefa)
        return dao.AdicionarTarefa(x)

    def ExcluirTarefa(self,excluir):
        self.lista.pop(excluir)
        return True

    def ListarTarefa(self):
        daolista = DAO_ListarTarefa()
        return daolista.ListarTarefa()

TODO = ToDo()