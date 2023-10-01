vector_original = [0] * 20
for i in range(20):
    vector_original[i] = int(input(f"Ingrese un valor {i}: "))
vector_inverso = vector_original[::-1]
print(f"Vector Inverso:", vector_inverso)
