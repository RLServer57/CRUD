import os
from CRUD import *

crud = CRUD()

def clear():
    ptf = os.name
    if ptf == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def run_app():
    preguntar = True
    print('Peliculas')
    print('1.- Nueva pelicula')
    print('2.- Editar pelicula')
    print('3.- Listar peliculas')
    print('4.- Eliminar pelicula')
    while preguntar:
        opcion=input('Ingrese una opción(ENTER para salir): ')
        if opcion.isnumeric():
            if int(opcion) == 1:
                clear()
                nueva_pelicula()
                preguntar = False
            elif int(opcion) == 2:
                clear()
                editar_pelicula()
                preguntar = False
            elif int(opcion) == 3:
                clear()
                consultar_peliculas()
                preguntar = False
            elif int(opcion) == 4:
                clear()
                eliminar_pelicula()
                preguntar = False
            else:
                clear()
                print('Opción no válida')
                run_app()
        elif opcion != "":
            clear()
            print('Opción no válida')
            run_app()
        else:
            break

def nueva_pelicula():
    print('Peliculas')
    titulo = input('Ingrese nombre de pelicula: ')
    anio = int(input('Ingrese el año: '))
    crud.crear(titulo,anio)
    run_app()

def editar_pelicula():
    print('Editar pelicula')
    titulo=input('Ingrese el titulo: ')
    id = int(input('Ingrese el id: '))
    crud.actualizar(titulo,id)
    run_app()

def consultar_peliculas():
    print('Lista de peliculas')
    crud.leer()
    run_app()

def eliminar_pelicula():
    id = int(input('Ingrese el id para eliminar: '))
    crud.eliminar(id)
    run_app()

clear()
run_app()