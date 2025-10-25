from datetime import date
tema = "Bradley Cooper | Lukas Nelson - Shallow"
def obtener_colaboradores(tema: str) -> list:
    colaboradores = []
    nombre = ""
    for caracter in tema:
        if caracter == "-":
            break
        else:
            nombre += caracter
    actual = ""
    for caracter in nombre:
        if caracter != "|":
            actual += caracter
        else:
            colaboradores.append(actual)
            actual = ""
    colaboradores.append(actual)
    return colaboradores
#--------------------------------------------------
def obtener_nombre_tema(tema: str) -> str:
    nombre = ""
    guion_encontrado = False
    for letra in tema:
        if guion_encontrado:
            nombre = nombre + letra
        if letra == "-":
            guion_encontrado = True
    return nombre
#--------------------------------------------------
"""Recorro la cadena y la lista, y si sus elementos coinciden, son agregados a la cadena views. 
Convierto la ultima en entero y la multiplico por 1 millon."""
def convertir_vistas_numerico(vistas: str) -> int:
    numeros = ["0","1","2","3","4","5","6","7","8","9"] 
    views = ""
    for v in range(len(vistas)):
        for n in range(len(numeros)): 
            if vistas[v] == numeros[n]:
                views += vistas[v]
                break #no quiero seguir buscando numeros porque ya encontro
    entero = int(views) *1000000
    return entero 
vistas = "1900 millones"
#--------------------------------------------------
"""Voy a recorrer la cadena duracion hasta llegar a ":". 
A lo de la izquierda del ":" lo multiplico por 60 y le sumo lo de la derecha"""
def convertir_duracion_numerico(duracion: str) -> int:
    segundos = ""
    minutos = ""
    separacion = False
    for i in range(len(duracion)):
        if duracion[i] == ":":
            separacion = True #encontro ":"
        elif separacion:
            segundos += duracion[i]
        else:
            minutos += duracion[i]
    total = int(minutos) *60 + int(segundos)
    return total
duracion = "3:37"
#--------------------------------------------------
def obtener_codigo(url: str) -> str:
    codigo = ""
    separacion = False
    for i in range(len(url)):
        if url[i] == "=":
            separacion = True #encontro el "="
        elif separacion: #separacion es True pero ya lo paso
            codigo += url[i] 
    return codigo
url = "https://www.youtube.com/watch?v=bo_efYhYU2A"
#--------------------------------------------------
def formatear_fecha(fecha: str) -> date:
    anio = ""
    mes = ""
    dia = ""
    contador = 0
    for caracter in fecha:
        if caracter == "-":
            contador += 1
        elif contador == 0:
            anio += caracter
        elif contador == 1:
            mes += caracter
        elif contador == 2:
            dia += caracter
    anio = int(anio)
    mes = int(mes)
    dia = int(dia)
    return date(anio, mes, dia)
fecha = "2018-09-27"
#--------------------------------------------------
def analizar(tema,vistas,duracion,url,fecha):
    a = obtener_colaboradores(tema)
    b = obtener_nombre_tema(tema)
    c = convertir_vistas_numerico(vistas)
    d = convertir_duracion_numerico(duracion)
    e = obtener_codigo(url)
    f = formatear_fecha(fecha)
    print("Lista con colaboradores:",a)
    print("Nombre de la cancion:",b)
    print("Vistas totales:",c)
    print("Duración en segundos:",d)
    print("Código único:",e)
    print("Fecha de lanzamiento:",f)
analizar(tema,vistas,duracion,url,fecha)