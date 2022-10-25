from math import sqrt


def desviacion_estandar(valores, media):
    suma = 0
    for valor in valores:
        suma += (valor - media) ** 2

    radicando = suma / len(valores)

    return sqrt(radicando)


def calcular_media(valores):
    suma = 0
    for valor in valores:
        suma += valor

    return suma / len(valores)


# valores = [7, 3, 13, 17, 10, 8, 12, 9]
nNumber = int(input("Enter the number of elements to insert: "))
valores = []

for i in range(0, nNumber):
    valor = int(input("Enter the value: "))
    valores.append(valor)

media = calcular_media(valores)
desviacion = desviacion_estandar(valores, media)

print(desviacion)
