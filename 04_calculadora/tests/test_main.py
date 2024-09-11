from fastapi.testclient import TestClient
from calculadora.main import app

client = TestClient(app)

def test_somar_a_b_validos():
    response = client.get('/somar?a=2&b=2')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 2, "resultado" :4 }

# def test_somar_a_invalido_b_valido():
#     response = client.get('/somar?a=2.2&b=2')
#     assert response.status_code == 400
#     assert response.json() == {"error": "[{'type': 'int_parsing', 'loc': ('query', 'a'), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': '2.2'}]"}