import os

class Transportadora:
    def __init__(self):
        self.despachos = {}
        self.numero_despacho = 1
    
    def registro_salida(self, placa, descripcion_vehiculo, nombre_conductor, contacto_conductor, ruta, descripcion_carga):
        self.despachos[self.numero_despacho] = {
            'Placa del vehículo': placa,
            'Descripción del vehículo': descripcion_vehiculo,
            'Nombre del conductor': nombre_conductor,
            'Contacto del conductor': contacto_conductor,
            'Ruta': ruta,
            'Descripción de la carga': descripcion_carga
        }
        self.numero_despacho += 1
    
    def mostrar_salida(self):
        for numero_despacho, despacho_info in self.despachos.items():
            print(f"Despacho número: {numero_despacho}")
            for clave, valor in despacho_info.items():
                print(f"{clave}: {valor}")
            print("=" * 50)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    transportadora = Transportadora()
    
    while True:
        clear_console()
        print("1. Registrar salida")
        print("2. Mostrar salidas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            placa = input("Ingrese la placa del vehículo: ")
            descripcion_vehiculo = input("Ingrese la descripción del vehículo: ")
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            contacto_conductor = input("Ingrese el contacto del conductor: ")
            ruta = input("Ingrese la ruta: ")
            descripcion_carga = input("Ingrese la descripción de la carga: ")
            
            transportadora.registro_salida(placa, descripcion_vehiculo, nombre_conductor, contacto_conductor, ruta, descripcion_carga)
            print("¡Salida registrada exitosamente!\n")
            input("Presione Enter para continuar...")
        
        elif opcion == '2':
            if transportadora.despachos:
                print("=== Salidas registradas ===")
                transportadora.mostrar_salida()
                input("Presione Enter para continuar...")
            else:
                print("No hay salidas registradas aún.\n")
                input("Presione Enter para continuar...")
        
        elif opcion == '3':
            print("Gracias por sapo")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()
