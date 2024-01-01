# Leer dos valores enteros X e Y
X = int(input())
Y = int(input())

# Asegurar que X sea el menor valor
if X > Y:
    X, Y = Y, X

# Inicializar la suma de impares
suma_impares = 0

# Calcular la suma de impares entre X e Y
for i in range(X + 1, Y):
    if i % 2 != 0:
        suma_impares += i

# Imprimir la suma de impares
print(suma_impares)
