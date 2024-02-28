def pertence_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    if a == numero:
        return f'O número {numero} pertence à sequência de Fibonacci.'
    else:
        return f'O número {numero} não pertence à sequência de Fibonacci.'

numero_informado = int(input("Informe um número: "))
print(pertence_fibonacci(numero_informado))
