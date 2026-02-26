#Se usa libreria re para trabajar con expresiones regulares
import re

#Abrimos el archivo de texto 
with open ("preproinsulin-seq-clean.txt", "r") as f:
    
    #Leemos  todo el contenido del archivo 
    raw_data = f.read()

#Eliminar el terminar el origin
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags=re.IGNORECASE)

#Eliminar el terminador de registro
clean_data = clean_data.replace("//", "")

#Eliminar cualquier cosa que no sea letra
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

#Convertimos todo a minusculas
clean_data = clean_data.lower()

#Abrir nuevamente el archivo de prepoinsulina
with open ("preproinsulin-seq-clean.txt", "w") as f:
    #Limpiamos el archivo
    f.write(clean_data)
    
#Calculamos la longitud de prepoinsulina    
print("Longitud prepoinsulina = ", len(clean_data))

#Si la secuencia no tien 110 caracteres nos salimos del programa
if len(clean_data) != 110:
    print("Error la secuencia no tiene 110 caracteres")
    exit()
    
#Extraemos los primeros 4 caracteres 
lsinsulin = clean_data[0:24]

#Extraemos del carater 25-54
binsulin = clean_data[24:54]

#Extraemos del caracter 55-89
cinsulin = clean_data[54:89]

#Extraemos del caracter 90-110
ainsulin = clean_data[89:110]

#Creamos los diferentes archivos
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(lsinsulin)

with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(binsulin)

with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(cinsulin)
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(ainsulin)
    
#Verificamos el tamaño de caacteres
print("lsinsulin = ", len(lsinsuline))

print("binsulin = ", len(binsuline))

print("cinsulin = ", len(cinsuline))

print("ainsulin = ", len(ainsuline))

insulin = binsulin + ainsulin

#Total de insulina
print("insulina procesada = ", len(insulin))

#Secuencia de la insulina 
print("secuencia de la insulina = ", insulin)