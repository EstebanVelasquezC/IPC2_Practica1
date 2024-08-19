# Auto
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
        self.id = None
        self.cliente = cliente
        self.lista_productos = []
        self.costo_total = 0.0

    def agregar_auto(self, auto, seguro=False):
        self.lista_productos.append(auto)
        if seguro:
            self.costo_total += auto.precio_unitario * 1.15  # Con seguro
        else:
            self.costo_total += auto.precio_unitario  # Sin seguro

    def finalizar_compra(self):
        if self.costo_total > 0:
            self.id = Compra.contador_id
            Compra.contador_id += 1
            return True
        return False

    def __str__(self):
        autos_info = "\n".join([str(auto) for auto in self.lista_productos])
        return f"Compra ID: {self.id}\nCliente: {self.cliente}\nAutos:\n{autos_info}\nTotal: Q{self.costo_total:.2f}"

# Listas
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

def registrar_auto():
    placa = marca = modelo = descripcion = None
    precio_unitario = None

    while not placa:
        placa = input("Ingrese placa del auto: ").strip()
        if not placa:
            print("Campo obligatorio.")

    while not marca:
        marca = input("Ingrese la marca del auto: ").strip()
        if not marca:
            print("Campo obligatorio.")

    while not modelo:
        modelo = input("Ingrese modelo del auto: ").strip()
        if not modelo:
            print("Campo obligatorio.")

    while not descripcion:
        descripcion = input("Ingrese una descripción del auto: ").strip()
        if not descripcion:
            print("Campo obligatorio.")

    while precio_unitario is None:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del auto: Q").strip())
            if precio_unitario <= 0:
                print("Campo obligatorio.")
                precio_unitario = None
        except ValueError:
            print("El precio debe ser un número. Inténtelo de nuevo.")

    auto = Auto(placa, marca, modelo, descripcion, precio_unitario)
    autos.append(auto)
    print("\nAuto registrado exitosamente.")

def registrar_cliente():
    nombre = correo_electronico = nit = None

    while not nombre:
        nombre = input("Ingrese nombre del cliente: ").strip()
        if not nombre:
            print("Campo obligatorio.")

    while not correo_electronico:
        correo_electronico = input("Ingrese correo electrónico del cliente: ").strip()
        if not correo_electronico:
            print("Campo obligatorio.")

    while not nit:
        nit = input("Ingrese NIT del cliente: ").strip()
        if not nit:
            print("Campo obligatorio.")

    cliente = Cliente(nombre, correo_electronico, nit)
    clientes.append(cliente)
    print("\nCliente registrado exitosamente.")

def realizar_compra():
    nit_cliente = input("Ingrese NIT del cliente: ")
    cliente = next((c for c in clientes if c.nit == nit_cliente), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    compra = Compra(cliente)
    
    while True:
        print(f"\n------------- Menú Compra -------------\n{cliente.nombre}")
        print("1. Agregar Auto")
        print("2. Terminar Compra")
        print("----------------------------------------")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            placa = input("Ingrese placa del auto a comprar: ")
            auto = next((a for a in autos if a.placa == placa), None)
            
            if not auto:
                print("Auto no encontrado.")
                continue
            
            seguro = input("¿Desea agregar seguro al auto? (si/no): ").lower() == "si"
            compra.agregar_auto(auto, seguro)
            print("Auto agregado a la compra.")
        
        elif opcion == "2":
            if compra.finalizar_compra():
                compras.append(compra)
                print(f"Compra realizada exitosamente. Total: Q{compra.costo_total:.2f}")
            else:
                print("Compra cancelada, ningún auto seleccionado.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

def reporte_compras():
    if not compras:
        print("No se han realizado compras.")
        return
    
    print("\n------------- REPORTE DE COMPRAS -------------")
    total_general = 0.0
    
    for compra in compras:
        print(compra)
        print("===============================================")
        total_general += compra.costo_total
    
    print(f"Total General: Q{total_general:.2f}")
    print("---------------------------------------------")

def datos_estudiante():
    print("Nombre: Rogelio Esteban Velasquez Castillo")
    print("Carnet: 202200387")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_auto()
        elif opcion == "2":
            registrar_cliente()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            reporte_compras()
        elif opcion == "5":
            datos_estudiante()
        elif opcion == "6":
            print("Cerrando programa. ¡Feliz día!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()


