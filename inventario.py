Inventario=[
        ["coca", 1500, 4],
        ["pepitos", 400, 6],
        ["lays", 78, 10],
        ["milka", 56, 3]
]
    
def cargar_productos():
    seguir="si"
    while seguir=="si":
        nombre= input("Ingrese el nombre del producto: ")
        precio= int(input("Ingrese el precio del producto: "))
        cantidad= int(input("Ingrese el cantidad del producto: "))
        Inventario.append([nombre, precio, cantidad])

        seguir=input("Desea seguir ingresando si/no: ").lower()

def buscar_producto(Inventario):
    while Inventario != []:
        busqueda= input("Ingrese lo buscado: ")
    
        for i in range(len(Inventario)):
            if busqueda == Inventario[i][0]:
                print(f"Nombre: {Inventario[i][0]}, Precio: {Inventario[i][1]}, Cantidad: {Inventario[i][2]}")
                return 
        print("El producto no está en stock")

def ordernar_inventario(Inventario):
    n = len(Inventario)
    for i in range(n):       
        for j in range(0,n-1-i): 
            if Inventario[j][1] > Inventario[j+1][1]:
                Inventario[j], Inventario[j+1] = Inventario[j+1], Inventario[j]
    for k in range(n):
        print(f"Precio: {Inventario[k][1]}")

def producto_mas_caro(Inventario):
    mayor=0
    for i in range(len(Inventario)):
        if Inventario[i][1] > mayor:
            mayor= Inventario[i][1]
            producto_mayor= Inventario[i][0]
    print(f"Producto mas caro: {producto_mayor}")

def producto_mas_barato(Inventario):
    menor= float('inf')
    for i in range(len(Inventario)):
        if Inventario[i][1] < menor:
            menor= Inventario[i][1]
            producto_menor= Inventario[i][0]
    print(f"Producto mas barato: {producto_menor}")