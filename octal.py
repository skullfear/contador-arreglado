class Octal:
    def __init__(self, valor):
        self.valor = valor

    def avanzar(self):
        self.valor += 1

    def obtener_valor(self):
        return oct(self.valor)