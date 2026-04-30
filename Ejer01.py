def convertir_temperatura(valor, unidad_origen, unidad_destino):
    # Primero convertimos todo a Celsius
    if unidad_origen == "C":
        celsius = valor
    elif unidad_origen == "K":
        celsius = valor - 273.15
    elif unidad_origen == "F":
        celsius = (valor - 32) * 5/9
    else:
        raise ValueError("Unidad de origen no válida. Use 'C', 'K' o 'F'.")

    # Ahora convertimos desde Celsius a la unidad destino
    if unidad_destino == "C":
        return celsius
    elif unidad_destino == "K":
        return celsius + 273.15
    elif unidad_destino == "F":
        return (celsius * 9/5) + 32
    else:
        raise ValueError("Unidad de destino no válida. Use 'C', 'K' o 'F'.")


# Programa principal
valor = float(input("Ingrese el valor de la temperatura: "))
unidad_origen = input("Ingrese la unidad de origen (C/K/F): ").upper()
unidad_destino = input("Ingrese la unidad de destino (C/K/F): ").upper()

resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
print(f"{valor} {unidad_origen} equivalen a {resultado:.2f} {unidad_destino}")