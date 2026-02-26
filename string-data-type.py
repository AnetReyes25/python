# Creamos una variable myString y dentro de ella guardamos el texto "This is a string"
myString = "This is a string."

# Imprimimos el valor de la varianle myString
print(myString)

#Imprimimos el tipo de dato de la variable myString
print(type(myString))

#Imprimimos el valor de la variable string, un texto y finalmente el tipo de dato de la variable string
print(myString + " is of the data type " + str(type(myString)))

# Creamos la variable firstString y dentro de ella guardamos el valor de "water""
firstString = "water"
# Creamos la variable secondstring y dentro de ella guardamos el valor de "fall"
secondString = "fall"
# Guardamos el valor concatenado de las variables firstString y secondString
thirdString = firstString + secondString
# Imprimimos el valor de la variable thrirdString
print(thirdString)

#Creamos la variable name y usando la funcion imput vamos a almacenar lo que escriba el usuario por consola 
name = input("What is your name? ")

# Imprimimos el valor de la variable name 
print(name)

# Creamos la vriable color y usando la funcion input vamos a almacenar lo que escriba el usuario por consola 
color = input("What is your favorite color?  ")

# Creamos la vriable color y usando la funcion input vamos a almacenar lo que escriba el usuario por consola 
animal = input("What is your favorite animal?  ")

# Pra imprimir usando format{} vamos a poner un {} por cada variable y el format() va a poner el valor de las variables en el orden que se estan usando
print("{}, you like a {} {}!".format(name,color,animal))