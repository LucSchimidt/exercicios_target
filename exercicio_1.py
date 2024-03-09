#=============================================================
#Exercício Número 1:

def exercicio_um(indice, soma) -> int:

    K = 0

    while K < indice:
        K += 1

        soma = soma + K

    return soma
    

#=============================================================
#Bloco de execução do código:

resposta = exercicio_um(13, 0)

print(resposta)


# Resposta: O valor da variável soma será 91.
#=============================================================