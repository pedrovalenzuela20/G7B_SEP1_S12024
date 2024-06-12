
import pandapower as pp
import pandapower.plotting as plot
import matplotlib.pyplot as plt

# Crear la red
net = pp.create_empty_network()

# Crear buses
bus1 = pp.create_bus(net, vn_kv=110, name='Bus 1')
bus2 = pp.create_bus(net, vn_kv=20, name='Bus 2')
bus3 = pp.create_bus(net, vn_kv=0.4, name='Bus 3')

# Crear un transformador entre los buses de alta y media tensión
pp.create_transformer(net, bus1, bus2, std_type="25 MVA 110/20 kV", name='Trafo 1')

# Crear un transformador entre los buses de media y baja tensión
pp.create_transformer(net, bus2, bus3, std_type="0.4 MVA 20/0.4 kV", name='Trafo 2')

# Crear una línea entre los buses de media y baja tensión
pp.create_line_from_parameters(net, bus2, bus3, length_km=0.5, r_ohm_per_km=0.876, x_ohm_per_km=0.115, c_nf_per_km=0, max_i_ka=0.123, name='Line 1')

# Crear una carga en el bus de baja tensión
pp.create_load(net, bus3, p_mw=0.1, q_mvar=0.05, name='Load 1')

# Crear una fuente externa (generador) en el bus de alta tensión
pp.create_ext_grid(net, bus1, vm_pu=1.02, name='Grid Connection')

# Ejecutar el flujo de carga
pp.runpp(net)

# Imprimir los resultados del flujo de carga
print("Resultados del flujo de carga:")
print(net.res_bus)
print(net.res_line)

# Plotear la red
plot.simple_plot(net)

# Mostrar el gráfico
plt.show()
