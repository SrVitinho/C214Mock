import json
from .horarioDeAtendimento import horarioDeAtendimento


class buscaHorario:
    def __init__(self, service):
        self.horarioService = service

    def buscaHorario(self, id):
        jsonHorarioString = self.horarioService.Procura(id)
        # convertendo a string em um json
        jsonHorario = json.loads(jsonHorarioString)

        return jsonHorario["id"], jsonHorario["nomeDoProfessor"], jsonHorario["horarioDeAtendimento"], jsonHorario["periodo"], jsonHorario["sala"], jsonHorario["predio"]