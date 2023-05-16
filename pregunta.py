"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():
    data=[]

    nombre_columnas=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']

    fila=[0, 0, 0, '']
    datos_organizados=[]


    with open("clusters_report.txt", "r") as file:
        d=file.readlines()
        for i in d:
            data.append(i.strip('\n'))
    data=data[4:]


    for i in data:
        if re.match('^ +[0-9]+ +', i):
            lista = i.split()
            fila[0]=int(lista[0])
            fila[1]=int(lista[1])
            fila[2]= float(lista[2].replace(',','.'))
            fila[3]=' '.join(lista[4:])  
        elif re.match('^ +[a-z]', i):
            lista=i.split()
            string= ' '.join(lista)
            fila[3]+=' ' +string
        else:
            fila[3] = fila[3].replace('.', '')
            datos_organizados.append(fila)
            fila = [0, 0, 0, '']

    datos_organizados=pd.DataFrame(datos_organizados, columns =nombre_columnas )

    #
    # Inserte su código aquí
    #

    return datos_organizados
print(ingest_data())
