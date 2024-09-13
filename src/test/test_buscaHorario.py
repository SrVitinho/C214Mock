import pytest
from src.main.buscaHorario import buscaHorario
from src.test.MockHorarioService import MockHorarioService

# Mockando o serviço
@pytest.fixture
def mock_servico():
    return MockHorarioService()

# Criando uma instância da classe buscaHorario
@pytest.fixture
def busca(mock_servico):
    return buscaHorario(mock_servico)

# Função auxiliar para verificar se a sala está no prédio correto
def predio_correto(sala, predio):
    sala = int(sala)
    predio = int(predio)
    if 1 <= sala <= 5 and predio == 1:
        return True
    elif 6 <= sala <= 10 and predio == 2:
        return True
    elif 11 <= sala <= 15 and predio == 3:
        return True
    elif 16 <= sala <= 20 and predio == 4:
        return True
    elif 21 <= sala <= 30 and predio == 6:
        return True
    return False

# Testa se a sala do PaiDoConrado está no prédio correto
def test_sala_PaiDoConrado(busca):
    resultado = busca.buscaHorario(1)
    assert predio_correto(resultado[4], resultado[5]), "Sala do PaiDoConrado está no prédio errado"

# Testa se o ID retornado do Chris está correto
def test_id_Chris(busca):
    resultado = busca.buscaHorario(2)
    assert resultado[0] == "2", "ID incorreto do Chris"

# Testa se a sala do Chris está no prédio correto
def test_sala_Chris(busca):
    resultado = busca.buscaHorario(2)
    assert predio_correto(resultado[4], resultado[5]), "Sala do Chris está no prédio errado"

# Testa se o ID retornado do Marcelo está correto
def test_id_Marcelo(busca):
    resultado = busca.buscaHorario(3)
    assert resultado[0] == "3", "ID incorreto do Marcelo"

# Testa se a sala do Marcelo está no prédio correto
def test_sala_Marcelo(busca):
    resultado = busca.buscaHorario(3)
    assert predio_correto(resultado[4], resultado[5]), "Sala do Marcelo está no prédio errado"

# Testa se a sala da Victoria está no prédio correto
def test_sala_Victoria(busca):
    resultado = busca.buscaHorario(6)
    assert predio_correto(resultado[4], resultado[5]), "Sala da Victoria está no prédio errado"

# Testa se a sala da Alessandra está no prédio correto
def test_sala_Alessandra(busca):
    resultado = busca.buscaHorario(7)
    assert predio_correto(resultado[4], resultado[5]), "Sala da Alessandra está no prédio errado"

# Testa se a sala do Vitor está no prédio correto
def test_sala_Vitor(busca):
    resultado = busca.buscaHorario(8)
    assert predio_correto(resultado[4], resultado[5]), "Sala do Vitor está no prédio errado"

# Testa se o horário de atendimento da Alessandra está correto
def test_horario_Alessandra(busca):
    resultado = busca.buscaHorario(7)
    assert resultado[2] == "12:00 - 14:00", "Horário de atendimento da Alessandra está errado"

def test_periodo_Chris(busca):
    resultado = busca.buscaHorario(2)
    assert resultado[3] == "noturno", "Período do Chris está errado"