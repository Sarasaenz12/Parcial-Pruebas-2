import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_monto_string_es_rechazado():
    response = client.post("/recarga", json={"monto": "abc", "premium": False})
    assert response.status_code == 422


def test_monto_negativo_es_rechazado():
    response = client.post("/recarga", json={"monto": -5000, "premium": False})
    assert response.status_code == 400


def test_campo_monto_faltante_es_rechazado():
    response = client.post("/recarga", json={"premium": False})
    assert response.status_code == 422


def test_payload_vacio_es_rechazado():
    response = client.post("/recarga", json={})
    assert response.status_code == 422


def test_tipo_premium_incorrecto_es_rechazado():
    response = client.post("/recarga", json={"monto": 15000, "premium": "si"})
    assert response.status_code == 422


def test_inyeccion_sql_en_monto_es_rechazado():
    response = client.post(
        "/recarga", json={"monto": "1; DROP TABLE users;", "premium": False}
    )
    assert response.status_code == 422


def test_health_check_responde():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_monto_cero_es_rechazado():
    response = client.post("/recarga", json={"monto": 0, "premium": False})
    assert response.status_code == 400