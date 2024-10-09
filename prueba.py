from menu import *
from inventario import *

#La Empresa “Empire Inventory” necesita desarrollar un sistema de administración de
#productos para sus almacenes. Para cada producto se almacenará:
#• Nombre del producto.
#• Precio del producto.
#• Cantidad del producto.
#La información de los productos se almacenará en un arreglo bidimensional, donde cada fila
#representara un producto y las columnas contendrán los datos mencionados.
#Requerimientos:
#El sistema deberá constar de los siguientes puntos:
#1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
#• Cargar producto/s.
#• Buscar producto.
#• Ordenar inventario.
#• Mostrar producto más caro y más barato.
#• Mostrar productos con precio mayor a 15000.
#• Salir
#2. Cargar inventario:
#• Desarrollar una función que permita al usuario ingresar los datos del o los
#productos en una matriz (nombre, precio, cantidad).
#• El sistema debe permitir al usuario ingresar la cantidad deseada de productos.
#3. Buscar producto:
#• Implementar un algoritmo de búsqueda que permita al usuario encontrar un
#producto específico por su nombre y muestre por pantalla todos los datos de
#ese producto (nombre, precio y cantidad).
#4. Ordenar inventario:
#• Utilizar un algoritmo de ordenamiento para ordenar los productos en función
#de su precio de manera ascendente y luego mostrar por pantalla los productos
#ordenados.
#5. Mostrar producto más caro:
#• Desarrollar una función que identifique y muestre el producto más caro del
#inventario.
#6. Mostrar producto más barato:
#• Desarrollar una función que identifique y muestre el producto más barato del
#inventario.
#Requisitos técnicos:
#▪ Utilizar funciones para cada una de las operaciones mencionadas.
#▪ Mantener una estructura de código limpia y bien comentada.
#▪ Si el usuario selecciona cualquier opción sin que existan productos registrados en el
#sistema, aparecerá un mensaje en pantalla notificando que no hay productos
#disponibles para la operación solicitada.
#Entrega del programa

Inventario=[
        ["coca", 1500, 4],
        ["pepitos", 400, 6],
        ["lays", 78, 10],
        ["milka", 56, 3]
]
# def menu():
#     print(""" Menu Principal:
#     1.Cargar Producto/s
#     2.Buscar producto
#     3.Ordenar inventario
#     4.Mostrar producto más caro y más barato
#     5.Mostrar productos con precio mayor a 15000
#     6.Salir 
# """)
    
#2. Cargar inventario:
#• Desarrollar una función que permita al usuario ingresar los datos del o los
#productos en una matriz (nombre, precio, cantidad).
#• El sistema debe permitir al usuario ingresar la cantidad deseada de productos.

# def cargar_productos():
#     seguir="si"
#     while seguir=="si":
#         nombre= input("Ingrese el nombre del producto: ")
#         precio= int(input("Ingrese el precio del producto: "))
#         cantidad= int(input("Ingrese el cantidad del producto: "))
#         Inventario.append([nombre, precio, cantidad])

#         seguir=input("Desea seguir ingresando si/no: ").lower()

#3. Buscar producto:
#• Implementar un algoritmo de búsqueda que permita al usuario encontrar un
#producto específico por su nombre y muestre por pantalla todos los datos de
#ese producto (nombre, precio y cantidad).
# def buscar_producto():
#     while Inventario != []:
#         busqueda= input("Ingrese lo buscado: ")
    
#         for i in range(len(Inventario)):
#             if busqueda == Inventario[i][0]:
#                 print(f"Nombre: {Inventario[i][0]}, Precio: {Inventario[i][1]}, Cantidad: {Inventario[i][2]}")
#                 return 
#         print("El producto no está en stock")

#4. Ordenar inventario:
#• Utilizar un algoritmo de ordenamiento para ordenar los productos en función
#de su precio de manera ascendente y luego mostrar por pantalla los productos
#ordenados.
#Inventario=[
#    ["coca", 1500, 4],
#    ["pepitos", 400, 6],
#    ["lays", 78, 10],
#    ["milka", 56, 3]
#]
# def ordernar_inventario(Inventario):
#     n = len(Inventario)
#     for i in range(n):       
#         for j in range(0,n-1-i): 
#             if Inventario[j][1] > Inventario[j+1][1]:
#                 Inventario[j], Inventario[j+1] = Inventario[j+1], Inventario[j]
#     for k in range(n):
#         print(f"Precio: {Inventario[k][1]}")

#5. Mostrar producto más caro:
#• Desarrollar una función que identifique y muestre el producto más caro del
#inventario.
#6. Mostrar producto más barato:
#• Desarrollar una función que identifique y muestre el producto más barato del
#inventario.
# def producto_mas_caro(Inventario):
#     mayor=0
#     for i in range(len(Inventario)):
#         if Inventario[i][1] > mayor:
#             mayor= Inventario[i][1]
#             producto_mayor= Inventario[i][0]
#     print(f"Producto mas caro: {producto_mayor}")

# def producto_mas_barato(Inventario):
#     menor= float('inf')
#     for i in range(len(Inventario)):
#         if Inventario[i][1] < menor:
#             menor= Inventario[i][1]
#             producto_menor= Inventario[i][0]
#     print(f"Producto mas barato: {producto_menor}")

#1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
#• Cargar producto/s.
#• Buscar producto.
#• Ordenar inventario.
#• Mostrar producto más caro y más barato.
#• Mostrar productos con precio mayor a 15000.
#• Salir



seleccion=0
while seleccion !="6":
    menu()
    seleccion=input("Ingrese su opcion: ")
    match seleccion:
        case "1": 
            cargar_productos()
            print(Inventario)
        case "2":
            buscar_producto(Inventario)
        case "3":
            ordernar_inventario(Inventario)
        case "4": 
            producto_mas_caro(Inventario)
            producto_mas_barato(Inventario)
        case "5":
            pass
        case "6": 
            print("chaito")
        case _:
            print("error")