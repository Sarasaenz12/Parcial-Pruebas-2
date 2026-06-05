# language: es
Característica: Cálculo de recargas de celular RecargaYa
  Como operador de RecargaYa
  Quiero calcular el valor final de una recarga
  Para aplicar correctamente las bonificaciones según las reglas de negocio

  Escenario: Recarga con monto inválido por debajo del mínimo
    Dado que el usuario intenta recargar con un monto de 999
    Cuando se procesa la recarga
    Entonces el sistema rechaza la recarga con un error de monto inválido

  Escenario: Recarga con monto inválido por encima del máximo
    Dado que el usuario intenta recargar con un monto de 50001
    Cuando se procesa la recarga
    Entonces el sistema rechaza la recarga con un error de monto inválido

  Escenario: Recarga sin bonificación para monto bajo
    Dado que el usuario intenta recargar con un monto de 5000
    Cuando se procesa la recarga
    Entonces la bonificación aplicada es del 0%

  Escenario: Recarga de usuario premium sin bonificación base
    Dado que el usuario premium intenta recargar con un monto de 5000
    Cuando se procesa la recarga
    Entonces la bonificación aplicada es del 5%

  Escenario: Recarga de usuario premium con bonificación alta
    Dado que el usuario premium intenta recargar con un monto de 30000
    Cuando se procesa la recarga
    Entonces la bonificación aplicada es del 30%

  Esquema del escenario: Bonificación según el monto de recarga
    Dado que el usuario intenta recargar con un monto de <monto>
    Cuando se procesa la recarga
    Entonces la bonificación aplicada es del <bonificacion>%

    Ejemplos:
      | monto | bonificacion |
      | 1000  | 0            |
      | 9999  | 0            |
      | 10000 | 10           |
      | 29999 | 10           |
      | 30000 | 25           |
      | 50000 | 25           |