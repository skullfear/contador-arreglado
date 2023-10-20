
```
Jean Franco Gamboa Díaz. Codigo: 20231020074.
Linda Dayanna Niño Lasso. Codigo: 20231015106.
Juan Sebastian Hernandez Susatama. Codigo: 20231015062

En el codigo `ejemplo_refactoring.py` utilizamos las tecnicas de refactoring para unificar la logica en una sola clase utilizando la clase unica en `SistemaNumerico` para manejar todas las operaciones relacionadas con sistemas numéricos en lugar de tener clases separadas para cada sistema numérico(principio de Kiss y principio de Dry).

`codigo inicial`

class Binario:

    def __init__(self, valor):
        self.valor = valor

    def avanzar(self):
        self.valor += 1

class Octal:
    def __init__(self, valor):
        self.valor = valor

    def avanzar(self):
        self.valor += 1

class Hexadecimal:
    def __init__(self, valor):
        self.valor = valor

    def avanzar(self):
        self.valor += 1

class Decimal:
    def __init__(self, valor):
        self.valor = valor
        
    def avanzar(self):
        self.valor += 1 

`utilizando tecnicas de refactoring`

class SistemaNumerico:
    def __init__(self, sistema, valor):
        self.sistema = sistema
        self.valor = valor

    def avanzar(self):
        self.valor += 1


luego agregamos el Polimorfismo en el método `obtener_valor()`, se utiliza una estructura condicional (`if-elif-else`) para determinar el sistema numérico actual y realizar la conversión correspondiente(Principio de Dry).

`codigo inicial`
def obtener_valor(self):    
    return bin(self.valor)

def obtener_valor(self):
        return oct(self.valor)

def obtener_valor(self):
        return hex(self.valor)

def obtener_valor(self):
        return str(self.valor)

`utilizando tecnicas de refactoring`

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
 
Esto aprovecha el polimorfismo para que el método funcione de manera diferente según el sistema numérico seleccionado.
  
  
Tambien utilizamos Minimización de duplicación para eliminar la duplicación de código innecesaria al unificar las operaciones en una sola clase.Por ultimo se utilizó la  Interacción con el usuario mediante la entrada de sistemas numéricos y valores iniciales, luego muestra el contador en el sistema numérico elegido. 

`codigo inicial`

sistema_seleccionado = input("Seleccione un sistema (binario, hexadecimal, octal o decimal): ").lower()
valor_inicial = int(input(f"Ingrese un valor inicial en el sistema {sistema_seleccionado}: "))

contador = Contador(sistema_seleccionado, valor_inicial)

for _ in range(10):
    print(contador.obtener_valor()[2:])
    contador.avanzar()

`utilizando tecnicas de refactoring`

print("¡Hola, bienvenido!")

sistema_seleccionado = input("Seleccione un sistema (binario, hexadecimal, octal o decimal): ").lower()
valor_inicial = int(input(f"Ingrese un valor inicial en el sistema {sistema_seleccionado}: "))

contador = SistemaNumerico(sistema_seleccionado, valor_inicial)

for _ in range(10):
    print("Contador en", sistema_seleccionado + ":", contador.obtener_valor())
    contador.avanzar() 

```