
"""
este programa eventualmente encontrara el primer numero de 
fibonnacci que tenga 1000 divisores pero ocupa alrededor de 40min
para resolver el problema
"""

a = 1
b = 1
lista_divisores = []
while len(lista_divisores) < 1000 :
    lista_enteros = []  
    fibonacci = a + b 

    a,b = b, fibonacci
    for n in range(1,fibonacci +1):
        if fibonacci % n  == 0:
            lista_divisores.append(n)
    print("Numero de fibonnacci: {} ,Numero de divisores:{}".format(fibonacci, len(lista_divisores) ))

print("numero de fibonnaci con mas  1000 divisores : {}".format(fibonacci))


