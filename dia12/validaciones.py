def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("⚠️  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️  Ingresa solo números enteros.")

def pedir_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("⚠️  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️  Ingresa solo números.")

def pedir_opcion_menu(total_opciones=5):
    opciones_validas = [str(i) for i in range(1, total_opciones + 1)]
    while True:
        opcion = input("Elige una opción: ")
        if opcion in opciones_validas:
            return opcion
        print(f"⚠️  Opción no válida (1-{total_opciones})")