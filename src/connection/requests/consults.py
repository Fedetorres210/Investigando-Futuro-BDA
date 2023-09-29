import neo4j
import pandas as pd


#  Creacion de un investigador en la base de datos
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # idInvestigacion: id del investigador
    #parameter:
    # nombre: nombre del investigador
    #parameter:
    #   titulo: Titulo del investigador
    #parameter:
    # institucion: institucion del investigador
    #parameter:
    # correo: correo del investigador
# return sumary resumen de la respuesta de la base de datos de grafos

def crear_investigador(driver,idInvestigacion,nombre,titulo,institucion,correo):
    sumary = driver.execute_query("CREATE (i:Investigador {id:$id,nombreCompleto: $nombre, titulo: $titulo, institucion: $institucion, correo: $correo})", id=idInvestigacion ,nombre=nombre , titulo=titulo , institucion=institucion , correo = correo)
    return sumary




#  modificar un investigador en la base de datos con base en su id
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # idInvestigacion: id del investigador
    #parameter:
    # nombre: nombre del investigador
    #parameter:
    #   titulo: Titulo del investigador
    #parameter:
    # institucion: institucion del investigador
    #parameter:
    # correo: correo del investigador
    # return: result resultado de la respuesta de la base de datos de grafos
    # 

def modificar_investigador(driver,idInvestigador,nombre,titulo,institucion,correo):
    results = driver.execute_query("MATCH (unInvestigador:Investigador {id:$idInvestigador}) SET unInvestigador = {id:$idInvestigador,nombreCompleto: $nombre, titulo: $titulo, institucion: $institucion, correo: $correo} RETURN unInvestigador", idInvestigador=idInvestigador,nombre=nombre, titulo=titulo, institucion=institucion, correo = correo)
    return results

#  Encontrar un investigador en base a su id 
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # id: id del investigador
    # 
    # return: pandas dataframe de los datos del investigador 
    # 

def encontrar_investigador(driver, id):
    result = driver.execute_query("MATCH (i:Investigador {id:$id}) RETURN i.id, i.nombreCompleto, i.correo, i.institucion, i.titulo",id = id, result_transformer_= neo4j.Result.to_df) 
    return result;


#  Encontrar los proyectos relacionados con un investigador
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # idInvestigador: id del investigador
    #
    # return: pandas dataframe de los datos de los proyectos en los que ha participado en investigador 
    # 

def encontrar_investigador_relacionado(driver,idInvestigador):
    result = driver.execute_query("MATCH (i:Investigador {id:$idInvestigador})-[:PARTICIPA_EN]->(p:Proyecto) RETURN p.id, p.titulo,p.area_conocimiento,p.duracion_meses,p.año_inicio",idInvestigador = idInvestigador, result_transformer_= neo4j.Result.to_df) 
    return result;



#  
# encontrar_investigadores:
#   Encontrar todos los investigadores
        # parameter:
        #   driver: Es la configuracion para la conexion con la base de datos
        # return: pandas dataframe de los datos  de todos los investigadores registrados 
#
#

def encontrar_investigadores(driver):
    records = driver.execute_query("MATCH (i:Investigador) return i.id, i.nombreCompleto, i.correo, i.institucion, i.titulo",result_transformer_= neo4j.Result.to_df)
    return records;


#  
# asociar_proyecto_investigador:
#   Asociar un proyecto con un investigador 
        # parameter:
        #   driver: Es la configuracion para la conexion con la base de datos
        #parameter:
        # idInvestigador: id del investigador
        #parameter:
        # idProyecto: id del proyecto
#
#

def asociar_proyecto_investigador(driver,idInvestigador,idProyecto):
    driver.execute_query("MATCH (i:Investigador {id:$idInvestigador}) MATCH(p:Proyecto {id:$idProyecto}) CREATE (i)-[:PARTICIPA_EN]->(p)",idInvestigador=idInvestigador,idProyecto=idProyecto)


#  Encontrar un proyecto en base a su id 
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # id: id del proyecto
    # 
    # return: pandas dataframe de los datos del proyecto
    # 

def encontrar_proyecto(driver, id):
    result = driver.execute_query("MATCH (p:Proyecto {id:$id}) RETURN  p.id, p.titulo,p.area_conocimiento,p.duracion_meses,p.año_inicio",id = id, result_transformer_= neo4j.Result.to_df) 
    return result;



#  Encontrar todos los  proyectos 
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # 
    # 
    # return: pandas dataframe de los datos de todos los proyectos
    # 


def encontrar_proyectos(driver):
    records = driver.execute_query("MATCH (p:Proyecto) return p.id, p.titulo,p.area_conocimiento,p.duracion_meses,p.año_inicio",result_transformer_= neo4j.Result.to_df)
    return records;


#  Creacion de un proyecto en la base de datos 
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # idProyecto: id del proyecto
    #parameter:
    # nombreProyecto: nombre del proyecto
    #parameter:
    #   yearInicio: aNo de inicio
    #parameter:
    # areaConocimiento: Area  de conocimiento del proyecto
    #parameter:
    # duracion: duracion en MESES del proyecto
# return sumary resumen de la respuesta de la base de datos de grafos

def crear_proyecto(driver,idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion):
    sumary = driver.execute_query("CREATE (p:Proyecto {id:$idProyecto,titulo: $nombre, año_inicio: $yearInicio, area_conocimiento: $areaConocimiento, duracion_meses: $duracion})", idProyecto=idProyecto ,nombre=nombreProyecto , yearInicio=yearInicio , areaConocimiento=areaConocimiento , duracion = duracion)
    return sumary

#  modificar un proyecto en la base de datos con base en su id
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # parameter:
    # idProyecto: id del proyecto
    #parameter:
    # nombreProyecto: nombre del proyecto
    #parameter:
    #   yearInicio: aNo de inicio
    #parameter:
    # areaConocimiento: Area  de conocimiento del proyecto
    #parameter:
    # duracion: duracion en MESES del proyecto
    # return: result resultado de la respuesta de la base de datos de grafos
    # 


def modificar_proyecto(driver,idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion):
    results = driver.execute_query("MATCH (p:Proyecto {id:$idProyecto}) SET p = {id:$idProyecto,titulo: $nombre, año_inicio: $yearInicio, area_conocimiento: $areaConocimiento, duracion_meses: $duracion} RETURN p", idProyecto=idProyecto ,nombre=nombreProyecto , yearInicio=yearInicio , areaConocimiento=areaConocimiento , duracion = duracion)
    return results


#  Encontrar los investigadores relacionados con un proyecto
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # id: id del proyecto
    #
    # return: pandas dataframe de los datos de todos  los investigadores en los que ha participado en el proyecto
    # 


def encontrar_proyecto_relacionado(driver,id):
    result = driver.execute_query("MATCH (p:Proyecto{id:$id})<-[:PARTICIPA_EN]-(i:Investigador) RETURN i.id, i.nombreCompleto, i.correo, i.institucion, i.titulo,p.id, p.titulo",id = id, result_transformer_= neo4j.Result.to_df) 
    return result;


###PUBLICACIONES!


#  modificar una publicacion en la base de datos con base en su id
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # parameter:
    # id: id del producto
    #parameter:
    # titulo: titulo del producto
    #parameter:
    #   año_publicacion: año de publicacion
    #parameter:
    # revista: Revista de publicacion

    # return: result resultado de la respuesta de la base de datos de grafos
    # 

def modificar_publicacion(driver,id,titulo,año_publicacion,revista):
    results = driver.execute_query("MATCH (p:Publicacion {id:$id}) SET p = {id:$id,titulo: $titulo, año_publicacion: $año_publicacion, revista: $revista} RETURN p.id,p.titulo,p.año_publicacion,p.revista", id=id ,titulo=titulo , año_publicacion=año_publicacion , revista=revista)
    return results


#  Encontrar una publicacion en base a su id 
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # id: id de la publicacion  
    # 
    # return: pandas dataframe de los datos la publicacion

def encontrar_publicacion(driver, id):
    result = driver.execute_query("MATCH (p:Publicacion {id:$id}) RETURN  p.id,p.titulo,p.año_publicacion,p.revista",id = id, result_transformer_= neo4j.Result.to_df) 
    return result;


#  Encontrar  todas las publicaciones registradas
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # 
    # 
    # return: pandas dataframe de los datos de todas las publicaciones registradas
    # 

def encontrar_publicaciones(driver):
    records = driver.execute_query("MATCH (p:Publicacion) return p.id,p.titulo,p.año_publicacion,p.revista",result_transformer_= neo4j.Result.to_df)
    return records;

#  Crear una publicacion en la base de datos 
    # parameter:
    #   driver: Es la configuracion para la conexion con la base de datos
    # parameter:
    # parameter:
    # id: id del producto
    #parameter:
    # titulo: titulo del producto
    #parameter:
    #   año_publicacion: año de publicacion
    #parameter:
    # revista: Revista de publicacion

    # return: result resultado de la respuesta de la base de datos de grafos
    # 



def crear_publicacion(driver,id,titulo,año_publicacion,revista):
    sumary = driver.execute_query("CREATE (p:Publicacion {id:$id,titulo: $titulo, año_publicacion: $año_publicacion, revista: $revista})", id=id ,titulo=titulo , año_publicacion=año_publicacion , revista=revista)
    return sumary



#  
# asociar_proyecto_publicacion:
#   Asociar una publicacion con un proyecto 
        #   driver: Es la configuracion para la conexion con la base de datos
        #parameter:
        # idProyecto: id del investigador
        #parameter:
        # idPublicacion: id del proyecto
    #return: respuesta de la base de datos 
#
#


def asociar_proyecto_publicacion(driver,idProyecto,idPublicacion):
    return driver.execute_query("MATCH (proyecto:Proyecto {id:$idProyecto}) MATCH(publicacion:Publicacion {id:$idPublicacion}) CREATE (proyecto)-[:GENERA]->(publicacion) RETURN publicacion.id,publicacion.titulo,publicacion.año_publicacion,publicacion.revista,proyecto.id, proyecto.titulo,proyecto.area_conocimiento,proyecto.duracion_meses,proyecto.año_inicio ",idProyecto=idProyecto,idPublicacion=idPublicacion,result_transformer_= neo4j.Result.to_df)




#  
# encontrar_asociaciones_publicacionesn:
#   Encuentra las publicaciones que no tienen ninguna relacion con un proyecto, esto lo hace llamando a la funcion encontrar_publicaciones y consultando a la base de datos
        #   driver: Es la configuracion para la conexion con la base de datos
        #parameter:
        # idProyecto: id del proyecto
        #parameter:
        # idPublicacion: id de la publicacion
    #return: lista de todas las publicaciones sin relacion con proyecto
#
#


def encontrar_asociaciones_publicaciones(driver):
    publicacionesTotales = encontrar_publicaciones(driver)
    publicacionesRelacionadas = driver.execute_query("MATCH (proyecto:Proyecto)-[:GENERA]->(publicacion:Publicacion)  RETURN publicacion.id,publicacion.titulo,publicacion.año_publicacion,publicacion.revista ",result_transformer_= neo4j.Result.to_df)
    publicacionesSinRelacionar = []
    for elem in publicacionesTotales.to_numpy().tolist():
        index = 0
        for item in publicacionesRelacionadas.to_numpy().tolist():
            if elem == item:
                
                index = 1;
        if index == 0:
            publicacionesSinRelacionar.append(elem)
    
    return publicacionesSinRelacionar


#  
# encontrar_asociaciones_publicacionesn:
#   Encuentra los proyectos relacionados a una publicacion
#       parameter:
#           driver: Es la configuracion para la conexion con la base de datos
        #parameter:
        #   id: id de la publicacion
    #return: pandas dataframe de todas los proyectos relacionados con una publicacion
#
#

def definir_proyectos_relacionados_publicaciones(driver,id):
    return  driver.execute_query("MATCH (publicacion:Publicacion{id:$id})<-[:GENERA]-(p:Proyecto)  RETURN p.id, p.titulo,p.area_conocimiento,p.duracion_meses,p.año_inicio ",id=id,result_transformer_= neo4j.Result.to_df)