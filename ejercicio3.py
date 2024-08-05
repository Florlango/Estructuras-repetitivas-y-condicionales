#Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos 
#mayores de edad y cuántos menores de edad.

edad = [int(input(f"Ingrese edad de las 15 personas: persona {i+1} "))for i in range (15)]

sexo = [str(input(f"Ingrese m o f de las 15 personas según corresponda: persona {i+1} "))for i in range (15)]

edades_menores = [num for num in edad if num < 18]
edades_mayores = [num for num in edad if num >= 18]

sexo_mujer = [num for num in sexo if num == "f"]
sexo_hombre = [num for num in sexo if num == "m"]

print (f"La cantidad de personas menores de edad son: {len (edades_menores)} ")

print (f"La cantidad de personas mayores de edad son: {len(edades_mayores)} ")

print (f"La cantidad de mujeres son: {len (sexo_mujer)} ")
print (f"La cantidad de hombres son: {len (sexo_hombre)} ")
