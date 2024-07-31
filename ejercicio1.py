#Realice un programa que lea 4 números y diga cuántos son pares y
#cuantos impares y devuelva la sumatoria de los pares.

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(4)]

#se pide ingresar numeros a la lista números, for i in range 4 porque son 4 numeros en un contador

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 == 1]

#los datos obtenidos de la lista numeros, se almacenan en pares o impares dependiendo el resto al dividirlos por 2

print(f"Números pares: {len(pares)}")
print(f"Números impares: {len(impares)}")

#imprime cantidad de numeros pares e impares

print(f"Sumatoria de los números pares: {sum(pares)}")

#imprime la sumatoria de los numeros pares
