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

# Cliente
class Cliente:
    def __init__(self, nombre, correo_electronico, nit):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.nit = nit

    def __str__(self):
        return f"Nombre: {self.nombre}, NIT: {self.nit}, Correo: {self.correo_electronico}"

# Compra
class Compra:
    contador_id = 1
    
    def __init__(self, cliente):
        self.id = Compra.contador_id
        Compra.contador_id += 1
        self.cliente = cliente
        self.lista_productos = []
        self.costo_total = 0.0

    def agregar_auto(self, auto, seguro=False):
        self.lista_productos.append(auto)
        if seguro:
            self.costo_total += auto.precio_unitario * 1.15  # si el carro tiene s 
        else:
            self.costo_total += auto.precio_unitario  # si no tiene s

    def __str__(self):
        autos_info = "\n".join([str(auto) for auto in self.lista_productos])
        return f"Compra ID: {self.id}\nCliente: {self.cliente}\nAutos:\n{autos_info}\nTotal: Q{self.costo_total:.2f}"
autos = []
clientes = []
compras = []

def mostrar_menu():
    print("\n------------- Menú Principal -------------")
    print("1. Registrar Auto")
    print("2. Registrar Cliente")
    print("3. Realizar Compra")
    print("4. Reporte de Compras")
    print("5. Datos del Estudiante")
    print("6. Salir")
    print("------------------------------------------")
