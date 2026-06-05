## Sistema de recargas 

# Comandos para ejecutar cada prueba

- Python 3.12
- uv (gestor de paquetes)

# Instalar dependcias de uv
uv sync

# Tests unitarios con cobertura
uv run pytest tests/test_recarga.py -v --cov=src --cov-report=term-missing

# Tests BDD
uv run pytest tests/features/ -v

# Tests de seguridad
uv run pytest tests/security/ -v

# Todos los tests con cobertura
uv run pytest tests/ -v --cov=src --cov-report=term-missing --cov-fail-under=80

# Pruebas de rendimiento con Locust
uv run uvicorn src.api:app --host 0.0.0.0 --port 8000 &
uv run locust -f tests/performance/locustfile.py --headless -u 30 -r 5 --run-time 30s --host http://localhost:8000

## Reglas

- El monto de recarga debe estar entre $1.000 y $50.000, de lo contrario se rechaza.
- Recargas de $10.000 o más reciben un 10% de datos de bonificación.
- Recargas de $30.000 o más reciben un 25% de datos de bonificación.
- Los usuarios con plan premium obtienen un 5% adicional sobre cualquier bonificación.

# Casos de prueba 

### Tabla de casos de prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP-01 | R1 | Monto válido en rango bajo | Ninguna | monto=5000, premium=False | Llamar `calcular_recarga(5000)` | Recarga aceptada, bonificacion=0% | Positivo |
| CP-02 | R1 | Monto en límite inferior exacto | Ninguna | monto=1000 | Llamar `calcular_recarga(1000)` | Recarga aceptada | Borde |
| CP-03 | R1 | Monto en límite superior exacto | Ninguna | monto=50000 | Llamar `calcular_recarga(50000)` | Recarga aceptada | Borde |
| CP-04 | R1 | Monto por debajo del mínimo | Ninguna | monto=999 | Llamar `calcular_recarga(999)` | `MontoInvalidoError` | Negativo |
| CP-05 | R1 | Monto por encima del máximo | Ninguna | monto=50001 | Llamar `calcular_recarga(50001)` | `MontoInvalidoError` | Negativo |
| CP-06 | R2 | Monto exactamente en umbral 10% | Ninguna | monto=10000 | Llamar `calcular_recarga(10000)` | bonificacion=10% | Borde |
| CP-07 | R2 | Monto justo antes del umbral 10% | Ninguna | monto=9999 | Llamar `calcular_recarga(9999)` | bonificacion=0% | Borde |
| CP-08 | R3 | Monto exactamente en umbral 25% | Ninguna | monto=30000 | Llamar `calcular_recarga(30000)` | bonificacion=25% | Borde |
| CP-09 | R3 | Monto justo antes del umbral 25% | Ninguna | monto=29999 | Llamar `calcular_recarga(29999)` | bonificacion=10% | Borde |
| CP-10 | R4 | Usuario premium suma 5% adicional | Ninguna | monto=10000, premium=True | Llamar `calcular_recarga(10000, True)` | bonificacion=15% | Positivo |
| CP-11 | R4 | Premium sin bonificación base | Ninguna | monto=5000, premium=True | Llamar `calcular_recarga(5000, True)` | bonificacion=5% | Positivo |
| CP-12 | R4 | Premium con bonificación 25% | Ninguna | monto=30000, premium=True | Llamar `calcular_recarga(30000, True)` | bonificacion=30% | Positivo |



