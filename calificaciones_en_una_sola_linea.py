calificaciones= input('Ingrese las calificaciones separadas por comas: ')
#print muestra mensaje en pantalla pero input muestra un mensaje pidiendo el ingre de información al usuario.

datos= list(map(int, calificaciones.split(',')))
# entrada.split((',')) separa la cadena en una lista de valores))
# map(int, ...) convierte cada elemento de la lista en un entero.
#list(...) convierte el resultado final en una lista

aprobados=0
reprobados=0

for calificacion in datos:
      if calificacion >= 7:
        aprobados= aprobados + 1
      else:
        reprobados = reprobados + 1
        
print(f'Cantidad de aprobados: {aprobados}')
print(f'Cantidad de reprobados: {reprobados}')