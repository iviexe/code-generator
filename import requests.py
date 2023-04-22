import random

def generar_codigo():
    codigo = ''
    for i in range(4):
        for j in range(4):
            codigo += str(random.randint(0, 9))
        codigo += '-'
    return codigo[:-1]

cantidad_codigos = int(input("Ingrese la cantidad de códigos que desea generar: "))

for i in range(cantidad_codigos):
    print(generar_codigo())
