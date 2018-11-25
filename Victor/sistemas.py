import os
import shutil
from os import walk
from datetime import datetime

from os import listdir
from os.path import isfile, isdir

def _ruta_archivo():
    global ruta 
    ruta = input("Indica la ruta, si no indicas la ruta, la ruta sera la actual: ")
    if(ruta == ""): 
        ruta = os.getcwd() + '/'
        print(ruta)

def _crear_archivo():
    num_arc=int(input('¿Cuántos archivos deseas crear?: '))
    contador = 1
    while contador <= num_arc:
        archivo = input('Ingresa el nombre del archivo: ')
        texto = input('Ingresa el texto')
        f = open (archivo,'w')
        f.write(texto)
        f.close()
        contador=contador + 1
        
    num_dir=int(input("Número de directorios a los que deseas mandar los datos: "))
    contador2 = 1
    while contador2 <= num_dir:
        ruta2 = input("Indica la ruta a la cual deseas copiar los ficheros: ")
        src_files = os.listdir(ruta) 
        for file_name in src_files: 
            full_file_name = os.path.join(ruta, file_name) 
            if (os.path.isfile(full_file_name)):
                shutil.copy(full_file_name,ruta2)
        contador2 = contador2 + 1

def _tamaño_archivo():
    num_archivos = 0
    if(ruta == ""): ruta == os.getcwd() + '/'
    for dirName, subdirList, fileList in os.walk(ruta):
        for fname in fileList:
            num = 0
            tamaño = os.path.getsize(fname)
            if(num > tamaño):
                tamaño = num
            print(tamaño)


def _menu_():
        print('Programa de maneja de archivos y directorios U4: ')
        print()
        print('1-> Crear 5 archivos y copiarlos a 2 Directorios (D1 y D2) ')
        print('2-> Buscar al archivo mas grande de D2 y el mas chico de D1')
        print('3-> Comprobar los archivos de los 2 directorios D1 y D2 (muestra el mas actual de D1 y el mas antiguo de D2)')
        print('4-> Copia el contenido de un achivo A dentro el archivo B conservando el contenido de B (concatenación)')
        print('5-> Cuenta el numero de ocurrencias de las letras "B" o "b" dentro de un archivo del del directorio d1')
        print('6-> Cambia los permisos del Archivo A1 a solamente ejecución')
        print('7-> Cambia al archivo A2 de propietaio')
        print('8-> Cambia al archivo A2 de grupo')
        print('9-> Crea un enlace para vel el contenido del archivo D2 ')
        print('10-> Encriptar y des encriptar archivos d2')
        print('[0] Salir del programa ')



if __name__ == '__main__':
    

    salir = False
    while not salir:
        _menu_()
        
        opcion = input()
        opcion = opcion.upper()

        if opcion == '1':
            _ruta_archivo()
            _crear_archivo()
          
            
        elif opcion == '2':
            _ruta_archivo()
            _tamaño_archivo()
        
        elif opcion == '3':
            _ruta_archivo()
            _tamaño_archivo()
        
        elif opcion == '4':
            _ruta_archivo()
            _copiar_archivo()
        
        elif opcion == '5':
            _ruta_archivo()
            _mostrar_directorio()

        elif opcion == '6':
            _ruta_archivo()
            _mostrar_directorio()

        elif opcion == '7':
            _ruta_archivo()
            _mostrar_directorio()
        
        elif opcion == '8':
            _ruta_archivo()
            _mostrar_directorio()
        
        elif opcion == '9':
            _ruta_archivo()
            _mostrar_directorio()
        
        elif opcion == '10':
            _ruta_archivo()
            _mostrar_directorio()
                
        elif opcion == '0':
            salir = True
               
