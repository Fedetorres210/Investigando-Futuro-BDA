# Investigando el futuro
![badge](https://img.shields.io/badge/Neo4j-018bff?style=for-the-badge&logo=neo4j&logoColor=white)	
![badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![badge](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)



![image](https://img.freepik.com/vector-gratis/hombre-negocios-lupa_1133-347.jpg?size=626&ext=jpg)


## Tabla de contenidos
---
- [Descripcion](#descripcion)
- [Funciones](#Funciones)
    - [Cargar de datos](#carga-de-datos)
    - [Mantenimiento de investigadores](#mantenimiento-de-investigadores)
    - [Mantenimiento de proyectos](#mantenimiento-de-proyectos)
    - [Mantenimiento de publicaciones](#mantenimiento-de-publicaciones)
    - [Asociar investigador(a)](#asociar-investigadora)
    - [Asociar artículo](#asociar-artículo)
    
    
- [Consultas](#consultas)
    - [Top 5 investigadores(as)](#top-5-investigadoresas)
    - [Top 5 instituciones](#top-5-de-institucionesg)
    - [Top 5 areas de conocimiento](#top-5-de-áreas-de-conocimiento)
    - [Busqueda de colegas](#búsqueda-de-colegas)
    - [Busqueda de publicaciones](#búsqueda-de-publicaciones)
    - [Busqueda por area de conocimiento](#búsqueda-por-área-de-conocimiento)
    - [Busqueda de un proyecto](#búsqueda-de-un-proyecto)


---
  



## Descripcion
Aplicación que permite registrar y  analizar las relaciones
entre los(as) investigadores(as) o científicos(as) de varias instituciones.
Esto con el fin de explorar las relaciones de colaboración que pudieran estarse
dando entre ellos, las temáticas de mayor interés abordadas en los diferentes
proyectos de investigación y las publicaciones generadas a partir de las
diferentes investigaciones. 

## Funciones: 

### Carga de datos: 
----------------------------------------------------------------
Inicialmente la base de datos estará vacía, por lo que
debe existir una opción para cargar los 5 archivos antes descritos. Una
vez cargados la aplicación debe construir el grafo correspondiente para
relacionar los datos. En otras palabras, a partir de la lectura de los 5
archivos, se deben crear los nodos y las correspondientes relaciones
iniciales.
### Mantenimiento de investigadores: 
-----
Son las operaciones permitirán
agregar un(a) investigador(a), así como modificar cualquiera de sus
datos o atributos. En este caso no se eliminarán los datos de la persona.
El resultado de toda operación debe reflejarse inmediatamente en la
base de datos (grafo). Esta función no debe estar disponible si no se ha
cargado previamente los datos en el grafo. Para cada investigador(a) se registra: nombre completo, título académico (ejemplo: licenciado,
doctora, máster, etc), nombre de la institución donde labora, correo
electrónico.
### Mantenimiento de proyectos: 
----------------------------------------------------------------
Son las operaciones permitirán agregar
un nuevo proyecto de investigación, asi como modificar cualquiera de
sus datos o atributos. No se eliminarán los datos del mismo.
El resultado de toda operación debe reflejarse inmediatamente en la
base de datos (grafo). Esta función no debe estar disponible si no se ha
cargado previamente los datos en el grafo.
Para cada proyecto se registra: título del proyecto de investigación, año
de inicio del proyecto, duración en meses, área de conocimiento a la que
pertenece.

### Mantenimiento de publicaciones: 
----------------------------------------------------------------
Son las operaciones permitirán
agregar un nuevo artículo y/o modificar cualquiera de sus datos o
atributos. No se eliminarán los datos de la misma.
El resultado de toda operación debe reflejarse inmediatamente en la
base de datos (grafo). Esta función no debe estar disponible si no se ha
cargado previamente los datos en el grafo. Para cada artículo se
registra: título, año de publicación, revista donde se publicó.

### Asociar investigador(a) : 
----------------------------------------------------------------
Esta función permitirá afiliar o incluir un(a)
investigador(a) con un proyecto de investigación. Tanto la persona como
el proyecto deberán estar previamente registrados.
Se debe mostrar una lista de los(as) investigadores(as) existentes en la
base de datos, de los cuales el usuario elegirá uno(a), luego se mostrará
una lista de los proyectos de investigación ya registrados y el usuario
seleccionará en cuál proyecto o proyectos (podrían ser varios) va a
incluir al investigador. Luego de esto, el/la investigador(a) quedará
asociado a esos proyectos de investigación.

### Asociar artículo : 
----------------------------------------------------------------
Esta función permitirá relacionar un artículo con un
proyecto de investigación. Tanto el artículo como el proyecto deberán
estar previamente incluidos en la base de datos.
Se debe mostrar una lista de las publicaciones existentes en la base de
datos, de las cuales el usuario elegirá una, luego se mostrará una lista 


## Consultas

### Top 5 de áreas de conocimiento. 
---
Se debe mostrar el nombre del
área de conocimiento y la cantidad de proyectos de investigación
para las 5 áreas que cuenten con mayor cantidad de
investigaciones. Se requiere mostrar la información ordenada
descendentemente por cantidad.

### Top 5 de instituciones
---
Se debe mostrar el nombre de la
institución y la cantidad de proyectos de investigación para las 5
instituciones que cuenten con mayor cantidad de investigaciones.
Se requiere mostrar la información ordenada descendentemente
por cantidad.

### Top 5 investigadores(as).
--- 
En este caso se mostrará el nombre
completo, la institución donde labora y la cantidad de proyectos
de investigación, para los(as) 5 investigadores(as) que participen
en la mayor cantidad de investigaciones. Se requiere mostrar la
información ordenada descendentemente por cantidad.

### Búsqueda de un(a) investigador(a): 
----
Se seleccionará el nombre
completo del investigador(a) y se mostrar en pantalla sus datos
básicos, así como toda la información de las investigaciones en las
cuales participa.


### Búsqueda de un proyecto: 
----
Se seleccionará el nombre o título de
un proyecto de investigación y se mostrará en pantalla sus datos
completos, incluyendo también los datos completos de cada
uno(a) de los (as) investigadores(as) que participan en ese
proyecto, así como los datos completos de cada una de las
publicaciones que tenga asociadas el proyecto.

### Búsqueda de publicaciones: 
----
Se debe presentar una lista con los
títulos de las publicaciones registradas, de esa lista el usuario
elegirá una o más publicaciones. Para cada artículo seleccionado
deben mostrarse sus datos básicos y el nombre de la
investigación o proyecto al que está asociado.


### Búsqueda por área de conocimiento: 
----
Se debe presentar una lista
con las áreas de conocimiento registradas, de esa lista el usuario
elegirá una. Para el área seleccionada se deben mostrar:

1. El nombre del área de conocimiento
2. El nombre o título de las investigaciones o proyectos que
pertenezcan a esa área de conocimiento
3. Los títulos de todas las publicaciones asociadas a las
investigaciones de esa área.

### Búsqueda de colegas: 
---
 Se debe presentar una lista con el nombrede cada investigador(a) registrado (a), de dicha lista el usuario seleccionará una persona. Para la persona seleccionada se deben mostrar:
1. Todos sus datos básicos (id, nombre completo, título o grado
académico, nombre de la institución donde labora, correo
electrónico)
2. Los nombres completos de los investigadores(as) con los que
haya trabajado en proyectos de investigación.