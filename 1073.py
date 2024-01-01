# Leer un entero N
N = int(input())

# Imprimir el cuadrado de cada valor par desde 1 hasta N
for i in range(2, N + 1, 2):
    print(f"{i}^2 = {i*i}")
