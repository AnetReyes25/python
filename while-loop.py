#librerias van en el principio
import random

#Se crea la variable numero y se le pide al usuario que escriba un numero
numero = input("Escriba el numero 0")
#Conertimos la variable numero de str a entero 
numero = int (numero)
# Se verifica que lo que hay en la variable numero dea menor a 10
while numero < 10: 
# Se incrementa el valor de nuMEro

  numero = numero + 1
  #Si numero es menor que 10 se imprime su valor
  print (numero)
  
 #Vams a escribir tablas de multiplicar de un numero
 
numero = input("Escriba un numero: ")
#Conertimos la variable numero de str a entero 
numero = int (numero)
multiplicador = 0
# Se verifica que lo que hay en la variable numero dea menor a 10
while multiplicador < 10: 
# Se incrementa el valor de nuMEro
  #Multiplicador 
 
  multiplicador = multiplicador + 1
  # Valor de multiplicación 
  multiplicacion = numero * multiplicador
  #Si numero es menor que 10 se imprime su valor
  print (f"{numero} + {multiplicador} + {multiplicacion}")
  
  
  
  
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)


isGuessRight = False


# Mientras la variable isGuessRight sea diferente de verdadero se ejecuta
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    # Mientras el valor de la variable guess sea igual al valor de la variable number 
    if int(guess) == number:
        # Imprime que ganamos
        print("You guessed {}. That is correct! You win!".format(guess))
        #La variable isGuessRight se pasa a veradero para terminar el ciclo while
        isGuessRight = True
    # Si la variable guess no es exactamente igual a la variable IsGuessRight imprime 
    else:
        # Intentalo de nuevo
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))