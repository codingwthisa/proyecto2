from claseAntibiotico import Antibiotico
from claseCliente import Cliente
from clasePlagas import ControlPlagas
from claseFertilizantes import ControlFertilizantes
from tabla import crear_factura
from typing import List

productos_control_plagas, productos_control_fertilizantes, productos_antibioticos = [], [], []

def crear_sistema_facturacion(clientes: List[Cliente] = []) -> tuple:

    productos_control = []
    antibioticos = []
 
    while True:
        print("¿Qué tipo de producto desea agregar?")
        print("1. Control de Plagas")
        print("2. Control de Fertilizantes")
        print("3. Antibióticos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación del producto: ")
            valor = float(input("Ingrese el valor del producto: "))
            periodo_carencia = input("Ingrese el periodo de carencia del producto: ")

            producto = ControlPlagas(frecuencia_aplicacion, nombre, periodo_carencia, valor)



            productos_control.append(producto)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación del producto: ")
            valor = float(input("Ingrese el valor del producto: "))
            fecha_ultima_aplicacion = input("Ingrese la fecha de la última aplicación del producto: ")

            producto = ControlFertilizantes(frecuencia_aplicacion, nombre, fecha_ultima_aplicacion, valor)

            productos_control.append(producto)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del antibiótico: ")
            dosis = int(input("Ingrese la dosis del antibiótico (entre 400 y 600 Kg): "))
            if dosis < 400 or dosis > 600:
                print("La dosis ingresada no está dentro del rango válido")
                continue
            tipo_animal = input("Ingrese el tipo de animal al que se le puede aplicar el antibiótico (Bovinos, caprinos o porcinos): ")
            valor = float(input("Ingrese el precio del antibiótico: "))
            dosis_recomendada = input("Ingrese la dosis recomendada del antibiótico: ")

            producto = Antibiotico(nombre, dosis, tipo_animal, valor, dosis_recomendada)

            antibioticos.append(producto)

        elif opcion == "4":
            break

    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        fecha_pedido = input("Ingrese la fecha del pedido (en formato ddmmyyyy): ")

        cliente = Cliente(nombre, cedula, fecha_pedido)
        clientes.append(cliente)

        otra_compra = input("¿El cliente realizó otra compra? (S/N): ")
        if otra_compra.upper() == "N":
            break

    return productos_control, antibioticos, clientes

if __name__ == '__main__':
    productos_control, antibioticos, clientes = crear_sistema_facturacion()
    # se combinan los productos de los tres tipos en una sola lista
    productos = productos_control + antibioticos 
    # se crea una factura para el último cliente ingresado
    crear_factura(clientes[-1], productos)
    # preguntar al usuario si desea ver el historial de clientes
    # guardar los clientes en un archivo JSON


  






