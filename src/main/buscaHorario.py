class buscaHorario:
    def __init__(self, service):
        self.horarioService = service

    def buscaHorario(self, id):
        jsonHorario = self.horarioService.procura(id)
        return jsonHorario.Nome, jsonHorario.idProfessor, jsonHorario.horarioDeAtendimento, jsonHorario.Periodo, jsonHorario.Sala, jsonHorario.Predio
