class MontoInvalidoError(Exception):
    pass

MONTO_MINIMO = 1000
MONTO_MAXIMO = 50000
UMBRAL_BONIFICACION_MEDIA = 10000
UMBRAL_BONIFICACION_ALTA = 30000
BONIFICACION_MEDIA = 10
BONIFICACION_ALTA = 25
BONIFICACION_PREMIUM = 0


def _validar_monto(monto: int | float) -> None:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise MontoInvalidoError(
            f"El monto debe estar entre ${MONTO_MINIMO:,} y ${MONTO_MAXIMO:,}"
        )


def _calcular_bonificacion(monto: int | float, premium: bool) -> int:
    """Calcula el porcentaje de bonificación según el monto y el plan."""
    if monto >= UMBRAL_BONIFICACION_ALTA:
        bonificacion = BONIFICACION_ALTA
    elif monto >= UMBRAL_BONIFICACION_MEDIA:
        bonificacion = BONIFICACION_MEDIA
    else:
        bonificacion = 0

    if premium:
        bonificacion += BONIFICACION_PREMIUM

    return bonificacion


def calcular_recarga(monto: int | float, premium: bool = False) -> dict:
    _validar_monto(monto)
    bonificacion_pct = _calcular_bonificacion(monto, premium)
    return {
        "monto": monto,
        "bonificacion_pct": bonificacion_pct,
    }

