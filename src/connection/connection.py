from neo4j import GraphDatabase
from connection.requests.consults import crear_investigador,modificar_investigador, encontrar_investigador, encontrar_investigadores, asociar_proyecto_investigador,encontrar_proyecto,encontrar_proyectos,crear_proyecto
import os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv('URL')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
AUTH = (user, password)



driver =  GraphDatabase.driver(url, auth=AUTH) 

def crearInvestigador(id,nombre,titulo,institucion,correo):

    summary = crear_investigador(driver,id,nombre,titulo,institucion,correo)
    return summary

def modificar_investigador(idInvestigador,nombre,titulo,institucion,correo):
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
    crear_proyecto(idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion)