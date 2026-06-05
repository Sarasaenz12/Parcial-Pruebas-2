import pytest
from src.recarga import calcular_recarga, MontoInvalidoError


def test_monto_por_debajo_del_minimo():
    with pytest.raises(MontoInvalidoError):
        calcular_recarga(999)


def test_monto_por_encima_del_maximo():
    with pytest.raises(MontoInvalidoError):
        calcular_recarga(50001)

def test_monto_valido_rango_bajo():
    resultado = calcular_recarga(5000)
    assert resultado["monto"] == 5000
    assert resultado["bonificacion_pct"] == 0

def test_limite_inferior_exacto():
    resultado = calcular_recarga(1000)
    assert resultado["monto"] == 1000
    assert resultado["bonificacion_pct"] == 0

def test_limite_superior_exacto():
    resultado = calcular_recarga(50000)
    assert resultado["monto"] == 50000
    assert resultado["bonificacion_pct"] == 25

def test_umbral_bonificacion_10_exacto():
    resultado = calcular_recarga(10000)
    assert resultado["monto"] == 10000
    assert resultado["bonificacion_pct"] == 10

def test_justo_antes_umbral_10():
    resultado = calcular_recarga(9999)
    assert resultado["monto"] == 9999
    assert resultado["bonificacion_pct"] == 0