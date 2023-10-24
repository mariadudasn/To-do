from Dao import *

class ToDo():

    def AdicionarTarefa(self, tarefa):
        dao = DAO_AdicionarTarefa()
        return dao.AdicionarTarefa(tarefa)

    def ExcluirTarefa(self,excluir):
        self.lista.pop(excluir)
        return True

    def ListarTarefa(self):
        daolista = DAO_ListarTarefa()
        return daolista.ListarTarefa()

TODO = ToDo()