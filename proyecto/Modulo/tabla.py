from datetime import datetime
from typing import List
from prettytable import PrettyTable
from claseCliente import Cliente
from claseProducto import Producto
from claseFactura import Factura

def crear_factura(cliente: Cliente, productos: List[Producto]) -> None:
    # Se crea la tabla para la factura
    table = PrettyTable()
    table.field_names = ["Producto", "Tipo", "Cliente", "Cédula", "Fecha de la compra", "Total"]

    # Se agregan los productos comprados a la tabla
    for producto in productos:
        table.add_row([producto.nombre, producto.__class__.__name__, cliente.nombre, cliente.cedula, cliente.fecha_pedido, producto.valor])
    
    print(table)
    print(f"Valor total de la compra: {sum([producto.valor for producto in productos])}")

    # se crea la factura
    factura = Factura(cliente, elementos_facturados=[], productos=[], fecha_compra=datetime.now())
    for producto in productos:
        factura.agregar_producto(producto)

    # se agrega la factura a la lista de facturas del cliente
    cliente.agregar_factura(factura)




