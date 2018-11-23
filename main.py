import lorem
import subprocess
import os
from switch import switch, case

def mkdir(dirname):
    """Función para crear un directorio nuevo y vacio"""
    subprocess.call(["mkdir", dirname])

def touch(filename):
    """Función para crear un archivo"""
    subprocess.call(["touch", filename])
    os.system('echo ' + lorem.paragraph() + ' > ' + filename)

def menu():
    op = 0
    while(op != 13):
        menu = """
        -- MENU --
        1. Crear directorio(s)
        2. Crear archivo(s)
        4. Copiar archivos a carpeta
        3. Buscar archivo más chico y mas grande 
        4. Comparar fechas de 2 directorios
        5. Concatena 2 archivos
        6. Contar ocurrencias
        7. Cambiar permisos a un archivo
        8. Cambiar propietario de un archivo
        9. Cambiar grupo de un archivo
        10. Crear acceso directo de un archivo
        11. Encriptar una archivos/carpeta
        12. Desencriptar archivos/carpeta
        13. Salir
        """
        print(menu)
        try:
            op = int(input("Ingrese una opcion o (CTRL + C para salir): "))
            option(op)
        except ValueError:
            print("Solo se permiten números")
            pass

def option(op):
    while switch(op):
        if case(1):
            mkdir(input("Nombre del directorio: "))
            break
        if case(2):
            touch(input("Nombre del archivo: "))
            break
        if case(3):
            # TODO: Method of option 3
            # your code goes here.
            break
        if case(4):
            # TODO: Method of option 4
            # your code goes here.
            break
        if case(5):
            # TODO: Method of option 5
            # your code goes here.
            break
        if case(6):
            # TODO: Method of option 6
            # your code goes here.
            break
        if case(7):
            # TODO: Method of option 7
            # your code goes here.
            break
        if case(8):
            # TOO: Method of option 8
            # your code goes here.
            break
        if case(9):
            # TODO: Method of option 9
            # your code goes here.
            break
        if case(10):
            # TODO: Method of option 10
            # your code goes here.
            break
        if case(11):
            # TODO: Method of option 11
            # your code goes here.
            break
        if case(12):
            # TODO: Method of option 12
            # your code goes here.
            break
        print("Adios!!")
        break


if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        pass
