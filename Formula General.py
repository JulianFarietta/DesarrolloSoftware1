import math

def titulo():
  print("\t\t\tEncuentra el valor de la funcion cuadratica\n")
def funcionCuadratica(a,b,c):
  y=((b**2)-4*a*c)
  if y<0:
    print("La ecuacion no tiene soluciones reales")
  else:
    r=math.sqrt(y)
    x=((-b+r)/(2*a))
    print(x)
    z=((-b-r)/(2*a))
    print(z)
    
titulo()
a=float(input("Ingrese el valor de A: "))
b=float(input("Ingrese el valor de B: "))
c=float(input("Ingrese el valor de C: "))

funcionCuadratica(a,b,c)


