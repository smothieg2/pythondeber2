import math

# Leer tres números de punto flotante
A = float(input())
B = float(input())
C = float(input())

# Verificar si es posible formar un triángulo
if A + B > C and A + C > B and B + C > A:
    # Calcular el perímetro del triángulo
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Calcular el área del trapecio
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}")
