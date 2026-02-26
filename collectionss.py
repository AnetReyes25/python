# Pra crear una lista se usan corchetes
#Creamos la lista myFruitList y dentro de ella guardamos las siguientes frutas "apple", "banana", "cherry"
myFruitList = ["apple", "banana", "cherry"]

#Imprimimos la lista de frutas completa
print(myFruitList)

#Imprimimos el tipo de dato que es myFruitList
print(type(myFruitList))

#Imprimimos el valor que esta en la primera pocision de la lista myFruitList (este valor es "apple")
print(myFruitList[0])

#Imprimimos el valor que esta en la segunda pocision de la lista myFruitList (este valor es "banana")
print(myFruitList[1])

#Imprimimos el valor que esta en la tercera pocision de la lista myFruitList (este valor es "cherry")
print(myFruitList[2])

#Vamos a cambiar el valor de la lista en su posición dos que antes era "cherry" y ahora va a ser "orange"
myFruitList[2] = "orange"

#Imprimir la lista completa con el cambio
print(myFruitList)


# Para crear una dupla se usan parentesis myFruitList y dentro de ella guardamos las siguientes frutas "apple", "banana", "cherry"
myFinalAnswerTuple = ("apple", "banana", "pineapple")

#Imprimimos el contenido de la tupla
print(myFinalAnswerTuple)

#Imprimimos el tipo de dato de la tupla
print(type(myFinalAnswerTuple))

#Imprimimos el primer valor de la tupla (que es "apple")
print(myFinalAnswerTuple[0])

#Imprimimos el primer valor de la tupla (que es "banana")
print(myFinalAnswerTuple[1])

#Imprimimos el primer valor de la tupla (que es "pinapple")
print(myFinalAnswerTuple[2])

#Para crear un diccionario se utilizan llaves y dentro de ellas se va a crear una clave y un valor. La clave y el valor van separados por dos puntos y luego de cada clave valor se separa del siguiente usando una coma 
#Creamos el diccionario myFavoriteFruitDictionary con las siguientes claves "Akua","Saanvi","Paulo" con los siguientes valores  "apple", "banana", "pineapple"

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

#Imprimimos el diccionario completo
print(myFavoriteFruitDictionary)

#Imprimimos el tipo de dato de myFavoriteFruitDictionary
print(type(myFavoriteFruitDictionary))


# Imprimimos el valor de la clave "Akua"
print(myFavoriteFruitDictionary["Akua"])

# Imprimimos el valor de la clave "Saanvi"
print(myFavoriteFruitDictionary["Saanvi"])

# Imprimimos el valor de la clave "Paulo"
print(myFavoriteFruitDictionary["Paulo"])