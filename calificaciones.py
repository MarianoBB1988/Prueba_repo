import pandas as pd

cals=pd.read_csv('calificaciones.csv')

aprobados=0
reprobados=0

for index, row in cals.iterrows():
    nombre = row['Nombre']
    calificacion = int(row['Calificacion'])
    if calificacion >= 7:
        aprobados= aprobados + 1
    else:
        reprobados = reprobados + 1
    
print(f'Cantidad de aprobados: {aprobados}')
print(f'Cantidad de reprobados: {reprobados}')