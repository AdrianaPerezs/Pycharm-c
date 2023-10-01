vector = [0] * 40
for i in range(40):
    vector[i] = float(input("Ingrese un valor: "))

promedio = sum(vector) / 40

valores_mayores_que_promedio = []

num_datos_mayores = 0
for valor in vector:
    if valor > promedio:
        num_datos_mayores += 1
        valores_mayores_que_promedio.append(valor)

print("Promedio: {promedio}")
print("Número de datos mayores que el promedio: {num_datos_mayores}")
print("Valores mayores que el promedio: {valores_mayores_que_promedio}")

