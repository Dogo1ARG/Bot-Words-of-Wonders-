import os
from collections import Counter

direccionScript = os.path.dirname(os.path.abspath(__file__))
os.chdir(direccionScript)

listaP = []

with open('Palabras_espanol.txt', 'r', encoding='utf-8') as listaPalabras:

    for p in listaPalabras.readlines():
        if(len(p.strip()) >= 3 ):
            listaP.append(p.strip())



def generadorPalabras(letras, lista):
    palabrasClave = []
    letrasDisponibles = Counter(letras)

    for palabra in lista:
        letrasPalabra = Counter(palabra)
        valida = True

        for letra, cantidad in letrasPalabra.items():
            if letrasDisponibles[letra] < cantidad:  
                valida = False
                break

        if valida:
            palabrasClave.append(palabra)

    return palabrasClave


def main():
    letras = input("Ingrese las letras que tiene disponible: ")
    listaLetras = []
    for c in letras:
        listaLetras.append(c)

    resultado = generadorPalabras(listaLetras, listaP)

    print(resultado)




if "__main__" == __name__:
    main()