#=============================================================
#Exercício Número 3:

#Lógica dos números ímpares:
def logica_a() -> list:

    numeros = range(1,30)
    numeros_impares = []

    numero_e_impar = lambda n: numeros_impares.append(n) if n % 2 != 0 else None

    for n in numeros:
        numero_e_impar(n)
    

    return numeros_impares


#Lógica dos números com base dois:
def logica_b():

    n = 2
    i = 1

    base_dois = []

    while i < 8:
        r = n**i
        i += 1
        
        base_dois.append(r)
    
    return base_dois

#Lógica de números ao quadrado:
def logica_c():
    resposta = []

    for n in range(0,10):
        quad = n*n
        resposta.append(quad)

    return resposta

#Lógica de números pares ao quadrado:
def logica_d():

    resposta = []

    numeros = range(0,11)
    numeros_pares = []
    e_par = lambda n: True if n%2 == 0 else False

    for n in numeros:
        if e_par(n) == True:
            numeros_pares.append(n)
        else:
            pass

    for i in numeros_pares:
        r = i**2
        resposta.append(r)

    
    return resposta

    pass

#Lógica da sequência de Fibonacci:
def logica_e():
    a = 0
    b = 1

    sequencia_fibonacci = [a, b]

    for i in range(1,10):
        a, b = b, a + b

        sequencia_fibonacci.append(b)

    return sequencia_fibonacci

def logica_f():

    #Não entendi a lógica númerica desse exercício.
    pass




#=============================================================
#Bloco de execução do código:

print(logica_f())

#=============================================================