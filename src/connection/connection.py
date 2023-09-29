from neo4j import GraphDatabase
## Imports de todas las funciones de consults.py
from connection.requests.consults import (crear_investigador,
                                          modificar_investigador, 
                                          encontrar_investigador, 
                                          encontrar_investigadores, 
                                          asociar_proyecto_investigador,
                                          encontrar_proyecto,encontrar_proyectos,
                                          crear_proyecto,
                                          modificar_proyecto,
                                          modificar_publicacion, 
                                          crear_publicacion, 
                                          encontrar_publicacion, 
                                          encontrar_publicaciones,
                                          asociar_proyecto_publicacion,
                                          encontrar_asociaciones_publicaciones,
                                          encontrar_investigador_relacionado,
                                          definir_proyectos_relacionados_publicaciones,
                                          encontrar_proyecto_relacionado,
                                          cargar_investigadores_desde_csv,
                                          cargar_proyectos_desde_csv,
                                          cargar_publicaciones_desde_csv,
                                          crear_relaciones_publicaciones_proyectos,
                                          crear_relaciones_investigadores_proyectos)
## import de variables relativa, relacionadas a un .env 
import os
from dotenv import load_dotenv
import neo4j
##Llamada a las variables relativas 
load_dotenv()
url = os.getenv('URL')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
AUTH = (user, password)


# Configurador de la base de datos

driver =  GraphDatabase.driver(url, auth=AUTH) 




###FUNCIONES DE CONEXION 
## SUS PARAMETROS SON IGUALES A LOS DE LAS FUNCIONES DE CONSULTS
#SIRVEN PARA DIVIDIR LOS FICHEROS Y AUMENTAR LA COMPRESION
#LA VARIABLE driver funciona como global para todas estas funciones
# RETURNS: SON IGUALES A LOS DE LAS FUNCIONES DE CONSULTS O NULOS EN CASO DE NO SER NECESARIOS PARA EL CLIENTE
def crearInvestigador(id,nombre,titulo,institucion,correo):

    summary = crear_investigador(driver,id,nombre,titulo,institucion,correo)
    return summary

def modificarInvestigador(idInvestigador,nombre,titulo,institucion,correo):
    results = modificar_investigador(driver,idInvestigador,nombre,titulo,institucion,correo)
    return results


def encontrarInvestigador(idInvestigador):
    result = encontrar_investigador(driver, idInvestigador)
    return result;


def encontrarInvestigadores():
    results = encontrar_investigadores(driver);
    return results;


def asociarProyectoInvestigador(idinvestigador,idProyecto):
    asociar_proyecto_investigador(driver,idinvestigador,idProyecto)


def encontrarProyecto(id):
    return encontrar_proyecto(driver, id)

def encontrarProyectos():
    return encontrar_proyectos(driver)

def crearProyecto(idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion):
    crear_proyecto(driver,idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion)


def modificarProyecto(idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion):
    modificar_proyecto(driver,idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion)


##PUBLICACIONES

def modificarPublicacion(id,titulo,año_publicacion,revista):
    modificar_publicacion(driver,id,titulo,año_publicacion,revista)


def encontrarPublicacion(id):
    return encontrar_publicacion(driver, id)

def encontrarPublicaciones():
    return encontrar_publicaciones(driver)


def crearPublicacion(id,titulo,año_publicacion,revista):
    crear_publicacion(driver,id,titulo,año_publicacion,revista)


def asociarProyectoPublicacion(idProyecto,idPublicacion):
    return asociar_proyecto_publicacion(driver,idProyecto,idPublicacion)
    

def encontrarAsociacionesPublicaciones():
    return encontrar_asociaciones_publicaciones(driver)



def encontrarInvestigadorRelacionado(idInvestigador):
    return encontrar_investigador_relacionado(driver,idInvestigador)



def encontrarProyectoRelacionado(id):
    return encontrar_proyecto_relacionado(driver,id)


def definirProyectosRelacionadosPublicaciones(id):
    return definir_proyectos_relacionados_publicaciones(driver,id)


def cargarArchivoInvestigadorCSV(csv_file_path):
    cargar_investigadores_desde_csv(driver, csv_file_path);

def cargarArchivoProyectosCSV(csv_file_path):
    cargar_proyectos_desde_csv(driver, csv_file_path);

def cargarArchivoPublicacionesCSV(csv_file_path):
    cargar_publicaciones_desde_csv(driver, csv_file_path);

def cargarArchivoRelacionesPublicacionYProyectoCSV(csv_file_path):
    crear_relaciones_publicaciones_proyectos(driver, csv_file_path);

def cargarArchivoRelacionesInvestigadorYProyectoCSV(csv_file_path):
    crear_relaciones_investigadores_proyectos(driver, csv_file_path);
