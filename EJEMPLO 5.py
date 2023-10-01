vector = [0] * 25
for i in range(25):
    vector[i] = int(input(f"Ingrese un valor para {i}: "))
números_ceros = 0
números_negativos = 0
números_positivos = 0
suma_delos_negativos = 0
suma_delos_positivos = 0
for valor in vector:
    if valor == 0:
        números_ceros += 1
    elif valor < 0:
        números_negativos += 1
        suma_delos_negativos += valor
    else:
        números_positivos += 1
        suma_delos_positivos += valor

print(f"Números ceros: {números_ceros}")
print(f"Números negativos: {números_negativos} (Suma: {suma_delos_negativos})")
print(f"Números positivos: {números_positivos} (Suma: {suma_delos_positivos})")
