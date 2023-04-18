def serie_fibonacci(number):
    lista_fibonacci= [0,1]
    suma=1
    if number== 0:
        return 0
    if (len(lista_fibonacci)) != number:
        for lista in range(1,number-1):
            suma= (lista_fibonacci[-2] + lista_fibonacci[-1])
            lista_fibonacci.append(suma)
            suma_lista= (lista_fibonacci[-2]+lista_fibonacci[-1])
        return suma_lista
    else: 
        return sum( lista_fibonacci)