from fastapi.testclient import TestClient
from calculadora_completa.main import app

client = TestClient(app)

def test_somar_a_b_validos():
    response = client.get('/somar?a=2&b=2')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 2, "resultado" :4 }

def test_somar_a_invalido_b_valido():
    response = client.get('/somar?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() == {'error': "[{'type': 'int_parsing', 'loc': ('query', 'a'), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': '2.2'}]"}

def test_subtrair_a_b_validos():
    response = client.get('/subtrair?a=2&b=3')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 3, "resultado" : -1 }

def test_subtrarir_a_invalido_b_valido():
    response = client.get('/subtrair?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() ==  {'error': "[{'type': 'int_parsing', 'loc': ('query', 'a'), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': '2.2'}]"}

def test_multiplicar_a_b_validos():
    response = client.get('/multiplicar?a=2&b=3')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 3, "resultado" : 6 }

def test_multiplicar_a_invalido_b_valido():
    response = client.get('/multiplicar?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() ==  {'error': "[{'type': 'int_parsing', 'loc': ('query', 'a'), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': '2.2'}]"}

def test_dividir_a_b_validos():
    response = client.get('/dividir?a=4&b=2')
    assert response.status_code == 200
    assert response.json() == {"a": 4, "b": 2, "resultado" : 2 }

def test_dividir_a_invalido_b_valido():
    response = client.get('/dividir?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() ==  {'error': "[{'type': 'int_parsing', 'loc': ('query', 'a'), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': '2.2'}]"}

# def test_dividir_b_zero():
#     response = client.get('/dividir?a=4&b=0')
#     assert response.status_code == 400
#     assert response.json() == {"error": "b cannot be 0 (zero)"}
