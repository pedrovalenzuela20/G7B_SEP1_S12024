import numpy as np 
from sympy import symbols, Eq, solve
from sympy import solve
import cmath
import sympy as sp
import math

x= sp.symbols('x')
#---------Párametros obtenidos previamente---------
A = 0.97741975+0.00392699999999999j
B = 9.849465+57.080301875j
C = -1.0280886000000084e-06+0.00077948849055j
D = 0.97741975+0.003926999999999999j
#-------------------Datos--------------------------
Sc= 1200*10**6
fp=0.9
Vs= (500*10**3)/np.sqrt(3)
#---------------Formulación----------------------
Vr=Vs
print("VS=",Vs)
Ir= (Sc)/Vr
angulo_grados = math.acos(fp)
Ir_fasor= cmath.rect(Ir,angulo_grados)
print("Ir_fasor=", Ir_fasor)

angulo_y= 90
x=float(x)
x_fasor= cmath.rect(x,90)

print("x=", x_fasor)
print(B*Ir_fasor)

eq= (((B*(x_fasor)+A)*Vr+B*Ir_fasor),Vs)
print(eq)
print(sp.solve(eq,x))
# Resolver la ecuación
soluciones = sp.solve(eq_2, x)
print(soluciones)