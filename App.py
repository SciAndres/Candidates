#Importar librerias necesarias

import sqlalchemy 
import pandas as pd
from sqlalchemy import create_engine 

ruta_archivo = input ("Porfavor ingrese la ruta y el nombre del archivo:")
       
try: 
    archivo =pd.read_csv(f"{ruta_archivo}", sep=';')  
    

except FileNotFoundError:
    print ("El archivo no ha sido encontrado")
 

else:
    print ("Su arvhivo ha sido ingresado") 

nombre_tabla = input ("Ingrese un nombre para la tabla:") 

engine = create_engine('postgresql://postgres:Basesdedatosandres@localhost:5432/votaciones') 
    
archivo.to_sql(f"{nombre_tabla}"  , engine)    

print ("Su tabla ha sido subida a postgresSQL") 






