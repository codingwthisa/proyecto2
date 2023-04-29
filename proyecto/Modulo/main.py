from sistema import crear_sistema_facturacion, crear_factura
from historial import ver_historial_clientes
from guardarDatos import cargar_datos
from guardarDatos import guardar_datos

def main():
    clientes = cargar_datos()
    while True:
        print("Seleccione una opción:")
        print("1. Ingresar compra")
        print("2. Consultar facturas")
        print("3. Salir")
        
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            productos_control, antibioticos, clientes = crear_sistema_facturacion()
            crear_factura(clientes[-1], productos_control + antibioticos)
            guardar_datos(clientes)
        elif opcion == "2":
            ver_historial_clientes(clientes)
        elif opcion == "3":
            break
        else:
            guardar_datos(clientes)
            print("Opción inválida, por favor intente de nuevo")

main()

