import pandapower as pp
import pandapower.plotting as plot
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

# Función para mostrar un DataFrame en una ventana emergente
def show_dataframe(df, title):
    root = tk.Tk()
    root.title(title)

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    treeview = ttk.Treeview(frame, columns=list(df.columns), show='headings')
    treeview.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    for col in df.columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=tkFont.Font().measure(col))

    for row in df.itertuples(index=False):
        treeview.insert('', 'end', values=row)

    frame.pack(fill='both', expand=True)
    root.mainloop()

# Crear una red eléctrica vacía
net = pp.create_empty_network()

# Crear buses
bus1 = pp.create_bus(net, name="HV Busbar", vn_kv=110, type="b")
bus2 = pp.create_bus(net, name="HV Busbar 2", vn_kv=110, type="b")
bus3 = pp.create_bus(net, name="HV Transformer Bus", vn_kv=110, type="n")
bus4 = pp.create_bus(net, name="MV Transformer Bus", vn_kv=20, type="n")
bus5 = pp.create_bus(net, name="MV Main Bus", vn_kv=20, type="b")
bus6 = pp.create_bus(net, name="MV Bus 1", vn_kv=20, type="b")
bus7 = pp.create_bus(net, name="MV Bus 2", vn_kv=20, type="b")

# Mostrar la tabla de buses en una ventana emergente
show_dataframe(pd.DataFrame(net.bus), "Buses")

# Crear una conexión a la red externa
pp.create_ext_grid(net, bus=bus1, vm_pu=1.02, va_degree=50) 

# Mostrar la tabla de redes externas en una ventana emergente
show_dataframe(pd.DataFrame(net.ext_grid), "Redes Externas")

# Crear un transformador
trafo1 = pp.create_transformer(net, hv_bus=bus3, lv_bus=bus4, name="110kV/20kV transformer", std_type="25 MVA 110/20 kV")

# Mostrar la tabla de transformadores en una ventana emergente
show_dataframe(pd.DataFrame(net.trafo), "Transformadores")

# Crear líneas
line1 = pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=10, std_type="N2XS(FL)2Y 1x300 RM/35 64/110 kV", name="Line 1")
line2 = pp.create_line(net, from_bus=bus5, to_bus=bus6, length_km=2.0, std_type="NA2XS2Y 1x240 RM/25 12/20 kV", name="Line 2")
line3 = pp.create_line(net, from_bus=bus6, to_bus=bus7, length_km=3.5, std_type="48-AL1/8-ST1A 20.0", name="Line 3")
line4 = pp.create_line(net, from_bus=bus7, to_bus=bus5, length_km=2.5, std_type="NA2XS2Y 1x240 RM/25 12/20 kV", name="Line 4")

# Mostrar la tabla de líneas en una ventana emergente
show_dataframe(pd.DataFrame(net.line), "Líneas")

# Crear un generador
pp.create_gen(net, bus=bus6, p_mw=6, max_q_mvar=3, min_q_mvar=-3, vm_pu=1.03, name="generator") 

# Mostrar la tabla de generadores en una ventana emergente
show_dataframe(pd.DataFrame(net.gen), "Generadores")

# Crear coordenadas genéricas para la visualización
plot.create_generic_coordinates(net)

# Mostrar la figura del esquema eléctrico
plot.simple_plot(net, plot_loads=True, plot_sgens=True, plot_line_switches=True, plot_busbar=True)
plt.show()
