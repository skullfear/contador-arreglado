#la clase sitemanumerico cuenta 10 veces desde un limite inicial, luego convierte este conteo en el sistema deseado por el usuario
class SistemaNumerico:
    def __init__(self, sistema, valor):
        self.sistema = sistema
        self.valor = valor

    def avanzar(self):
        self.valor += 1

    def obtener_valor(self):
        if self.sistema == 'binario':
            return bin(self.valor)[2:]
        elif self.sistema == 'octal':
            return oct(self.valor)[2:]
        elif self.sistema == 'hexadecimal':
            return hex(self.valor)[2:]
        elif self.sistema == 'decimal':
            return str(self.valor)
        else:
            return "Sistema no válido"
#interaccion con el usuario
print("¡Hola, bienvenido!")

sistema_seleccionado = input("Seleccione un sistema (binario, hexadecimal, octal o decimal): ").lower()
valor_inicial = int(input(f"Ingrese un valor inicial en el sistema {sistema_seleccionado}: "))

contador = SistemaNumerico(sistema_seleccionado, valor_inicial)

for _ in range(10):
    print("Contador en", sistema_seleccionado + ":", contador.obtener_valor())
    contador.avanzar()
