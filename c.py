# Se va a crear un validador para saber si podemos o no entrar a una fista, es importante agregar que para entrar a la fiesta debes ser mayor de edad

# Se crea la variable edad y ella se va aguardar lo que escriba el usuario
edad = input ("Escriba su edad: ")

#Convertimos la variable de entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)
# Vamos a comparra si la edad es mayor o igual a 18 años
if edad >= 8: 
    #Imprime que lo deja entrar
    print ("Puede entrar")
else:
    #Si no se cumple, imprime "No puede entra"
    print ("No puede entrar")


#Ahora se va a validar si la persona es mayor de edad y ademas tiene más de $600

edad = input("Escriba su edad: ")
edad = int(edad)
dinero = input ("Escriba que cantidad de dinero tiene: ")
dinero = int(dinero)

if edad >= 18: 
    if dinero >= 600:
       print ("Puede entrar")
    else:
    #Si no se cumple, imprime "No puede entra"
       print ("No puede entrar")
else:
    #Si no se cumple, imprime "No puede entra"
    print ("No puede entrar")
    
    
    
if edad >= 8 and dinero >= 600: 
    #Imprime que lo deja entrar
    print ("Puede entrar")
else:
    #Si no se cumple, imprime "No puede entra"
    print ("No puede entrar")
    
    
#Condicional con multiples comparaciones
#Creamos la variable llamada dinero
dinero = input("Escriba el dinero con el que cuenta")
dinero = int(dinero)

if dinero < 100:
    print("Le compro unas galletas")
elif dinero >= 100 and dinero <= 200:
    print("Le compro unos chocolates")
elif dinero >= 200 and dinero <= 300:
    print("Le compro un ramo de rosas")
else:
    print("Le compro un peluche")
    
    
#Creamos la variable userreply y en ella guardamos 
userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
else: # Alineado perfectamente con el 'if'
    print("Please come back when you need to ship a package. Thank you.")
    

#En la variable userReply vamos a guardar una de estas opciones que deben ser escritas en la consola si no se escribe nada escribimos un mensaje de despedida
#Si userReply es exactamente igual a "stamps" imprime el mensaje stamps
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")

#Si userReply es exactamente igual a "envelope" imprime el mensaje envelope
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
    
#Si userReply es exactamente igual a "copy" imprime el mensaje copy
elif userReply == "copy":

# Se crea la variable copies y se almacena el numero de copias que desee crear el usuario
    copies = input("How many copies would you like? (Enter a number) ")
    
    #Imprime el numero de copias
    print("Here are {} copies.".format(copies))
else:
    #Imprime mensaje de despedida
    print("Thank you, please come again.")
    
