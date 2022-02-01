#Ejercicio1
import pdb
pdb.set_trace()

lista = [[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]]
def maximo_lista():
    maximos = [max(lista[i]) for i in range(len(lista))]
    return maximos
print(maximo_lista())

#Ejercicio2
def primo(n):
    for i in range(2,n):
        if i > 1 and n % i == 0:
            return False
    return True
numeros = [3,4,8,5,5,22,13]
primos = list(filter(primo,numeros))
print(primos)