import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import MVC as ctr
import os


def leer_variables(boton):   
    ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
    os.chdir(ruta_principal)
    os.chdir('./Archivos_Mru/')
    
    nombre = et_nombre.get() 
    velocidad_inicial = et_Velocidad_Ini.get() if len(et_Velocidad_Ini.get()) != 0 else 0
    velocidad_final = et_Velocidad_fin.get() if len(et_Velocidad_fin.get()) != 0 else 0
    tiempo =et_Tiempo.get() if len(et_Tiempo.get()) != 0 else 0
    posicion_final = et_Posicion_fin.get() if len(et_Posicion_fin.get()) != 0 else 0
    aceleracion = et_Aceleracion.get() if len(et_Aceleracion.get()) != 0 else 0

    controlador=ctr.Controlador(nombre,float(posicion_final),float(aceleracion),float(velocidad_inicial),float(velocidad_final),float(tiempo))
    
    if  boton=="frenar": 
        controlador.frenado()
    else:
        controlador.calcular_uso()
        print('f')

    var_tiempo=controlador.variable_tiempo()
    var_aceleracion=controlador.variable_aceleracion()
    var_velocidad=controlador.variable_velocidad()
    var_posicion=controlador.variable_posicion()
    var_archivo=controlador.variable_archivo()
    var_alerta=controlador.alerta()

    actualizar_combobox()
    completar_tabla(var_archivo)
    actualizar_grafico(var_archivo)
    actualizar_entry(var_tiempo,var_aceleracion,var_velocidad,var_posicion,var_alerta)


def completar_tabla(archivo):
    ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
    os.chdir(ruta_principal)
    os.chdir('./Archivos_Mru/')

    df = pd.read_excel(archivo, 'Hoja 1')
    treeview_data.clear()  # Limpiar la lista existente
    
    # Actualizar los datos en treeview_data
    for _, row in df.iterrows():
        tiempo = row['Tiempo']
        distancia = row['distancia']
        acceleration = row['acceleration']
        velocidad = row['velocidad']
        objeto = row['objeto']
        objetodistancia = row['objetodistancia']
        
        treeview_data.append({
            'Tiempo': str(round(tiempo,2))+' s',
            'distancia': str(round(distancia,2))+' m',
            'acceleration': str(round(acceleration,2))+' m/s²',
            'velocidad': str(round(velocidad,2))+' m/s',
            'objeto': objeto,
            'objetodistancia': objetodistancia
        })
    
    # Insertar los datos en el Treeview
    insertar_datos_treeview()
    

def insertar_datos_treeview():
    # Limpiar los elementos existentes en el Treeview
    treeview.delete(*treeview.get_children())
    
    # Insertar los nuevos datos en el Treeview
    for i, dato in enumerate(treeview_data):
        iid = i + 1  # Identificador único del elemento
        tiempo = dato['Tiempo']
        distancia = dato['distancia']
        acceleration = dato['acceleration']
        velocidad = dato['velocidad']
        objeto = dato['objeto']
        objetodistancia = dato['objetodistancia']
        
        # Insertar el elemento en el Treeview
        treeview.insert(parent="", index="end", iid=iid, text=str(tiempo),
                        values=(distancia, acceleration, velocidad, objeto, objetodistancia))

def actualizar_grafico(archivo):
    ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
    os.chdir(ruta_principal)
    os.chdir('./Archivos_Mru/')

    # Leer los datos actualizados del archivo o de otra fuente
    df = pd.read_excel(archivo, 'Hoja 1')
    tiempo = df['Tiempo'].to_list()
    distancia = df['distancia'].to_list()
    aceleracion = df['acceleration'].to_list()
    velocidad = df['velocidad'].to_list()
    
    # Limpiar el gráfico existente
    axs1.clear()
    
    # Actualizar los datos y propiedades del gráfico
    axs1.plot(tiempo, distancia, linestyle='--', color='g')
    axs1.set_xlabel('Segundos',color='white')#para dar nombre al grafico
    axs1.set_ylabel('Distancia',color='white')#para dar nombre al grafico
    axs1.tick_params(axis='x', colors='white')
    axs1.tick_params(axis='y', colors='white')

    canvas1.draw()
    
    # Limpiar el gráfico existente
    axs2.clear()
    
    # Actualizar los datos y propiedades del gráfico
    axs2.plot(tiempo, aceleracion, linestyle='--', color='g')
    axs2.set_xlabel('Segundos',color='white')#para dar nombre al grafico
    axs2.set_ylabel('Aceleracion',color='white')#para dar nombre al grafico
    axs2.tick_params(axis='x', colors='white')
    axs2.tick_params(axis='y', colors='white')

    canvas2.draw()
    
    # Limpiar el gráfico existente
    axs3.clear()
    
    # Actualizar los datos y propiedades del gráfico
    axs3.plot(tiempo, velocidad, linestyle='--', color='g')
    axs3.set_xlabel('Segundos',color='white')#para dar nombre al grafico
    axs3.set_ylabel('Velocidad',color='white')#para dar nombre al grafico
    axs3.tick_params(axis='x', colors='white')
    axs3.tick_params(axis='y', colors='white')
    
    # Redibujar el gráfico en el lienzo existente
    canvas3.draw()

def actualizar_combobox():
    # Obtener la lista actualizada de archivos en el directorio
    ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
    os.chdir(ruta_principal)
    archivos = os.listdir('./Archivos_Mru')
    combo_list = [archivo.replace('.xlsx','') for archivo in archivos if archivo.endswith('.xlsx')]
    
    # Actualizar los valores del Combobox
    combobox['values'] = combo_list
    combobox.current(0)

def cambiar_combobox_graficos():

    ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
    os.chdir(ruta_principal)
    os.chdir('./Archivos_Mru/')
    archivo = str(combobox.get())+'.xlsx'
    completar_tabla(archivo)
    actualizar_grafico(archivo)


def actualizar_entry(tiempo,aceleracion,velocidad,posicion,alerta):

    et_alert.configure(state="normal")
    et_alert.delete(0, "end")
    et_alert.insert(0, alerta)
    et_alert.configure(state="readonly") 


    et_tiempo_d.configure(state="normal")
    et_tiempo_d.delete(0, "end")
    et_tiempo_d.insert(0, float(tiempo))
    et_tiempo_d.configure(state="readonly") 

    et_acelerar_d.configure(state="normal")
    et_acelerar_d.delete(0, "end")
    et_acelerar_d.insert(0, round(aceleracion,2))
    et_acelerar_d.configure(state="readonly") 

    et_velocidad_d.configure(state="normal")
    et_velocidad_d.delete(0, "end")
    et_velocidad_d.insert(0, round(velocidad,2))
    et_velocidad_d.configure(state="readonly") 

    et_distancia_d.configure(state="normal")
    et_distancia_d.delete(0, "end")
    et_distancia_d.insert(0, round(posicion,2))
    et_distancia_d.configure(state="readonly") 


ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
os.chdir(ruta_principal)

#os.chdir(r'D:/JUAN/PROYECTO_CAF_CLON/PROYECTO_MRUV_CAF_PY') #cambiar

ventana = tk.Tk()
ventana.title("Mruv")
ventana.iconbitmap("./Iconos/icono2.ico")
ventana.geometry('1350x600')
#ventana.configure(bg="#217346")

#responsive
ventana.columnconfigure(index=0, weight=1)
ventana.columnconfigure(index=1, weight=1)
ventana.columnconfigure(index=2, weight=1)
ventana.rowconfigure(index=0, weight=1)
ventana.rowconfigure(index=1, weight=1)
ventana.rowconfigure(index=2, weight=1)

# Creando estilo con plantilla
style = ttk.Style(ventana)

# Importando
ventana.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")



#creando frame1
style = ttk.Style()
style.configure("Custom.TLabelframe", background="#FC4A61")


frame1 = ttk.LabelFrame(ventana, text="Ingresar inputs",  padding=(10, 0))
frame1.grid(row=0, column=0, padx=(20, 4), pady=(20, 10), sticky="nsew")
frame1.grid_columnconfigure(0, weight=1)  # Configurar la columna 0 para que se expanda horizontalmente



# Labels and inputs :)

# Etiquetas
#--Label=lb
#--Entry=et
# Etiquetas

#creando label and input de frame1

lb_nombre = tk.Label(frame1, text="Ingrese un nombre:")
lb_nombre.grid(row=0, column=0, padx=0, pady=0, sticky="w")
et_nombre = ttk.Entry(frame1)
et_nombre.grid(row=1, column=0, padx=0, pady=(0, 10), sticky="ew")


lb_Velocidad_Ini = tk.Label(frame1, text="Ingrese la velocidad inicial:")
lb_Velocidad_Ini.grid(row=2, column=0, padx=0, pady=0, sticky="w")
et_Velocidad_Ini = ttk.Entry(frame1)
et_Velocidad_Ini.grid(row=3, column=0, padx=0, pady=(0, 10), sticky="ew")


lb_Velocidad_fin = tk.Label(frame1, text="Ingrese la velocidad final:")
lb_Velocidad_fin.grid(row=4, column=0, padx=0, pady=0, sticky="w")
et_Velocidad_fin = ttk.Entry(frame1)
et_Velocidad_fin.grid(row=5, column=0, padx=0, pady=(0, 10), sticky="ew")


lb_Tiempo = tk.Label(frame1, text="Ingrese el tiempo:")
lb_Tiempo.grid(row=6, column=0, padx=0, pady=0, sticky="w")
et_Tiempo = ttk.Entry(frame1)
et_Tiempo.grid(row=7, column=0, padx=0, pady=5, sticky="ew")


lb_Posicion_fin = tk.Label(frame1, text="Ingrese la posición final:")
lb_Posicion_fin.grid(row=8, column=0 , padx=0, pady=0, sticky="w")
et_Posicion_fin = ttk.Entry(frame1)
et_Posicion_fin.grid(row=9, column=0, padx=0, pady=5, sticky="ew")


lb_Aceleracion = tk.Label(frame1, text="Ingrese la aceleración:")
lb_Aceleracion.grid(row=10, column=0 , padx=0, pady=0, sticky="w")
et_Aceleracion = ttk.Entry(frame1)
et_Aceleracion.grid(row=11, column=0, padx=0, pady=5, sticky="ew")


# # Botón para imprimir las variables
# Togglebutton
button = ttk.Button(frame1,  text="Crear", command=lambda: leer_variables("crear"), style="Accent.TButton")
button.grid(row=12, column=0, padx=0, pady=10, sticky="ew")

button_fr = ttk.Button(frame1,  text="Aclerar y Frenar", command=lambda: leer_variables("frenar"), style="Accent.TButton")
button_fr.grid(row=13, column=0, padx=0, pady=10, sticky="ew")



#frame2

frame2 = ttk.LabelFrame(ventana, padding=(10,0))
frame2.grid_columnconfigure(0, weight=1)  # Configurar la columna 0 de frame2 para que se expanda horizontalmente
frame2.grid(row=0, column=1, padx=1, pady=(20, 10), sticky="nsew")


# Crear los dos nuevos LabelFrame dentro de frame2
frame_superior = ttk.LabelFrame(frame2, text="Resultados:",padding=5)
frame_superior.grid(row=0, column=0, padx=0, pady=(0,10), sticky="nsew")
frame_superior.grid_columnconfigure(0, weight=1)  # Configurar la columna 0 de frame2 para que se expanda horizontalmente


#mostrar
et_alert = ttk.Entry(frame_superior,width=22)
et_alert.grid(row=0, column=0, padx=3, pady=5,columnspan=2, rowspan=2)
et_alert.configure(state="readonly")


lb_tiempo= tk.Label(frame_superior, text="Tiempo:")
lb_tiempo.grid(row=3, column=0 , padx=(10,5), pady=0, sticky="w")

et_tiempo_d = ttk.Entry(frame_superior,width=10)
et_tiempo_d.grid(row=3, column=1, padx=1, pady=5)
et_tiempo_d.configure(state="readonly") 


lb_acelerar= tk.Label(frame_superior, text="Acelerar:")
lb_acelerar.grid(row=4, column=0 , padx=(10,5), pady=0, sticky="w")

et_acelerar_d = ttk.Entry(frame_superior,width=10)
et_acelerar_d.grid(row=4, column=1, padx=1, pady=5)
et_acelerar_d.configure(state="readonly") 


lb_velocidad= tk.Label(frame_superior, text="Velocidad:")
lb_velocidad.grid(row=5, column=0 , padx=(10,5), pady=0, sticky="w")

et_velocidad_d = ttk.Entry(frame_superior,width=10)
et_velocidad_d.grid(row=5, column=1, padx=1, pady=5)
et_velocidad_d.configure(state="readonly") 


lb_distancia= tk.Label(frame_superior, text="Distancia:")
lb_distancia.grid(row=6, column=0 , padx=(10,5), pady=0, sticky="w")

et_distancia_d = ttk.Entry(frame_superior,width=10)
et_distancia_d.grid(row=6, column=1, padx=1, pady=5)
et_distancia_d.configure(state="readonly") 


frame_inferior = ttk.LabelFrame(frame2, text="Graficar", padding=10)
frame_inferior.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
frame_inferior.grid_columnconfigure(0, weight=1)  # Configurar la columna 0 de frame2 para que se expanda horizontalmente

lb_Aceleracion = tk.Label(frame_inferior, text="Seleccione:")
lb_Aceleracion.grid(row=1, column=0 , padx=1, pady=0, sticky="w")



archivos=os.listdir('./Archivos_Mru')
if len(archivos)==0:
    combo_list=['Cree un grafico']
else:
    combo_list=[archivo.replace('.xlsx','') for archivo in archivos if archivo.endswith('.xlsx')]

# Combobox
combobox = ttk.Combobox(frame_inferior,state="readonly", values=combo_list)
combobox.current(0)
combobox.grid(row=2, column=0, padx=1, pady=5,  sticky="ew")

button = ttk.Button(frame_inferior,  text="Graficar",command=cambiar_combobox_graficos, style="Accent.TButton")
button.grid(row=3, column=0, padx=1, pady=10, sticky="nsew")





#########################
#creando tabla para mostrar

# Panedwindow
paned = ttk.PanedWindow(ventana)
paned.grid(row=0, column=2, padx=(4, 20),pady=(25, 5), sticky="nsew", rowspan=1)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1,2,3,4,5), height=6)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)



# Treeview columns
treeview.column("#0", width=120)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)
treeview.column(3, anchor="w", width=120)
treeview.column(4, anchor="w", width=120)
treeview.column(5, anchor="w", width=120)

# Treeview headings
treeview.heading("#0", text="Tiempo", anchor="center")
treeview.heading(1, text="distancia", anchor="center")
treeview.heading(2, text="acceleration", anchor="center")
treeview.heading(3, text="velocidad", anchor="center")
treeview.heading(4, text="objeto", anchor="center")
treeview.heading(5, text="objetodistancia", anchor="center")


# Datos de los diccionarios
treeview_data = [{'Tiempo': None,
                  'distancia': None,
                  'acceleration': None,
                  'velocidad': None,
                  'objeto': None,
                  'objetodistancia': None}]

# # Define treeview data
# df=pd.read_excel('Carrito2.xlsx','Hoja 1')
# treeview_data=df.to_dict(orient='records')


# Insertar datos en el Treeview
for i, dato in enumerate(treeview_data):
    iid = i + 1  # Identificador único del elemento
    tiempo = dato['Tiempo']
    distancia = dato['distancia']
    acceleration = dato['acceleration']
    velocidad = dato['velocidad']
    objeto = dato['objeto']
    objetodistancia = dato['objetodistancia']
    
    # Insertar el elemento en el Treeview
    treeview.insert(parent="", index="end", iid=iid, text=str(tiempo),
                    values=(distancia, acceleration, velocidad, objeto, objetodistancia))


# Select and scroll
if len(treeview_data)>1:
    treeview.selection_set(1)
    treeview.see(1)

######################################

#creando frame1

# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Notebook
notebook = ttk.Notebook(pane_2)

# Tab #1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)
notebook.add(tab_1, text="Distancia")


fig1,axs1=plt.subplots(1,1,dpi=80,figsize=(10,4) ,sharey=True,facecolor='#313131')
canvas1=FigureCanvasTkAgg(fig1,master=tab_1)
canvas1.draw()
canvas1.get_tk_widget().grid(column=0,row=0,rowspan=3)


# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Aceleracion")

fig2,axs2=plt.subplots(1,1,dpi=80,figsize=(10,4) ,sharey=True,facecolor='#313131')

canvas2=FigureCanvasTkAgg(fig2,master=tab_2)
canvas2.draw()
canvas2.get_tk_widget().grid(column=0,row=0,rowspan=3)



# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Velocidad")

fig3,axs3=plt.subplots(1,1,dpi=80,figsize=(10,4) ,sharey=True,facecolor='#313131')
# fig3.suptitle('graficas',color='white')

canvas3=FigureCanvasTkAgg(fig3,master=tab_3)
canvas3.draw()
canvas3.get_tk_widget().grid(column=0,row=0,rowspan=3)


notebook.pack(expand=True, fill="both", padx=5, pady=5)


ventana.mainloop()


##313131
