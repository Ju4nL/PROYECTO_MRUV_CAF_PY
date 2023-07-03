import matplotlib.pyplot as plt #para graficar informacion
import pandas as pd #para manejo de datos
import os #para rutas 
import threading #para ejecutar por segundo
import math
from itertools import zip_longest #para crear df teniendo listas vacias


class MRUV:
    #constructor
    def __init__(self,name,posicion_final=0,acceleration=0,velocidad_inicial=0,velocidad_final=0,tiempo=0):
      
      ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
      os.chdir(ruta_principal)
      os.chdir('./Archivos_Mru/')

      
      # os.chdir(r'C:/Users/MILAGROS/Desktop/Juan/PROYECTO_MRUV_CAF_PY/Archivos_Mru')

      archivos=os.listdir()
      n=[archivo.replace('.xlsx','') for archivo in archivos if archivo.endswith('.xlsx')]
      
      if name in n:
          print(f"El nombre :{name} ya existe elija otro nombre")
          return#raise NombreExistenteError(f"El nombre {name} ya existe,elija otro nombre")
      else:
        self.velocidad_inicial=velocidad_inicial
        self.tiempo=tiempo
        self.acceleration=acceleration
        self.velocidad_final=velocidad_final
        self.posicion_incial=0
        self.posicion_final=posicion_final
        self.list_tiempo=[]
        self.list_acceleration=[]
        self.list_posicion=[]
        self.list_velocidad=[]
        self.df_datos=pd.DataFrame()
        self.name=name
        self.archivo=name+'.xlsx'

    #creamos las funciones para el objeto c.omo acelerar y desacelerar que afectan a la velocidad
      print(f'nombre:{name},pf:{self.posicion_final},ac:{self.acceleration},vi:{self.velocidad_inicial},vf:{self.velocidad_final},t:{self.tiempo},ejecutando')
    #creamos las funciones para el objeto como acelerar y desacelerar que afectan a la velocidad

    def acelerar(self,acelerar):
      self.acceleration=float(self.acceleration)+float(acelerar) #acelerara el vehiculo


    def agregar_distancia(self,distancia):
      self.posicion_final=distancia #cambiaremos la distancia final


#'''CREANDO FORMULAS DE MRUV PARA PODER CALCULAR LOS DATOS QUE VA CORRIENDO EL VEHICULO'''
    def frm_acceleration(self):
      #Esta funcion va calcular la aceleracion que tendra el vehiculo
      #a = (v - v₀) / t  --Formula que nos indican
      if self.tiempo!=0:
        self.acceleration=((self.velocidad_final-self.velocidad_inicial)/self.tiempo)
      elif self.tiempo==0:
        #si no hay tiempo lo calculamos diferente
        self.acceleration=((self.velocidad_final**2)-(self.velocidad_inicial**2))/(2*(self.posicion_final))# - self.posicion_incial))
      elif self.tiempo!=0 and self.velocidad_final==0 and self.velocidad_inicial==0:
        # aceleración = 2 * distancia / tiempo^2
        self.acceleration=(2*self.posicion_final)/(self.tiempo**2)
      else :
        print('f')
      print(self.acceleration,'acelearcion')
      return self.acceleration


    def frm_velocidad_final(self):
      #Esta funcion calculara la velocidad final
      #v = v₀ + at
      if self.tiempo>0:
        self.velocidad_final=(self.velocidad_inicial+(self.acceleration*self.tiempo))
      elif self.tiempo==0:

        self.velocidad_cuadrado=(self.velocidad_inicial**2) + (2 * self.acceleration * (self.posicion_final - self.posicion_incial))
        self.velocidad_final = self.velocidad_cuadrado**(1/2)   
      return self.velocidad_final
      


    def frm_posicion(self):
      #Esta funcion va calcular posicion
      if self.tiempo!=0:
        #x = x₀ + v₀t + (1/2)at²
        self.posicion=self.posicion_incial+(self.velocidad_inicial*self.tiempo)+((1/2) * (self.acceleration) * (self.tiempo ** 2))
      else :
        self.posicion=((self.velocidad_final**2)-(self.velocidad_inicial**2))/(2*self.acceleration)
      
      self.posicion_final=self.posicion
      return self.posicion
    

    def frm_tiempo(self):
      #va calcular el tiempo recorrido con la velocidad
      #t = (v - v₀) / a
      if self.tiempo==0:
        self.tiempo=(self.velocidad_final-self.velocidad_inicial)/self.acceleration     
      else:
        self.tiempo=self.tiempo


      return self.tiempo



#'''GUARDAMOS LA INFORMACION PARA LUEGO PODER UTILIZARLOS EN DATOS Y OTROS GRAFICOS'''

    #guardamos la info para no perderla
    
    def unir_datos(self):
      # archivo=self.name+'.xlsx'
      # #busco primero si existe el archivo para solo agregar la info
      # df_archivo=pd.read_excel(archivo)
      # print(df_archivo)
      #usamos un dataframe para crear una tabla , como sip_longest evitamos un error que pueda truncarnos el proceso
      self.df_datos = pd.DataFrame(list(zip_longest(self.list_tiempo, self.list_posicion, self.list_acceleration,self.list_velocidad)), columns=['Tiempo', 'distancia', 'acceleration','velocidad'])
      self.df_datos['objeto']=self.name
      self.df_datos['objetodistancia']=''

      return self.df_datos


    def info_archivo(self):      
      ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
      os.chdir(ruta_principal)
      os.chdir('./Archivos_Mru/')
      # os.chdir(r'C:/Users/MILAGROS/Desktop/Juan/PROYECTO_MRUV_CAF_PY/Archivos_Mru')
      #os.chdir(r'D:/JUAN/PROYECTO_CAF_CLON/PROYECTO_MRUV_CAF_PY/Archivos_Mru')
      #buscamos si el archivo existe, para agregar info o crear
      if os.path.exists(self.archivo):
          df_existe=pd.read_excel(self.archivo)
          df=pd.concat([df_existe,self.df_datos],axis=0)
          # Eliminar los duplicados basándose en todas las columnas
          self.df_datos=df.drop_duplicates(subset=["Tiempo"])
          self.df_datos.to_excel(self.archivo,sheet_name="Hoja 1",index=False)
          # print("El archivo existe")
      else:
        self.df_datos.to_excel(self.archivo,sheet_name="Hoja 1",index=False)
      return self.archivo
    
#''''GRAFICAMOS LA INFO QUE TENEMOS ''''
    def extraer_unir_info_archivo(self):
      df=pd.read_excel(self.archivo)
      sec_max=df.iloc[-1]["Tiempo"] 
      self.df_datos['Tiempo']=self.df_datos['Tiempo']+sec_max

      dist_max=df.iloc[-1]["distancia"] 
      self.df_datos['distancia']=self.df_datos['distancia']+dist_max

    def listar_tiempo(self):
      #tiempo calcular para graficar
      tiempo=self.tiempo
      self.list_tiempo=[]
      for i in range(1, int(math.ceil(tiempo)) ):
        self.list_tiempo.append(i)

      self.list_tiempo.append(tiempo)
      print(self.list_tiempo)
      return self.list_tiempo
    

    def guardar_datos_distancia(self):
      
      if self.posicion_final!=0:
        posicion_inicial=float(self.posicion_incial)
        velocidad_inicial=float(self.velocidad_inicial)
        acceleration=float(self.acceleration)

        #tiempo calcular para graficar
        self.list_posicion=[]
        for second in self.list_tiempo:
          calculo=posicion_inicial+(velocidad_inicial*second)+((1/2) * (acceleration) * (second ** 2))
          self.list_posicion.append(calculo)
        
        #v = v₀ + at
        print(self.list_tiempo)
        print(self.list_posicion)
      else:
        self.list_posicion=[]
        
      return self.list_posicion
  

    def guardar_datos_aceleracion(self):

      aceleracion=float(self.acceleration)
      #a = (v - v₀) / t  --Formula que nos indican
      if self.tiempo!=0:
        self.list_acceleration=[]
        for second in self.list_tiempo:
          calculo=aceleracion
          # calculo=(velocidad_final-velocidad_inicial)/second
          self.list_acceleration.append(calculo)
      else:
        self.list_acceleration=[]
      #v = v₀ + at
      return self.list_acceleration


    def guardar_datos_velocidad(self):

      velocidad_inicial=self.velocidad_inicial 
      
      #tiempo calcular para graficar
      self.list_velocidad=[]
      for second in self.list_tiempo:
        print(self.list_acceleration)
        print(math.ceil(second)-1)
        calculo=(velocidad_inicial+((self.list_acceleration[math.ceil(second)-1]*second)))
        self.list_velocidad.append(calculo)
      
      #v = v₀ + at      
      return self.list_velocidad
    

    def actualizar_variables_st(self):
      self.velocidad_inicial=self.velocidad_final
      self.velocidad_final=0
      self.tiempo=0
      self.acceleration=0
    
    def actualizar_variables_ct(self):
      self.velocidad_inicial=self.velocidad_final
      self.velocidad_final=0
      self.acceleration=0

    def variable_tiempo(self):
      return self.tiempo
    
    def variable_aceleracion(self):
      return self.acceleration
    
    def variable_velocidad(self):
      return self.velocidad_final
    
    def variable_posicion(self):
      return self.posicion_final
    
    
