class MontoInvalidoError(Exception):
    pass


def calcular_recarga(monto, premium=False):
    if monto < 1000 or monto > 50000:
        raise MontoInvalidoError("El monto debe estar entre $1.000 y $50.000")