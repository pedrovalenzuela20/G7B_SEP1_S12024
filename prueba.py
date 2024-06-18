import pandapower as pp
import pandapower.plotting.plotly as plotly

#Crear una red vacía
net = pp.create_empty_network()

#Añadir buses
bus1 = pp.create_bus(net, vn_kv=500, name="Barra 1", type="b")
bus2 = pp.create_bus(net, vn_kv=500, name="Barra 2", type="b")

#Caracteristicas
linea_a = {"r_ohm_per_km": 0.02, "x_ohm_per_km": 0.115, "c_nf_per_km": 19.1, "max_i_ka": 1}
pp.create_std_type(net, name="linea_a", data=linea_a, element="line")
pp.available_std_types(net, element="line")

#Añadir líneas
pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=500, std_type="linea_a",  name="Línea 1")

#Añadir carga
pp.create_load(net, bus2, p_mw=1080, q_mvar=523.03, scaling=0.9, name="Carga")
#p.create_load(net, bus2, p_mw=1620, q_mvar=784.547, scaling=0.9, name="Carga+50%")
#pp.create_load(net, bus2, p_mw=540, q_mvar=261.516, scaling=0.9, name="Carga-50%")

#Añadir una fuente externa
pp.create_ext_grid(net, bus1, vm_pu=1.02, name="Grid Connection")

#Ejecutar el flujo de carga
pp.runpp(net)

#Visualizar la red con Plotly
plotly.simple_plotly(net)