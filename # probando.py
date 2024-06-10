# probando 
import pandapower as pp
import pandapower.plotting as plot 
net = pp.create_empty_network()
b1 = pp.create_bus (net, vn_kv=20.)
b2 = pp.create_bus (net, vn_kv=20.)
pp.create_line(net,from_bus=b1,to_bus=b2,length_km=2.5,std_type="NAVY 4x50 SE")
pp.create_ext_grid(net, bus=bi) 
pp. create_load (net, bus=b2, p_mw=1.) 
pp.runpp (net)
print(net.res_bus.vm_pu)
print(net.res_line.loading_percent)
plot.simple_plot (net)