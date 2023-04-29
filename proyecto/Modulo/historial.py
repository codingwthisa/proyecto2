from typing import List
from prettytable import PrettyTable
from claseFertilizantes import ControlFertilizantes
from clasePlagas import ControlPlagas
from claseCliente import Cliente
from claseAntibiotico import Antibiotico

def ver_historial_clientes(clientes: List[Cliente]) -> None:
    # mostrar tabla con nombres de clientes
    table = PrettyTable()
    table.field_names = ["Nombre", "Cédula"]
    for cliente in clientes:
        table.add_row([cliente.nombre, cliente.cedula])
    print(table)

    # pedir al usuario que seleccione un cliente
    nombre_cliente = input("Ingrese el nombre del cliente que desea ver su historial de compras: ")

    # buscar el cliente seleccionado y mostrar su historial de compras
    for cliente in clientes:
        if cliente.nombre == nombre_cliente:
            print(f"Historial de facturas para el cliente {cliente.nombre}:")
            productos_facturados = []
            for factura in cliente.facturas:
                for producto in factura.productos:
                    if isinstance(producto, Antibiotico):
                        productos_facturados.append("Antibiotico")
                    elif isinstance(producto, ControlPlagas):
                        productos_facturados.append("ControlPlagas")
                    elif isinstance(producto, ControlFertilizantes):
                        productos_facturados.append("ControlFertilizantes")

            if "Antibiotico" in productos_facturados:
                table = PrettyTable()
                table.field_names = ["Cliente", "Cédula", "Producto", "Tipo", "Dosis", "Dosis recomendada", "Animal", "Fecha de la compra", "Total"]
                for factura in cliente.facturas:
                    for producto in factura.productos:
                        if isinstance(producto, Antibiotico):
                            table.add_row([cliente.nombre, cliente.cedula, producto.nombre, producto.__class__.__name__, producto.dosis, producto.dosis_recomendada, producto.tipo_animal, factura.fecha_compra, producto.valor])
                print(table)
            
            if "ControlFertilizantes" in productos_facturados:
                table = PrettyTable()
                table.field_names = ["Cliente", "Cédula", "Producto", "Tipo", "Frecuencia de aplicacion", "Periodo de carencia", "Fecha de la compra", "Total"]
                for factura in cliente.facturas:
                    for producto in factura.productos:
                        if isinstance(producto, ControlPlagas):
                            table.add_row([cliente.nombre, cliente.cedula, producto.nombre, producto.__class__.__name__, producto.frecuencia_aplicacion, producto.periodo_carencia, factura.fecha_compra, producto.valor])
                print(table)
                
            if "ControlPlagas" in productos_facturados:
                table = PrettyTable()
                table.field_names = ["Cliente", "Cédula", "Producto", "Tipo", "Frecuencia de aplicacion", "Fecha de última aplicación", "Fecha de la compra", "Total"]
                for factura in cliente.facturas:
                    for producto in factura.productos:
                        if isinstance(producto, ControlFertilizantes):
                            table.add_row([cliente.nombre, cliente.cedula, producto.nombre, producto.__class__.__name__, producto.frecuencia_aplicacion, producto.fecha_ultima_aplicacion, factura.fecha_compra, producto.valor])
                print(table)
        else:
            print("El cliente ingresado no existe.")



