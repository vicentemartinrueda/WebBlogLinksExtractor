# Extraer links logueando en una web

##Objetivo
Extraer links de una página que sólo muestra esos links si estás logueado.

##Tecnologías utilizadas
La tecnología utlizada es Python 3.6.3 y las librerías utlizadas son:
- xlwt
- xlrd
- datetime
- urllib
- lxml
- -requests
- sys
- selenium

##Funcionamiento
1. El ++primer script++ **se loguea y extrae las direcciones de todos los posts** de la página referidos a juegos.
2. El ++segundo script++ **se loguea** (de la misma forma) **y extrae todas las urls destino de los enlaces de descarga** para su posterior tratado, separando éstas por una secuencia predefinida (en este caso ', ') **y finaliza escribiendo en un txt línea por línea 'link_post----titulo_post----links_descarga'** (donde está "----" en mi código son cinco guiones normales pero no modifica el comportamiento de los scripts).
3. El ++tercer script++ se encarga de **pasar esos tres datos por línea a un archivo en formato Excel**.
4. Y el ++cuarto script++ **divide todos los enlaces de descarga en columnas** dependiendo del servidor que *hostea* los archivos.

##Modo de uso
1. **Ejecutar el script posts2txt.py**
Esto crearía un txt (llamado posts.txt) con todos los enlaces a los distintos juegos de la página en cuestión.
```python posts2txt.py```

2. **Ejecutar el script links2txt.py**
Esto crearía un txt (llamado final.txt) con todos los enlaces a los posts, sus títulos y sus links de descarga.
```python links2txt.py```

3. **Ejecutar el script txt2Excel.py**
Esto crearía un archivo Excel (llamado sinOrdenar.xls) con 3 columnas y tantas filas como juegos haya. Cada columna corresponderá a uno de los tres datos (link del post, título o links de descarga)
```python txt2Excel.py```

4. **Ejecutar el script ordenarEnlaces.py**
Esto crearía otro archivo Excel con los valores del anterior pero con lis links de descarga ordenados en columnas.
```python ordenarEnlaces.py```