import streamlit as st
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
    consultasDisponibles = ["Top 5 de áreas de conocimiento","Top 5 de instituciones","Top 5 investigadores(as)","Búsqueda de un(a) investigador(a)","Búsqueda de un proyecto","Búsqueda de publicaciones","Búsqueda de colegas"]
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
        st.dataframe(data)
    if consulta == consultasDisponibles[4]:
        st.dataframe(data)
    if consulta == consultasDisponibles[5]:
        st.dataframe(data)
    if consulta == consultasDisponibles[6]:
        st.dataframe(data)


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
            nombreInvestigador = st.text_input("Ingrese el nombre del investigador: ")
            apellidoInvestigador = st.text_input("Ingrese el apellido del investigador: ")
            correoInvestigador = st.text_input("Ingrese el correo del investigador: ")
            tituloAcademico = st.selectbox("Seleccione el titulo academico",["Tecnico","Bachiller","Licenciado","Master","Doctor"])
            institucion = st.text_input("Ingrese la institucion del Investigador")
            insertar = st.button("Insertar Investigador")
            if insertar:
                pass
        if mantenimientos == opcionesDisponibles[1]:
            investigadores = []
            investigadorSeleccionado = st.selectbox("Seleccione el Investigador que desea modificar",investigadores)
            nombreInvestigador = st.text_input("Ingrese el nuevo nombre del investigador: ")
            apellidoInvestigador = st.text_input("Ingrese el nuevo apellido del investigador: ")
            correoInvestigador = st.text_input("Ingrese el nuevo correo del investigador: ")
            tituloAcademico = st.selectbox("Seleccione el nuevo titulo academico",["Tecnico","Bachiller","Licenciado","Master","Doctor"])
            institucion = st.text_input("Ingrese la nueva institucion del Investigador")
            insertar = st.button("Modificar Investigador")
            if insertar:
                pass
    ##Seleccione de mantenimientos disponibles para proyectos
    if mantenimiento == mantenimientosDisponibles[1]:
        st.image("https://cdn.shortpixel.ai/spai/w_818+q_+ret_img+to_webp/https://www.eude.es/wp-content/uploads/2020/06/IMAGEN-WEB-DIGITAL-1080x593.jpg")
        opcionesDisponibles = ["Agregar Proyecto","Modificar Proyecto"]
        mantenimientos = st.selectbox("Opciones Disponibles: ",opcionesDisponibles)
        ##Selccion de los mantenimientos de los proyectos
        if mantenimientos == opcionesDisponibles[0]:
            nombreProyecto = st.text_input("Ingrese el nombre del proyecto: ")
            yearInicio = st.selectbox("Ingrese el año de inicio del proyecto ",range(1890,2025))
            areaConocimiento = st.text_input("Ingrese el area de conocimiento del proyecto: ")
            institucion = st.number_input("Ingrese la duracion en meses del proyecto: ",1)
            insertar = st.button("Insertar Proyecto")
            if insertar:
                pass
        
        if mantenimientos == opcionesDisponibles[1]:
            proyectos = []
            proyectoSeleccionado = st.selectbox("Seleccione el Proyecto que desea modificar",proyectos)
            nombreProyecto = st.text_input("Ingrese el nuevo nombre del proyecto: ")
            yearInicio = st.selectbox("Ingrese el año de inicio del proyecto ",range(1890,2025))
            areaConocimiento = st.text_input("Ingrese el nuevo area de conocimiento del proyecto: ")
            institucion = st.number_input("Ingrese la nueva duracion en meses del proyecto: ",1)
            insertar = st.button("Modificar Proyecto")
            if insertar:
                pass
    if mantenimiento == mantenimientosDisponibles[2]:
        st.image("http://pandoranoviembre.com/wp-content/uploads/2017/07/publicaciones.png")
        opcionesDisponibles = ["Agregar Publicacion","Modificar Publicacion"]
        mantenimientos = st.selectbox("Opciones Disponibles: ",opcionesDisponibles)
        ##Selccion de los mantenimientos de las publicaciones
        if mantenimientos == opcionesDisponibles[0]:
            tituloPublicacion = st.text_input("Ingrese el titulo de la publicacion: ")
            fechaPublicacion = st.selectbox("Año Publicacion",range(1890,2025))
            revista = st.text_input("Ingrese la revista en la que se publico: ")
            
            insertar = st.button("Insertar Publicacion")
            if insertar:
                pass
        if mantenimientos == opcionesDisponibles[1]:
            publicaciones = []
            publicacionSeleccionada = st.selectbox("Seleccione la Publicacion que desea modificar",publicaciones)
            tituloPublicacion = st.text_input("Ingrese el nuevo titulo de la publicacion: ")
            fechaPublicacion = st.selectbox("Año Publicacion",range(1890,2025))
            revista = st.text_input("Ingrese la nueva revista en la que se publico: ")
            insertar = st.button("Modificar Publicacion")
            if insertar:
                pass

    



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
        investigadores = []
        investigadorSeleccionado = st.selectbox("Seleccione el Investigador que desea Asociar",investigadores)
        proyectos = []
        proyectoSeleccionado = st.selectbox("Seleccione el Proyecto que desea Asociar",proyectos)
        insertar = st.button("Asociar")
        if insertar:
            pass
    if asociacionesDisponibles == asocacionesD[1]:
        proyectos = []
        proyectoSeleccionado = st.selectbox("Seleccione el Proyecto que desea Asociar",proyectos)
        publicaciones = []
        publicacionSeleccionada = st.selectbox("Seleccione la Publicacion que desea Asociar",publicaciones)
        insertar = st.button("Asociar")
        if insertar:
            pass




    







