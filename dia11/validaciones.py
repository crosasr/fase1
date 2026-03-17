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