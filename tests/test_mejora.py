from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_cantidad_por_defecto():
    respuesta = cliente.get("/api/preguntas")
    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 5


def test_cantidad_especificada():
    respuesta = cliente.get("/api/preguntas", params={"cantidad": 2})
    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 2


def test_cantidad_fuera_de_rango():
    for cantidad in (0, 6):
        respuesta = cliente.get("/api/preguntas", params={"cantidad": cantidad})
        assert respuesta.status_code == 422
