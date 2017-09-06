import numpy as np
import pylab as pl
# crea un vector (arreglo) con los valores del eje X
x = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11, 12 ]
# crea un vector (arreglo) con los valores del eje Y para cada valor en el eje x
y = [7.5, 8.0, 10.0, 7.8, 9.5, 7.3, 10.0, 8.0, 8.3, 8.4, 8.5, 9.0]
# Dar nombre a los ejes
pl.ylabel('Promedio por semestre')
pl.xlabel('Semestres')
# Colocamos los rangos
pl.axis([0,15, 0,12])
# Grafica el vector x contra el vector y
pl.plot(x, y, 'cH')
#Guardar la grafica en formato png
pl.savefig('temp1.png')
#mostrar 
pl.show()
