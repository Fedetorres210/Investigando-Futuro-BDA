import neo4j
import pandas as pd

def crear_investigador(driver,idInvestigacion,nombre,titulo,institucion,correo):
    sumary = driver.execute_query("CREATE (i:Investigador {id:$id,nombreCompleto: $nombre, titulo: $titulo, institucion: $institucion, correo: $correo})", id=idInvestigacion ,nombre=nombre , titulo=titulo , institucion=institucion , correo = correo)
    return sumary



def modificar_investigador(driver,idInvestigador,nombre,titulo,institucion,correo):
    results = driver.execute_query("MATCH (unInvestigador:Investigador {idInvestigador:$idInvestigador}) SET unInvestigador = {nombreCompleto: $nombre, titulo: $titulo, institucion: $institucion, correo: $correo} RETURN unInvestigador", idInvestigador=idInvestigador,nombre=nombre, titulo=titulo, institucion=institucion, correo = correo)
    return results


def encontrar_investigador(driver, nombre):
    result = driver.execute_query("MATCH (i:Investigador {id:$nombre}) RETURN i.id, i.nombreCompleto, i.correo, i.institucion, i.titulo",nombre = nombre, result_transformer_= neo4j.Result.to_df) 
    return result;


def encontrar_investigadores(driver):
    records = driver.execute_query("MATCH (i:Investigador) return i.id, i.nombreCompleto, i.correo, i.institucion, i.titulo",result_transformer_= neo4j.Result.to_df)
    return records;


def asociar_proyecto_investigador(driver,idInvestigador,idProyecto):
    driver.execute_query("MATCH (i:Investigador {id:$idInvestigador}) MATCH(p:Proyecto {id:$idProyecto}) CREATE (i)-[:PARTICIPA_EN]->(p)",idInvestigador=idInvestigador,idProyecto=idProyecto)



def encontrar_proyecto(driver, id):
    result = driver.execute_query("MATCH (p:Proyecto {id:$id}) RETURN  p.id, p.titulo,p.area_conocimiento,p.duracion_meses,p.año_inicio",id = id, result_transformer_= neo4j.Result.to_df) 
    return result;


def encontrar_proyectos(driver):
    records = driver.execute_query("MATCH (p:Proyecto) return p.id, p.titulo,p.area_conocimiento,p.duracion_meses,p.año_inicio",result_transformer_= neo4j.Result.to_df)
    return records;




def crear_proyecto(driver,idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion):
    sumary = driver.execute_query("CREATE (p:Proyecto {id:$idProyecto,titulo: $nombre, año_inicio: $yearInicio, area_conocimiento: $areaConocimiento, duracion_meses: $duracion})", idProyecto=idProyecto ,nombre=nombreProyecto , yearInicio=yearInicio , areaConocimiento=areaConocimiento , duracion = duracion)
    return sumary


