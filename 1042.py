# Leer tres números enteros
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Ordenar los números en orden ascendente
sorted_numbers = sorted([num1, num2, num3])

# Imprimir los números ordenados en orden ascendente
for num in sorted_numbers:
    print(num)

# Imprimir una línea en blanco
print()

# Imprimir los números en la secuencia en la que fueron leídos
print(f"{num1}\n{num2}\n{num3}")
