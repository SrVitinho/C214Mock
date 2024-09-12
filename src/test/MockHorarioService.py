from src.main.HorarioService import HorarioService
from src.test.HorariosJsons import HorariosJsons


class MockHorarioService(HorarioService):

    def __int__(self, id):
        self.id = id

    def Procura(self):
        if self.id == 1:
            return HorariosJsons.PaiDoConrado

        elif self.id == 2:
            return HorariosJsons.Chris

        elif self.id == 3:
            return HorariosJsons.Marcelo

        elif self.id == 4:
            return HorariosJsons.Joao

        elif self.id == 5:
            return HorariosJsons.Rapahel

        elif self.id == 6:
            return HorariosJsons.Victoria

        elif self.id == 7:
            return HorariosJsons.Alessandra

        elif self.id == 8:
            return HorariosJsons.Vitor

        elif self.id < 0:
            return HorariosJsons.Inexistente

        else:
            return HorariosJsons.Inválido
