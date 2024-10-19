# -*- coding: utf-8 -*-
"""Sistema de Calificaciones (Core).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T4iXpjy43vn8M5mBHdW_rl-j0eU_RWz5

Tarea: Sistema de Calificaciones (Core)
Nombre: Luciano Benjamín Recalde Carballo
"""

def obtener_numero_estudiantes(): #Funcion para ingresar cant de estudiantes
    num_estudiantes = input("¿Cuántos estudiantes deseas ingresar? ")
    errores = 1
    while (errores != 0): # ciclo while para que vuelva a solicitar ingresar datos hasta que estos sean correctos
        errores = 0 # al iniciar no existen errores
        if not str(num_estudiantes).isnumeric():
            errores = 1
            print("Ingrese una cantidad válida")
            num_estudiantes = input("¿Cuántos estudiantes deseas ingresar? ")
    return int(num_estudiantes)

def obtener_nombre_estudiante(): # Funcion para ingresar nombre de estudiante
    nombre = input("Ingresa el nombre del estudiante")
    return nombre

def obtener_numero_asignaturas(): #funcion para obtener cant de asign
    n_asignaturas =  input("Ingresa el número de asignaturas")
    errores = 1
    while (errores != 0): # ciclo while para que vuelva a solicitar ingresar datos hasta que estos sean correctos
        errores = 0 # al iniciar no existen errores
        if not str(n_asignaturas).isnumeric():
            errores = 1
            print("Ingrese una cantidad válida")
            n_asignaturas =  input("Ingresa el número de asignaturas")
    return int(n_asignaturas)

def obtener_calificaciones(num_asignaturas): #funcion para ingresar nombre y calificacion
    calificaciones = []
    for i in range(0, num_asignaturas): #ciclo for para cargar datos de cada asignatura
          errores = 1 #flag para detectar si hay errores en la calificacion ingresada, inicializada en 1 para que ingrese al ciclo while que se encuentra m[as adelante]
          asignatura = input(f"Ingresa el nombre de la asignatura {i + 1}: ")
          calificacion = input(f"Ingresa la calificación obtenida en {asignatura}: ") #carga de datos
          while (errores != 0): # ciclo while para que vuelva a solicitar ingresar datos hasta que estos sean correctos
              errores = 0 # al iniciar no existen errores1
              if not calificacion.isnumeric(): #si la calificacion no es numerica avisa que no es valido y aumenta el flag de errores en 1
                  print("valor ingresado no válido")
                  errores +=1
              else:
                  if (int(calificacion) < 0 or int(calificacion) > 10): #si la calificacion esta fuera de rango imprime un error y aumenta el flag de errores
                      print("Calificacion inválida (fuera de rango)")
                      errores +=1
              if errores > 0: #verifica si existen errores y si es asi solicita volver a ingresar valores
                  calificacion = input(f"Vuelva a ingresar la calificación obtenida en {asignatura}: ")
          calificaciones.append(int(calificacion)) #anhade valores  a la lista
    return calificaciones


def calcular_promedio(calificaciones):
    suma_calificaciones=0
    for i in range(len(calificaciones)): #recorrre calificaciones y luego se va acumulando para dividir por la cantidad de materias
        suma_calificaciones = suma_calificaciones + calificaciones[i]
    promedio = suma_calificaciones / len(calificaciones)
    return promedio

def determinar_estado(promedio): #de acuerdo al promedio establece el estado como aprobado, reprobado
    if (promedio < 6):
        estado = "reprobado"
    else:
        estado = "aprobado"
    return estado

def imprimir_resumen(estudiantes): #imprime los valores del diccionario elemento por elemento para cada estudiante
    for i in estudiantes:
        print("Nombre=",i['nombre'], "Promedio=",i['promedio'], "Estado=", i['estado'])

#aqui se llaman a las funciones para ejecutar el programa
num_estudiantes = obtener_numero_estudiantes()
estudiantes = []

for _ in range(num_estudiantes): #para cada estudiante se solicitan los datos, se genera el promedio y el estado
    nombre = obtener_nombre_estudiante()
    num_asignaturas = obtener_numero_asignaturas()
    calificaciones = obtener_calificaciones(num_asignaturas)
    promedio = calcular_promedio(calificaciones)
    estado = determinar_estado(promedio)
    #se guardan los valores de los estudiantes en el diccionario
    estudiantes.append({
        'nombre': nombre,
        'promedio': promedio,
        'estado': estado
    })

imprimir_resumen(estudiantes)
