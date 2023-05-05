#Impresion de la lista de nombres
def imprimir_lista(nombres):
    print("->Nombres: ", end='')
    for nombre in nombres:
        print(f"{nombre}, ", end='')
    print("")
 
#Impresion del diccionario que contiene la clasificacion de los nombres   
def imprimir_nombres(diccionario):
    keys = diccionario.keys()
    for clave in keys :
        print(f"->{clave}: ", end='')
        for nombre in diccionario[clave]:
            print(f"{nombre}, ", end='')
        print("")

#Modificacion de los nombres de los magos. Se devuelve el diccionario con los nombre de los magos modificados
def hacer_grandiosos(diccionario):
    for ind,nombre in enumerate(diccionario["Magos"]):
        diccionario["Magos"][ind] = "El gran " + nombre
    return diccionario

#Separacion de nombres segun categoria y devolucion de estas en una tupla
def agrupar_nombres(nombres):
    magos = []
    cientificos = []
    otros = []
    
    for nombre in nombres:
        if(nombre in ["Harry Houdini", "David Blaine", "Teller"]):
            magos.append(nombre)
        elif(nombre in ["Newton","Hawking", "Einstein"]):
            cientificos.append(nombre)
        else:
            otros.append(nombre)
            
    return (magos, cientificos, otros)

#Main

#Listado de nombres
nombres = ["Harry Houdini", "Newton" , "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

#Agrupacion de nombres en una tupla
nombres_agrupados = agrupar_nombres(nombres)

#Asignacion de agrupaciones a un diccionario
diccionario = {}
diccionario["Magos"]=nombres_agrupados[0]
diccionario["Cientificos"]=nombres_agrupados[1]
diccionario["Otros"]=nombres_agrupados[2]

#Impresion de nombres
print("\nListado de personas\n")
imprimir_lista(nombres)

#Impresion de agrupaciones
print("\nClasificacion de personas\n")
imprimir_nombres(diccionario)

#Modificacion de nombres de magos e impresion de agrupaciones
print("\nClasificacion de personas con modificacion de nombres\n")
diccionario = hacer_grandiosos(diccionario)
imprimir_nombres(diccionario)
