#=============================================================
#Exercício Número 5:

def inverter_caractere(palavra) -> list:

    palavra = list(palavra)
    palavra_ao_contrario = []

    for i in range(1, len(palavra) + 1):
        
        palavra_ao_contrario.append(palavra[-i])

    return str(palavra_ao_contrario)
    


#=============================================================
#Bloco de execução do código:

print(inverter_caractere("Exercicio"))

#=============================================================