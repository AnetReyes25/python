# Se crea la lista myMixedTypeList en la cual se guardan diferentes tipos de datos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#El ciclo for se encarga de mirar cada uno de los elemnetos de la lista 
for item in myMixedTypeList:
    # En esta impresión se van a mostrar cada uno de los elementos de la lista, primero su valor y luegoe l tipo de dato
    print("{} is of the data type {}".format(item,type(item)))