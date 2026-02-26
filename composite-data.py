#La libreria csv nos permite trabajar con archivos separados por , 
import csv
#La libreria copy nos permite tomar archivos de un archivo y usarlos dentro de un programa
import copy

# Se crea el diccionario myVehicle
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Se crea un ciclo for para imprimir cada una de las clave valor que hay dentro del diccionario
for key, value in myVehicle.items():
    #Se imprime la clave valor
    print("{} : {}".format(key,value))
    
#Se cra la lista myInventoryList
myInventoryList = []

# Se abre el archivo car_fleet.csv y s eguarda dentro de la variable csvFile
with open('car_fleet.csv') as csvFile:
    #Se lee el archivo csvReader donde su delimitador son las comas
    csvReader = csv.reader(csvFile, delimiter=',')  
    #Se crea la variable lineCount y se le asigna el valor de 0
    lineCount = 0  
    #Se lee cada una de las líneas, filas o renglones del archivo cvsReader
    for row in csvReader:
        #Sie el valor de las lines es 0 se imprime el nombre de la columna 
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            #Se incrementa en 1 el valor de lineCount
            lineCount += 1  
        #Si el valor de las lineas no es 0 
        else:  
            #Imprime en cada una de las claves la posicion que fue separada por comas anteriormente 
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            #Se copia el valor de las variables dentro del diccionario myVehiculo
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            
            #Se agrega a la lista un vehiculo
            myInventoryList.append(currentVehicle)
            lineCount += 1  
            #Se imprime las lineas leidas
    print(f'Processed {lineCount} lines.')
    
    #Se crea un for para imprimir cada vehiculo de la lista
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")