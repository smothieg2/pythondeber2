# Leer la hora de inicio y final del juego
hora_inicio = int(input())
minuto_inicio = int(input())
hora_fin = int(input())
minuto_fin = int(input())

# Calcular la duración del juego en minutos
inicio_en_minutos = hora_inicio * 60 + minuto_inicio
fin_en_minutos = hora_fin * 60 + minuto_fin

duracion_en_minutos = (fin_en_minutos - inicio_en_minutos + 24 * 60) % (24 * 60)

# Calcular la duración en horas y minutos
duracion_horas = duracion_en_minutos // 60
duracion_minutos = duracion_en_minutos % 60

# Imprimir el mensaje con la duración del juego
print(f"O JOGO DUROU {duracion_horas} HORA(S) E {duracion_minutos} MINUTO(S)")
