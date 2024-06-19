import matplotlib.pyplot as plt
import numpy

# Potencia inicial
p_initial = 1200*0.9  # en Mw, 1200 MVA.

# Crear un rango de potencias que represente el cambio de ±50%
p_range = numpy.linspace(p_initial*0.5, p_initial*1.5, num=100)

# Lista para guardar las tensiones
voltages = []

# Para cada potencia en el rango
for p in p_range:
    # Actualizar la carga en la red
    net.load.loc[0, 'p_mw'] = p
    
    # Ejecutar una simulación de flujo de potencia
    pp.runpp(net, tolerance_mva=100, max_iteration=100)
    
    # Guardar la tensión en el bus de la carga
    voltages.append(net.res_bus.vm_pu[b2])

# Graficar la tensión en función de la potencia
plt.figure(figsize=(10, 6))
plt.plot(p_range, voltages, label='Tensión en el bus de la carga')
plt.xlabel('Potencia (Mw)')
plt.ylabel('Tensión (p.u.)')
plt.title('Comportamiento de la tensión para una carga que cambia en el rango ±50 de la potencia')
plt.legend()
plt.grid(True)
plt.show()