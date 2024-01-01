# Leer dos valores enteros
A = int(input())
B = int(input())

# Verificar si son múltiplos
if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
