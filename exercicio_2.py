#=============================================================
#Exercício Número 2:

class ExercicioTarget():
    def __init__(self, numero_informado):
        self.numero_informado = numero_informado
        self.sequencia_fibonacci = self.__sequencia_fibonacci()


    #Função interna da classe responsável por calcular a sequencia fibonacci:
    def __sequencia_fibonacci(self) -> list:
        a = 0
        b = 1

        sequencia_fibonacci = [a, b]

        for i in range(self.numero_informado - 1):
            a, b = b, a + b

            sequencia_fibonacci.append(b)

        return sequencia_fibonacci


    #Função que verifica se o número informado está dentro ou não da sequência:
    def esta_na_sequencia(self) -> bool:

        resposta = None

        if self.numero_informado in self.sequencia_fibonacci:
            resposta = True
        else:
            resposta = False

        return resposta


#=============================================================
#Bloco de execução do código:

numero_informado = int(input("Insira o seu número: "))

ex = ExercicioTarget(numero_informado)

nova_resposta = ex.esta_na_sequencia()

if nova_resposta == True:
    print('O número ESTÁ na sequencia de Fibonacci.')
else:
    print('O número NÃO ESTÁ na sequencia de Fibonacci.')

#=============================================================