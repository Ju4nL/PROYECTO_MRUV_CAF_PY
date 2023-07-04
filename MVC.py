import Clase_mruv as mruv
import os
import emoji



# objeto_Mruv=mruv.MRUV(nombre,float(posicion_final),float(aceleracion),float(velocidad_inicial),float(velocidad_final),float(tiempo))

class Controlador :
    def __init__(self,name,posicion_final=0,acceleration=0,velocidad_inicial=0,velocidad_final=0,tiempo=0):
      
      ruta_principal=str(os.getcwd()).replace('\Archivos_Mru','')
      os.chdir(ruta_principal)
      os.chdir('./Archivos_Mru/')
      archivos=os.listdir()
      n=[archivo.replace('.xlsx','') for archivo in archivos if archivo.endswith('.xlsx')]
      
      if name in n:
          print(f"El nombre :{name} ya existe elija otro nombre")
          return
      else:
        self.velocidad_inicial=velocidad_inicial
        self.tiempo=tiempo
        self.acceleration=acceleration
        self.velocidad_final=velocidad_final
        self.posicion_incial=0
        self.posicion_final=posicion_final
        self.name=name

        self.var_archivo=''

    def calcular_uso(self):
        objeto_Mruv=mruv.MRUV(self.name,float(self.posicion_final),float(self.acceleration),float(self.velocidad_inicial),float(self.velocidad_final),float(self.tiempo))

        if self.velocidad_inicial>0  and self.posicion_final>0 and self.tiempo==0 and self.acceleration==0:

            objeto_Mruv.frm_acceleration()
            objeto_Mruv.frm_tiempo()
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            self.var_archivo=objeto_Mruv.info_archivo()

        elif self.posicion_final==0 and self.velocidad_inicial>0 and self.acceleration!=0 and self.posicion_final==0:

            objeto_Mruv.frm_tiempo()
            objeto_Mruv.frm_posicion()
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            self.var_archivo=objeto_Mruv.info_archivo()
        
        elif self.tiempo!=0 and self.acceleration!=0 and self.velocidad_inicial==0:
            objeto_Mruv.frm_velocidad_final()
            objeto_Mruv.frm_posicion()
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            self.var_archivo=objeto_Mruv.info_archivo()
        
        elif self.acceleration!=0 and self.posicion_final!=0 and self.velocidad_inicial==0 and self.tiempo==0:
            
            objeto_Mruv.frm_velocidad_final()
            objeto_Mruv.frm_tiempo()

            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            self.var_archivo=objeto_Mruv.info_archivo()

        elif self.acceleration!=0 and self.posicion_final!=0 and self.velocidad_inicial>0 and self.tiempo==0:
            
            objeto_Mruv.frm_velocidad_final()
            objeto_Mruv.frm_tiempo()

            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            self.var_archivo=objeto_Mruv.info_archivo()
            
        else:
           print('f')
        
        self.var_tiempo=objeto_Mruv.variable_tiempo()

        self.var_aceleracion=objeto_Mruv.variable_aceleracion()

        self.var_velocidad=objeto_Mruv.variable_velocidad()

        self.var_posicion=objeto_Mruv.variable_posicion()
        

    def frenado(self):

        posicion_final=self.posicion_final
        aceleracion_ini=self.acceleration
        if self.velocidad_inicial==0  and self.posicion_final>0 and self.acceleration!=0 and self.tiempo==0:
            self.posicion_final=self.posicion_final/2
            objeto_Mruv=mruv.MRUV(self.name,float(self.posicion_final),float(self.acceleration),float(self.velocidad_inicial),float(self.velocidad_final),float(self.tiempo))
            
            objeto_Mruv.frm_velocidad_final()
            objeto_Mruv.frm_tiempo()
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()#1
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            objeto_Mruv.info_archivo()  

            objeto_Mruv.actualizar_variables_st()
            objeto_Mruv.frm_acceleration()    
            objeto_Mruv.frm_tiempo() 
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()#2
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            objeto_Mruv.extraer_unir_info_archivo()
            self.var_archivo=objeto_Mruv.info_archivo()  

        elif self.velocidad_inicial==0  and self.posicion_final>0 and self.acceleration==0 and self.tiempo>0:
            self.posicion_final=self.posicion_final/2
            self.tiempo=self.tiempo/2
            objeto_Mruv=mruv.MRUV(self.name,float(self.posicion_final),float(self.acceleration),float(self.velocidad_inicial),float(self.velocidad_final),float(self.tiempo))
            
            objeto_Mruv.frm_acceleration()
            objeto_Mruv.frm_velocidad_final()
           
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()#1
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            objeto_Mruv.info_archivo()  

            objeto_Mruv.actualizar_variables_ct()
            objeto_Mruv.frm_acceleration()     
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()#2
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            objeto_Mruv.extraer_unir_info_archivo()
            self.var_archivo=objeto_Mruv.info_archivo()  

        elif self.velocidad_inicial==0  and self.posicion_final>0 and self.acceleration!=0 and self.tiempo>0:
            self.posicion_final=self.posicion_final/2
            self.tiempo=self.tiempo/2
            objeto_Mruv=mruv.MRUV(self.name,float(self.posicion_final),float(self.acceleration),float(self.velocidad_inicial),float(self.velocidad_final),float(self.tiempo))
            
            objeto_Mruv.frm_velocidad_final()        
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()#1
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            objeto_Mruv.info_archivo()  

            objeto_Mruv.actualizar_variables_ct()
            objeto_Mruv.frm_acceleration()     
            objeto_Mruv.listar_tiempo()
            objeto_Mruv.guardar_datos_aceleracion()
            objeto_Mruv.guardar_datos_velocidad()#2
            objeto_Mruv.guardar_datos_distancia()
            objeto_Mruv.unir_datos()
            objeto_Mruv.extraer_unir_info_archivo()
            self.var_archivo=objeto_Mruv.info_archivo()  

        else:
           print('f')
        
        self.var_tiempo=objeto_Mruv.variable_tiempo()

        self.var_aceleracion=objeto_Mruv.variable_aceleracion()

        self.var_velocidad=objeto_Mruv.variable_velocidad()

        self.var_posicion=objeto_Mruv.variable_posicion()


    def alerta(self):
        if self.var_velocidad>0:
            self.var_alerta='\u26A0\ufe0f'+' Alerta de choque'
        else:
            self.var_alerta='\U0001F44D'
        return self.var_alerta
    

    def variable_aceleracion(self):
        return self.var_aceleracion
    

    def variable_tiempo(self):
        return self.var_tiempo


    def variable_posicion (self):
        return self.var_posicion 


    def variable_velocidad (self):
        return self.var_velocidad 


    def variable_archivo(self):
        return self.var_archivo
