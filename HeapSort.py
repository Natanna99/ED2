import time
def heapify(lista, n, i, cont): 
    maior = i  
    esquerda = 2 * i + 1    
    direita = 2 * i + 2
    
    if esquerda < n and lista[i] < lista[esquerda]: 
        maior = esquerda 
        print(lista, 'Ordenação a esquerda')
        cont+=1
        
    if direita < n and lista[maior] < lista[direita]: 
        maior = direita
        print(lista, 'Ordenação a direita')
        cont+=1
        
        
    if maior != i: 
        lista[i],lista[maior] = lista[maior],lista[i]
        cont= heapify(lista, n, maior, cont)
        print(lista, 'Trocar as posições')
        cont+=1

    return cont

  

def heapSort(lista): 
    n = len(lista) 
    cont=0
 
    for i in range(n, -1, -1): 
        cont=heapify(lista, n, i,cont)
    
    for i in range(n-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i]   
        cont=heapify(lista, i, 0,cont)

    return cont

  


inicio= time.time()
lista = ['n', 'a','t','a','n','n','a','r','o','c','h','a']


cont= heapSort(lista)


n = len(lista)
fim= time.time()

print('----------------------------------------------')
print ("A lista classificada é") 
for i in range(n): 
    print (lista[i]),
print("total de if's: ",cont)
print("tempo de execução:", round(fim-inicio,2))
