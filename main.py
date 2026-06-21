print("--- Calculadora de Promedio ---")
numeros = []

for i in range(5):
    num = float(input(f"Ingrese el {i+1} numero: "))
    numeros.append(num)

promedio = sum(numeros) / len(numeros)
print(f"El promedio de los 5 numeros ingresados es: {promedio}")