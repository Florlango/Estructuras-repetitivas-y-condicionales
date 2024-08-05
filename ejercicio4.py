#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

numeros = [float(input (f"Ingrese 10 números Reales: número {i+1}:"))for i in range (10)]

numeros_positivos = [num for num in numeros if num > 0]

numeros_negativos = [num for num in numeros if num < 0]

print (f"Los números positivos son:", numeros_positivos)


print (f"La suma de los números positivos es igual a : {sum(numeros_positivos)}")
