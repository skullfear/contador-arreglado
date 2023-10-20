from binario import Binario
from hexadecimal import Hexadecimal
from octal import Octal
from decimal_1 import Decimal

class Contador:
    def __init__(self, sistema, valor_inicial):
        self.sistema = sistema
        if sistema == 'binario':
            self.numero = Binario(valor_inicial)
        elif sistema == 'hexadecimal':
            self.numero = Hexadecimal(valor_inicial)
        elif sistema == 'octal':
            self.numero = Octal(valor_inicial)
        elif sistema == 'decimal':
            self.numero = Decimal(valor_inicial)

    def avanzar(self):
        self.numero.avanzar()

    def obtener_valor(self):
        return self.numero.obtener_valor()


# Solicitar al usuario que seleccione el sistema y el valor inicial
sistema_seleccionado = input("Seleccione un sistema (binario, hexadecimal, octal o decimal): ").lower()
valor_inicial = int(input(f"Ingrese un valor inicial en el sistema {sistema_seleccionado}: "))

contador = Contador(sistema_seleccionado, valor_inicial)

for _ in range(10):
    print(contador.obtener_valor()[2:])
    contador.avanzar()

