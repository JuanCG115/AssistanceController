import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleado = os.listdir(ruta)

for name in lista_empleado:
    imagen_actual = cv2.imread(f'{ruta}/{name}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(name)[0])

print(nombres_empleados)

# Codificar imagenes
def codificar(imagenes):

    # Crear lista nueva
    lista_codificada = []

    # Pasar imagenes RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # Codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregar a la lista
        lista_codificada.append(codificado)

    # Devolver lista codificada
    return lista_codificada

# Registrar ingresos
def registro(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleado_codificada = codificar(mis_imagenes)

# Tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer la imagen de la camara
exito, imagen = captura.read()

if not exito:
    print('No se pudo tomar la cptura')
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # Codificar la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias
    for cara_codif, cara_ubi in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleado_codificada, cara_codif)
        distancias = fr.face_distance(lista_empleado_codificada, cara_codif)
        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print('No coincide con ninguno de los empleados')
        else:
            # Buscar nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = cara_ubi
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            registro(nombre)

            # Mostar la imagen obtenida
            cv2.imshow('Imagen web', imagen)

            # Mantener ventana abierta
            cv2.waitKey(0)
