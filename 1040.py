# Leer cuatro números con 1 dígito después del punto decimal
N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())

# Calcular el promedio con pesos 2, 3, 4 e 1 respectivamente
promedio = (N1 * 2 + N2 * 3 + N3 * 4 + N4) / 10

# Imprimir el mensaje "Media: " seguido por el cálculo obtenido
print(f"Media: {promedio:.1f}")

# Verificar condiciones y tomar acciones apropiadas
if promedio >= 7.0:
    print("Aluno aprovado.")
elif promedio < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Leer la puntuación del examen
    nota_exame = float(input())
    
    # Calcular el nuevo promedio con la puntuación del examen
    promedio_final = (promedio + nota_exame) / 2
    
    # Imprimir la puntuación del examen
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # Imprimir el mensaje "Aluno aprovado." o "Aluno reprovado." según el nuevo promedio
    if promedio_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    # Imprimir el mensaje "Media final: " seguido por el promedio final
    print(f"Media final: {promedio_final:.1f}")
