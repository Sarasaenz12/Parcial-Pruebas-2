import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.recarga import calcular_recarga, MontoInvalidoError

scenarios("recarga.feature")


@pytest.fixture
def contexto():
    return {"monto": None, "premium": False, "resultado": None, "error": None}


@given(parsers.parse("que el usuario intenta recargar con un monto de {monto:d}"))
def dado_monto(contexto, monto):
    contexto["monto"] = monto
    contexto["premium"] = False


@given(parsers.parse("que el usuario premium intenta recargar con un monto de {monto:d}"))
def dado_monto_premium(contexto, monto):
    contexto["monto"] = monto
    contexto["premium"] = True


@when("se procesa la recarga")
def cuando_procesar(contexto):
    try:
        contexto["resultado"] = calcular_recarga(contexto["monto"], contexto["premium"])
        contexto["error"] = None
    except MontoInvalidoError as e:
        contexto["resultado"] = None
        contexto["error"] = e


@then("el sistema rechaza la recarga con un error de monto inválido")
def entonces_error(contexto):
    assert contexto["error"] is not None
    assert isinstance(contexto["error"], MontoInvalidoError)


@then(parsers.parse("la bonificación aplicada es del {bonificacion:d}%"))
def entonces_bonificacion(contexto, bonificacion):
    assert contexto["resultado"] is not None
    assert contexto["resultado"]["bonificacion_pct"] == bonificacion