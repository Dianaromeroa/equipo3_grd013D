#FUNCIONES
def datos_gabriel():
    print("Mi nombre es Gabriel y tengo 24 años")

def datos_diana():
    print("Mi nombre es Diana Romero y tengo 28 años")

def datos_ronald():
    print("Mi nombre es Ronald Troncoso y tengo 25 años")

# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_gabriel()
    elif op == "2":
        datos_diana()
    elif op == "3":
        datos_ronald()
    else:
        print(" Opción inválida.")
