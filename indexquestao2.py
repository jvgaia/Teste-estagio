def fibonacci_sequence(n):
    # Inicializando os valores de Fibonacci
    fib = [0, 1]

    # Calculando a sequência de Fibonacci até o n-ésimo termo
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    # Verificando se o número pertence à sequência
    if n in fib:
        return f'O número {n} pertence à sequência de Fibonacci!'
    else:
        return f'O número {n} não pertence à sequência de Fibonacci!'

# Exemplo de uso
numero = 21
print(fibonacci_sequence(numero))
