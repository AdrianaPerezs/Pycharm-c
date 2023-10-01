A = [0] * 36
B = [0] * 36
for i in range(36):
    A[i] = int(input(f"Ingrese valor para A[{i}]: "))
    B[i] = int(input(f"Ingrese valor para B[{i}]: "))

C = [A[i] + B[i] for i in range(36)]
print("Vector C (suma de A y B):", C)
