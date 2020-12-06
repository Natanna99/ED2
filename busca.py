import random
def busca(lista, a):
    cont=0
    for i in lista:
        cont=cont+1
        if i == a:
           return cont

lista = [12, 24, 25, 33, 37, 48, 57, 86, 92]
print(busca(lista, 48))


def busca(lista, a):
    cont=0
    for i in lista:
        cont=cont+1
        if i > a:
           return "nn esta na lista"
        if i== a:
            return "esta na lista"

print(busca(lista, 38))

lista1 = [12, 24, 25, 33, 37, 48, 57, 86, 92]

lista= [10, 20, 30, 40, 50, 60, 70, 80]
def busca_binaria(lista, a):
    i = 0
    f = len(lista)-1
    b= int(i + ((f - i) * ((a - lista[i])/(lista[f]-lista[i]))))
    vezes = 0
    cont = 0

    print(b, "-----")
    while cont <= f:
        vezes = vezes +1
        if lista[b] == a:
            return("achou com ", vezes," verificação")
            
        else:
            if lista[b] > a:
                print(lista[b])
                f = b-1
            else:
                print(lista[b])
                i = b+1
        cont = cont + 1
        b = int(i + ((f - i) * ((a - lista[i])/(lista[f]-lista[i]))))
        print(b)
    return "nn achei"


print(busca_binaria(lista, 20))




