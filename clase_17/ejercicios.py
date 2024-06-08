"""
Crear una calculadora que simule préstamos. Para simular el préstamo se debe tener el monto inicial, la tasa de interés anual y los períodos del préstamo. La calculadora debe calcular el interés simple, el interés compuesto, el valor final del préstamo y las tasas mensual y diarias.
"""

class Calculadora_prestamos:
    def __init__(self, monto_inicial, tasa_interes_anual, periodos):
        self.monto_inicial = monto_inicial
        self.tasa_interes_anual = tasa_interes_anual
        self.periodos = periodos
        
    def calcular_interes_simple(self):
        interes_simple = self.monto_inicial * self.tasa_interes_anual * self.periodos - self.monto_inicial
        return interes_simple
    
    def calcular_interes_compuesto(self):
        interes_compuesto = self.monto_inicial * (1 + self.tasa_interes_anual) ** self.periodos - self.monto_inicial
        return interes_compuesto
    
    def valor_final_prestamo(self):
        valor_futuro = self.monto_inicial * (1 + self.tasa_interes_anual) ** self.periodos
        return valor_futuro
    
    def tasa_mensual(self):
        tasa_mes = self.tasa_interes_anual / 12
        return tasa_mes
    
    def tasa_diaria(self):
        tasa_dia = self.tasa_interes_anual / 365
        return tasa_dia
    
    
monto_inicial = 1000
tasa_interes_anual = 0.08  # 8% de tasa de interés anual
periodos = 5

calculadora = Calculadora_prestamos(monto_inicial, tasa_interes_anual, periodos)
tasa_mensual = calculadora.tasa_mensual()
tasa_diaria = calculadora.tasa_diaria()

valor_final = calculadora.valor_final_prestamo()

print(f"Tasa de interés mensual: {tasa_mensual:.4f}")
print(f"Tasa de interés diaria: {tasa_diaria:.6f}")
print(f"Valor final del préstamo: {valor_final}")
