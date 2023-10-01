
vector = [0] * 35
for i in range(35):
    vector[i] = int(input(f"Ingrese un valor para la posición {i}: "))
max_valor = max(vector)
posicion_max = vector.index(max_valor)

print(f"El valor máximo es {max_valor} y se encuentra en la posición {posicion_max}.")

