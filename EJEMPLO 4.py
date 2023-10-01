vector_original = [0] * 30
for i in range(30):
    vector_original[i] = int(input(f"Ingrese un valor para {i}: "))
vector_resultante = [x ** 2 for x in vector_original]
print(f"Vector Original:", vector_original)
print(f"Vector Resultante (valores al cuadrado):", vector_resultante)
