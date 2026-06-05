class MontoInvalidoError(Exception):
    pass


def _validar_monto(monto: int | float) -> None:
    if monto < 1000 or monto > 50000:
        raise MontoInvalidoError("El monto debe estar entre $1.000 y $50.000")


def _calcular_bonificacion(monto: int | float, premium: bool) -> int:
    if monto >= 30000:
        bonificacion = 25
    elif monto >= 10000:
        bonificacion = 10
    else:
        bonificacion = 0

    if premium:
        bonificacion += 5

    return bonificacion


def calcular_recarga(monto: int | float, premium: bool = False) -> dict:
    _validar_monto(monto)
    bonificacion_pct = _calcular_bonificacion(monto, premium)
    return {
        "monto": monto,
        "bonificacion_pct": bonificacion_pct,
    }