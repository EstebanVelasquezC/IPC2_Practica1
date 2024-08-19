# Clase Auto
class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio_unitario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Precio: Q{self.precio_unitario:.2f}"