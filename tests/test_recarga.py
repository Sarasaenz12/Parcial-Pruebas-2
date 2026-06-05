import pytest
from src.recarga import calcular_recarga, MontoInvalidoError


def test_monto_por_debajo_del_minimo():
    with pytest.raises(MontoInvalidoError):
        calcular_recarga(999)


def test_monto_por_encima_del_maximo():
    with pytest.raises(MontoInvalidoError):
        calcular_recarga(50001)