# Leer el tiempo de comienzo y final del juego
hora_inicio = int(input())
hora_fin = int(input())

# Calcular la duración del juego
if hora_inicio < hora_fin:
    duracion = hora_fin - hora_inicio
else:
    duracion = 24 - (hora_inicio - hora_fin)

# Imprimir el mensaje con la duración del juego
print(f"O JOGO DUROU {duracion} HORA(S)")
