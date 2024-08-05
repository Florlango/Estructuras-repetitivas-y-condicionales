#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
numeros = [float (input(f"Inserte números negativos:{i+1}: ")) for i in range (4)]

numeros_positivos = [abs(numero) for numero in numeros]

print (f"Los números convertidos a positivos, son:", numeros_positivos)
