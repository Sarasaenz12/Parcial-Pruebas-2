class MontoInvalidoError(Exception):
    pass

def _validar_monto(monto: int | float) -> None:
    if monto < 1000 or monto > 50000:
        raise MontoInvalidoError("El monto debe estar entre $1.000 y $50.000")

def calcular_recarga(monto: int | float, premium: bool = False):
    _validar_monto(monto)