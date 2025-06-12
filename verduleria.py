productos= ["tomate", "lechuga", "cebolla", "morrón", "zanahoria"] # Cadena de caracteres
stock = [10, 5, 8, 12, 15] # numerico entero
i=0

def mostrar_stock(): #def definimos una función
    print("Stock de productos:")
    for i in range(len(productos)): #len largo de la lista productos
        print(f"{productos[i]}: {stock[i]} unidades")
    menu()

 #llamamos a la función agregar_producto

def agregar_producto():
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {nuevo_producto} a agregar: "))
    productos.append(nuevo_producto) #append agrega un elemento al final de la lista
    stock.append(cantidad) #append agrega un elemento al final de la lista stock
    mostrar_stock()
 #llamamos a la función mostrar_stock

def agregar_stock():
    producto = input("Ingrese el nombre del producto a agregar stock: ")
    if producto in productos:
       i= productos.index(producto) #index devuelve el indice del producto en la lista
       cantidad= int(input("Ingrese la cantidad a agregar: "))
       stock[i] = stock[i] + cantidad #actualiza el stock del producto
       mostrar_stock() #llamamos a la función mostrar_stock
    else:
        print("El producto no existe")
        menu()
     

def eliminar_producto():
     producto = input("Ingrese el nombre del producto a eliminar: ")
     if producto in productos:
        i=productos.index(producto) #index devuelve el indice del producto en la lista
        del productos[i] #del elimina el producto de la lista
        del stock[i]
        mostrar_stock()
     else:
        print("El producto no existe")
        menu()


def menu():  
    print("*** Bienvenido a la Verdulería ***")
    print("-----------------------------")
    print(". 1. Mostrar stock")
    print("\n. 2. Agregar producto")
    print("\n. 3. Agregar stock")
    print("\n. 4. Eliminar producto")
    print("\n. 0. Salir del programa")
    opcion = int(input("\n. Seleccione una opción: "))

    if opcion == 1:
        mostrar_stock()
    elif opcion == 2:   
        agregar_producto()
    elif opcion == 3:   
        agregar_stock()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 0:
        return
    else:
        print("Opción no válida")
        
                
menu()