from Dao import *

class ToDo():

    def AdicionarTarefa(self):
        dao = DAO_AdicionarTarefa()
        return dao.AdicionarTarefa()

    # def ExcluirTarefa(self,excluir):
    #     self.lista.pop(excluir)
    #     return True

    def ListarTarefa(self):
        daolista = DAO_ListarTarefa()
        return daolista

TODO = ToDo()