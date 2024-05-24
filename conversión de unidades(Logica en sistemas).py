'''Elabore un programa para realizar las operaciones
de conversión de unidades, para longitud entre Millas y Kilómetros.
Volumen entre m3 y pie3, Longitud entre pies, metros y yardas.

'''
#Deberá contar con un menú  en el cual se escoja cuál tipo de conversión desea solicitar,
def menu():
    print("\nmenú de Conversión")
    print("que tipo de conversión deseas hacer:\n")
    print("1. Millas y Kilómetros")
    print("2. Metros Cúbicos y Pies Cúbicos")
    print("3. Pies, Metros y Yardas")
    print("4. Terminar Ejercicio")

def convertir_km_m(opcion):
    if opcion == 1:
        millas = float(input("Escriba la distancia en millas: "))
        kilometros = millas * 1.60934
        print(f"La distancia en kilómetros es: {kilometros:.2f}")
        
    elif opcion == 2:
        kilometros = float(input("Escriba la distancia en kilómetros: "))
        millas = kilometros / 1.60934
        print(f"La distancia en Millas es: {millas:.2f}")

    else:
        print("\nEl múmero que ingrsaste no es valido.")


def convertir_v_p_3(opcion):
    if opcion == 1:
        metros_cubicos = float(input("Escriba el volumen en metros cúbicos: "))
        pies_cubicos = metros_cubicos * 35.314
        print(f"El volumen en pies cúbicos es: {pies_cubicos:.2f}")

    elif opcion == 2:
        pies_cubicos = float(input("Escriba el volumen en pies cúbicos: "))
        metros_cubicos = pies_cubicos / 35.314
        print(f"El volumen en metros cúbicos es: {metros_cubicos:.2f}")

    else:
        print("\nEl múmero que ingrsaste no es valido.")


def convertir_p_m_y(opcion):
    if opcion == 1:
        metros = float(input("Escriba la distancia en metros: "))
        pies = metros * 3.28084
        print(f"La distancia en pies es: {pies:.2f}")

    elif opcion == 2:
        pies = float(input("Escriba la distancia en pies: "))
        metros = pies / 3.28084
        print(f"La distancia en metros es: {metros:.2f}")

    elif opcion == 3:
        yardas = float(input("Escriba la distancia en yardas: "))
        metros = yardas * 0.9144
        print(f"La distancia en metros es: {metros:.2f}")

    else:
        print("\nEl múmero que ingrsaste no es valido.")


while True:
    menu()
    opcion = int(input("\nElige una opción: "))
    if opcion == 1:
        print("\n1. Millas a Kilómetros")
        print("2. Kilómetros a Millas")
        opcion = int(input("\nElige una conversión: "))
        convertir_km_m(opcion)  

    elif opcion == 2:
        print("\n1. Metros Cúbicos a Pies Cúbicos")
        print("2. Pies Cúbicos a Metros Cúbicos")
        opcion = int(input("\nElige una conversión: "))
        convertir_v_p_3(opcion)

    elif opcion == 3:
        print("\n1. Metros a Pies")
        print("2. Pies a Metros")
        print("3. Yardas a Metros")
        opcion = int(input("\nElige una conversión: "))
        convertir_p_m_y(opcion)

    elif opcion == 4:
        break

    else:
        print("\nEsta opción no es valida.")