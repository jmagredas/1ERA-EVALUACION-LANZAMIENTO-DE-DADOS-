from random import randint
"""
Programa de simulación de dados con número de lados variables
"""
min = 1 #Número menor del lado

print("Ingrese el número de lados del dado")
max = input()

max = verificar(max) #Número maximo de lados

menu() 

#Verificación de entrada de datos

def verificar(numero):
    while (numero.isnumeric() == False):
        print("Ingrese un numero valido")
        numero=input()
    while (int(numero)<=0):
        print("Ingrese un número mayor a 0")
        numero = input()
    return numero

def menu():
    #Menú de opciones

    print("Opciones:")
    print("1) Simulación de x lanzamientos")
    print("2) Lanzamiento repetitivo") 
    print("3) Tabla de frecuencia de X lanzamientos")
 
    opcion = input()
 
    opcion = verificar(opcion)   
     
    while (int(opcion) > 3 or int(opcion) <1):
        print("Ingrese un numero que se encuentre en las opciones")
        opcion = input()
        opcion = verificar(opcion) 
    
    metodos(opcion) #Llamada a los distintos métodos

def lazamientoNormal(): #Método de lanzamiento normal de x lanzamientos
    print("Cuantos lanzamientos desea realizar?")
    cantidad = input()
    cantidad = verificar(cantidad)
    for x in range(int(cantidad)):
        print("Tu lanzamiento numero ",x+1," arrojo un: ",randint(int(min),int(max))) #Uso de randint para la generación del número aleatorio entre los parámetros dados

def lazamientoRepetido(): #Método de lanzamiento repetido
    lanzar = True
    while lanzar:
        print("Tu lanzamiento arrojo un: ",randint(int(min),int(max))) #Uso de randint para la generación del número aleatorio entre los parámetros dados
        print("Quieres volver a lanzar(Si(s) o No(n))?")
        lanzar = ("s" or "si") in input().lower()
        

def tablaFrecuencia(): #Método de tablas de frecuencias
    tablaFrecuencias = {}#Diccionario para acumular las cantidades de lanzamientos y sus resultados
    fr=0
    for x in range (int(max)):
        tablaFrecuencias[x+1] = 0
    print("Cuantos lanzamientos desea realizar?")
    cantidad = input()
    cantidad = verificar(cantidad)
    for x in range(int(cantidad)):
        random = randint(int(min),int(max))
        claves = tablaFrecuencias.keys()
        for x in claves:
            if(x==random):
                tablaFrecuencias[x]=tablaFrecuencias[x]+1
    print("Lanzamientos:")            
    for x in range(int(max)):
        print(x+1," : ",tablaFrecuencias[x+1])
    print("Tabla de Frecuencias:")  
    for x in range(int(max)):
        print(x+1," : ","Frecuencia absoluta: ",tablaFrecuencias[x+1]," Frecuencia Relativa:", tablaFrecuencias[x+1]/int(cantidad), "Porcentaje: ", (tablaFrecuencias[x+1]/int(cantidad))*100,"%") #Calculo de las frecuencias
        fr=fr+tablaFrecuencias[x+1]/int(cantidad) #Suma para la frecuencia total
    print("Total Fa: ",cantidad,"Total Fr: ",fr, "Total Porcentaje:",fr*100)

def metodos(opcion): #Método de llamado a los distintos métodos
    eleccion = True
    if int(opcion) == 1:
        lazamientoNormal()
    elif int(opcion) == 2:
        lazamientoRepetido()
    elif int(opcion) == 3:
        tablaFrecuencia()
    print("Desea realizar otro método(Si(s) o No(n))?")
    eleccion = ("s" or "si") in input().lower()
    if(eleccion):
        menu()

