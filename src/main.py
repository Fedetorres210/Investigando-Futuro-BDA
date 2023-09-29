import streamlit as st
from connection.connection import encontrarInvestigadores,encontrarInvestigador, crearInvestigador,asociarProyectoInvestigador,encontrarProyectos,encontrarProyecto,crearProyecto,modificarInvestigador,modificarProyecto,encontrarPublicaciones,encontrarPublicacion,crearPublicacion,modificarPublicacion,asociarProyectoPublicacion,encontrarAsociacionesPublicaciones,encontrarAsociacionesPublicaciones,encontrarInvestigadorRelacionado,encontrarProyectoRelacionado,definirProyectosRelacionadosPublicaciones
import pandas as pd
import numpy as np

## Seleccion de pagina en sidebar de streamlit
pagina = st.sidebar.radio("Pagina deseada:", ["Inicio", "Consultas","Carga de datos","Mantenimientos","Asociciones"])


##Seleccion de pagina Inicio
if pagina == "Inicio":
    st.title("Bienvenido a la pagina principal de Investigando el futuro")
    st.write("Aca puedes ver un resumen ejecutivo de las funcionalidades de la pagina, asi como sus creadores.")
    col1, col2,col3 = st.columns(3)

    with col1:
        st.title("Consultas a la base de datos")
        st.subheader("Dentro de esta pagina en la seccion de consultas puedes realizar las siguientes consultas:")
        st.write("1. Top 5 de áreas de conocimiento")
        st.write("2. Top 5 de instituciones.")
        st.write("3. Top 5 investigadores(as).")
        st.write("4. Búsqueda de un(a) investigador(a): ")
        st.write("5. Búsqueda de un proyecto: ")
        st.write("6. Búsqueda de publicaciones:  ")
        st.write("7. Búsqueda de colegas: ")


#Seleccion de pagina de consultas  
if pagina == "Consultas":
    data = []
    ##Consultas disponibles
    consultasDisponibles = ["Top 5 de áreas de conocimiento","Top 5 de instituciones","Top 5 investigadores(as)","Búsqueda de un(a) investigador(a)","Búsqueda de un proyecto","Búsqueda de publicaciones"]
    st.title("Consultas a la base de datos")
    st.image("https://img.freepik.com/vector-premium/equipo-discutiendo-sobre-analisis-datos-servidor-nube_18660-3290.jpg")
    st.subheader("Dentro de esta pagina en la seccion de consultas puedes realizar las siguientes consultas:")
    ##Seleccion de la consulta por realizar 
    consulta = st.selectbox("Consultas a la base de datos",consultasDisponibles)
    ##llamada a la base de datos dependiendo de la consulta seleccionada
    if consulta == consultasDisponibles[0]:
        st.dataframe(data)
    if consulta == consultasDisponibles[1]:
        st.dataframe(data)
    if consulta == consultasDisponibles[2]:
        st.dataframe(data)
    if consulta == consultasDisponibles[3]:
        lista = encontrarInvestigadores().to_numpy().tolist()[1:]
        opcion = st.selectbox("Seleccione el investigador", [elem[0] for elem in lista])
        st.dataframe(encontrarInvestigador(opcion))
        st.subheader("Proyectos relacionados: ")
        st.dataframe(encontrarInvestigadorRelacionado(opcion))
        
        
    if consulta == consultasDisponibles[4]:
        proyectos = encontrarProyectos().to_numpy().tolist()
        opcion = st.selectbox("Seleccione el Proyecto a consultar", [elem[0] for elem in proyectos])
        st.subheader("Informacion del proyecto")
        st.dataframe(encontrarProyecto(opcion))
        st.subheader("Informacion de los investigadores")
        st.dataframe(encontrarProyectoRelacionado(opcion))
    if consulta == consultasDisponibles[5]:
        publicaciones = encontrarPublicaciones().to_numpy().tolist()
        publicacion = st.selectbox("Seleccione la Publicacion a consultar", [elem[0] for elem in publicaciones])
        st.subheader("Informacion de la Publicacion")
        st.dataframe(encontrarPublicacion(publicacion))
        st.subheader("Informacion del proyecto")
        st.dataframe(definirProyectosRelacionadosPublicaciones(publicacion))
        


##Seleccion de la pagina mantenimientos
if pagina == "Mantenimientos":
    st.title("Mantenimientos a la base de datos")
    st.image("https://img.freepik.com/vector-premium/equipo-esperando-proceso-carga-descarga-datos-servidor-nube_18660-3298.jpg?w=2000")
    st.subheader("Dentro de esta pagina en la seccion de Mantenimientos  puedes realizar los siguientes mantenimientos:")
    mantenimientosDisponibles = ["Mantenimiento de investigadores","Mantenimiento de proyectos","Mantenimiento de publicaciones: "]
    mantenimiento = st.selectbox("Mantenimientos a la base de datos",mantenimientosDisponibles)
    ## Seleccion de los mantenimientos disponibles
    if mantenimiento == mantenimientosDisponibles[0]:
        st.image("https://img.freepik.com/vector-gratis/concepto-trabajo-cientificos_23-2148488316.jpg?w=2000")
        opcionesDisponibles = ["Agregar Investigador","Modificar Investigador"]
        mantenimientos = st.selectbox("Opciones Disponibles: ",opcionesDisponibles)
        ##Selccion de los mantenimientos de los investigadores
        if mantenimientos == opcionesDisponibles[0]: 
            idInvestigador =  float(encontrarInvestigadores().to_numpy().tolist()[-1][0]+1)
            nombreInvestigador = st.text_input("Ingrese el nombre del investigador: ")
            correoInvestigador = st.text_input("Ingrese el correo del investigador: ")
            tituloAcademico = st.selectbox("Seleccione el titulo academico",["Tecnico","Bachiller","Licenciado","Master","Doctor"])
            institucion = st.text_input("Ingrese la institucion del Investigador")
            insertar = st.button("Insertar Investigador")
            if insertar:
                sumary = crearInvestigador(idInvestigador,nombreInvestigador,tituloAcademico,institucion,correoInvestigador)
                st.subheader("Insertado con exito!")
                st.dataframe(encontrarInvestigador(idInvestigador))

        if mantenimientos == opcionesDisponibles[1]:
            investigadores = encontrarInvestigadores().to_numpy().tolist()[1:]
            idInvestigador = st.selectbox("Seleccione el investigador que desea modificar", [elem[0] for elem in investigadores])
            st.dataframe(encontrarInvestigador(idInvestigador))
            nombreInvestigador = st.text_input("Ingrese el nuevo nombre del investigador: ")
            correoInvestigador = st.text_input("Ingrese el nuevo correo del investigador: ")
            tituloAcademico = st.selectbox("Seleccione el nuevo titulo academico",["Tecnico","Bachiller","Licenciado","Master","Doctor"])
            institucion = st.text_input("Ingrese la nueva institucion del Investigador")
            insertar = st.button("Modificar Investigador")
            if insertar:
                modificarInvestigador(idInvestigador,nombreInvestigador,tituloAcademico,institucion,correoInvestigador)
                st.subheader("MODIFICADO CON EXITO!")
                st.dataframe(encontrarInvestigador(idInvestigador))




    ##Seleccione de mantenimientos disponibles para proyectos
    if mantenimiento == mantenimientosDisponibles[1]:
        st.image("https://cdn.shortpixel.ai/spai/w_818+q_+ret_img+to_webp/https://www.eude.es/wp-content/uploads/2020/06/IMAGEN-WEB-DIGITAL-1080x593.jpg")
        opcionesDisponibles = ["Agregar Proyecto","Modificar Proyecto"]
        mantenimientos = st.selectbox("Opciones Disponibles: ",opcionesDisponibles)
        ##Selccion de los mantenimientos de los proyectos
        if mantenimientos == opcionesDisponibles[0]:
            idProyecto = encontrarProyectos().to_numpy().tolist()[-1][0] +1
            nombreProyecto = st.text_input("Ingrese el nombre del proyecto: ")
            yearInicio = st.selectbox("Ingrese el año de inicio del proyecto ",range(1890,2025))
            areaConocimiento = st.text_input("Ingrese el area de conocimiento del proyecto: ")
            duracion = st.number_input("Ingrese la duracion en meses del proyecto: ",1)
            insertar = st.button("Insertar Proyecto")
            if insertar:
                crearProyecto(idProyecto,nombreProyecto,yearInicio,areaConocimiento,duracion)
                st.subheader("Insertado con exito!")
                st.dataframe(encontrarProyecto(idProyecto))
        
        if mantenimientos == opcionesDisponibles[1]:
            proyectos =  encontrarProyectos().to_numpy().tolist()
            proyectoSeleccionado = st.selectbox("Seleccione el Proyecto que desea modificar",[elem[0] for elem in proyectos ])
            st.dataframe(encontrarProyecto(proyectoSeleccionado))
            nombreProyecto = st.text_input("Ingrese el nuevo nombre del proyecto: ")
            yearInicio = st.selectbox("Ingrese el año de inicio del proyecto ",range(1890,2025))
            areaConocimiento = st.text_input("Ingrese el nuevo area de conocimiento del proyecto: ")
            duracion = st.number_input("Ingrese la nueva duracion en meses del proyecto: ",1)
            insertar = st.button("Modificar Proyecto")
            if insertar:
                modificarProyecto(proyectoSeleccionado,nombreProyecto,yearInicio,areaConocimiento,duracion)
                st.subheader("MODIFICADO CON EXITO!")
                st.dataframe(encontrarProyecto(proyectoSeleccionado))


    if mantenimiento == mantenimientosDisponibles[2]:
        st.image("http://pandoranoviembre.com/wp-content/uploads/2017/07/publicaciones.png")
        opcionesDisponibles = ["Agregar Publicacion","Modificar Publicacion"]
        mantenimientos = st.selectbox("Opciones Disponibles: ",opcionesDisponibles)
        ##Selccion de los mantenimientos de las publicaciones
        if mantenimientos == opcionesDisponibles[0]:
            idPublicacion = encontrarPublicaciones().to_numpy().tolist()[-1][0] +1
            tituloPublicacion = st.text_input("Ingrese el titulo de la publicacion: ")
            fechaPublicacion = st.selectbox("Año Publicacion",range(1890,2025))
            revista = st.text_input("Ingrese la revista en la que se publico: ")
            
            insertar = st.button("Insertar Publicacion")
            if insertar:
                crearPublicacion(idPublicacion,tituloPublicacion,fechaPublicacion,revista)
                st.subheader("INSERTADO CON EXITO!")
                st.dataframe(encontrarPublicacion(idPublicacion))
        if mantenimientos == opcionesDisponibles[1]:
            publicaciones = encontrarPublicaciones().to_numpy().tolist()
            idPublicacion = st.selectbox("Seleccione la Publicacion que desea modificar", [elem[0] for elem in publicaciones])
            st.dataframe(encontrarPublicacion(idPublicacion))
            tituloPublicacion = st.text_input("Ingrese el nuevo titulo de la publicacion: ")
            fechaPublicacion = st.selectbox("Año Publicacion",range(1890,2025))
            revista = st.text_input("Ingrese la nueva revista en la que se publico: ")
            insertar = st.button("Modificar Publicacion")
            if insertar:
                modificarPublicacion(idPublicacion,tituloPublicacion,fechaPublicacion,revista)
                st.subheader("MODIFICADO CON EXITO!")
                st.dataframe(encontrarPublicacion(idPublicacion))

    



if pagina == "Carga de datos":
    st.title("Bienvenido a la seccion de carga de datos")
    st.image("https://static.vecteezy.com/system/resources/previews/002/846/729/non_2x/cloud-data-upload-vector.jpg")
    investigadores = st.file_uploader("Carga de archivos de Investigadores:")
    proyectos = st.file_uploader('Carga de archivos de Proyectos:')
    publicaciones = st.file_uploader('Carga de archivos de Publicaciones:')

if pagina == "Asociciones":
    st.title("Asociaciones a la base de datos")
    st.image("https://img.freepik.com/vector-premium/analisis-negocios-alta-tecnologia-servidor-nube_18660-2962.jpg")
    st.subheader("Dentro de esta pagina en la seccion de Asociaciones puedes realizar las siguientes asociaciones:")
    asocacionesD = ["Asociacion Proyecto-Investigador", "Asociacion Proyecto-Publicacion"]
    asociacionesDisponibles = st.selectbox("Asociaciones Disponibles",asocacionesD)
    if asociacionesDisponibles == asocacionesD[0]:
        investigadores = encontrarInvestigadores().to_numpy().tolist()[1:]
        investigadorSeleccionado = st.selectbox("Seleccione el Investigador que desea Asociar", [elem[0] for elem in investigadores])
        st.dataframe(encontrarInvestigador(investigadorSeleccionado))

        proyectos = encontrarProyectos().to_numpy().tolist()[1:]
        proyectoSeleccionado = st.selectbox("Seleccione el Proyecto que desea Asociar", [elem[0] for elem in proyectos])
        st.dataframe(encontrarProyecto(proyectoSeleccionado))
        insertar = st.button("Asociar")
        if insertar:
            asociarProyectoInvestigador(investigadorSeleccionado,proyectoSeleccionado)
            st.subheader("Asociacion completada!")
    if asociacionesDisponibles == asocacionesD[1]:
        proyectos =  encontrarProyectos().to_numpy().tolist()
        proyectoSeleccionado = st.selectbox("Seleccione el Proyecto que desea Asociar",[elem[0] for elem in proyectos ])
        st.dataframe(encontrarProyecto(proyectoSeleccionado))

        publicaciones = encontrarAsociacionesPublicaciones()
        idPublicacion = st.selectbox("Seleccione la Publicacion que desea Asociar", [elem[0] for elem in publicaciones])
        st.dataframe(encontrarPublicacion(idPublicacion))
        insertar = st.button("Asociar")
        if insertar:
            result = asociarProyectoPublicacion(proyectoSeleccionado,idPublicacion)
            st.subheader("Asociacion completada!")
            st.dataframe(result)
            publicaciones = encontrarAsociacionesPublicaciones()

            




    







