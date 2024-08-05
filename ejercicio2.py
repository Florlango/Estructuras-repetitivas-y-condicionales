#Leer 10 números y obtener la cantidad de mayores y la cantidad de
#menores a 100, cuál es el número máximo y cuál es el número mínimo.

numeros = [int(input(f"Ingrese 10 números {i+1}: "))for i in range (10)]

numeros_menores_100 = [num for num in numeros if num < 100]

numeros_mayores_100 = [num for num in numeros if num > 100]

sorted (numeros_menores_100)
reversed (numeros_mayores_100)

print (f"La cantidad de números menores a 100 son:{len(numeros_menores_100)}")

print (f"La cantidad de números mayores a 100 son {len(numeros_mayores_100)}")

print (f"El número menor ingresado es {numeros_menores_100[-1]}")

print (f"El número mayor ingresado es {numeros_mayores_100[-1]}")
