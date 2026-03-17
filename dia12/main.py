from validaciones import pedir_entero, pedir_flotante, pedir_opcion_menu
from productos import agregar_producto, eliminar_producto, listar_productos, buscar_productos
from menu import mostrar_menu

productos = []

while True:
    mostrar_menu()
    opcion = pedir_opcion_menu()

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = pedir_flotante("Precio: $")
        stock  = pedir_entero("Stock inicial: ")
        agregar_producto(productos, nombre, precio, stock)
        print(f"✅ '{nombre}' agregado correctamente.")

    elif opcion == "2":
        nombre = input("Nombre a eliminar: ")
        if eliminar_producto(productos, nombre):
            print(f"✅ '{nombre}' eliminado correctamente.")
        else:
            print(f"⚠️  '{nombre}' no encontrado.")

    elif opcion == "3":
        listar_productos(productos)

    elif opcion == "4":
        buscar = input("Nombre a buscar: ")
        resultados = buscar_productos(productos, buscar)
        if not resultados:
            print(f"⚠️  No se encontraron productos con '{buscar}'.")
        else:
            for p in resultados:
                print(f"  {p['nombre']:<12} ${p['precio']:,.2f}   stock: {p['stock']}")

    elif opcion == "5":
        print("¡Hasta luego!")
        break
'''



### Compara el resultado
```
Dia06_07.py    → 1 archivo, 80+ líneas mezcladas
dia12/main.py  → 20 líneas, solo orquesta
'''
