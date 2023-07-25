import json
import webbrowser
import os
import pyautogui
import time
import datetime
import sys

pyautogui.FAILSAFE=False

busca_pagina = {
    "pagina": os.path.join("imgs","pagina.png"),
}

input_inicio = {
    "detectar_input": os.path.join("imgs","detectar_input.png"),
}

logeo1 = { # Validación si está saliendo
    "logeo": os.path.join("imgs","logeo.png"),
}

aceptar1 = { # Validación si está logeando
    "aceptar": os.path.join("imgs","aceptar.png"),
}

ver_mas = { # Validación si está logeando
    "ver_mas": os.path.join("imgs","ver_mas.png"),
}

pagina_formulario = { # Validación si está en página formulario
    "pagina_formulario": os.path.join("imgs","pagina_formulario.png"),
}

interno = { # Validación de un campo del formulario
    "interno": os.path.join("imgs","interno.png"),
}

producto = { # Validación de un campo del formulario
    "producto": os.path.join("imgs","producto.png"),
}

centro_costo = { # Validación de un campo del formulario
    "centro_costo": os.path.join("imgs","centro_costo.png"),
}

actividad = { # Validación de un campo del formulario
    "actividad": os.path.join("imgs","actividad.png"),
}

servicio_prestado = { # Validación de un campo del formulario
    "servicio_prestado": os.path.join("imgs","servicio_prestado.png"),
}

fecha_servicio = { # Validación de un campo del formulario
    "fecha_servicio": os.path.join("imgs","fecha_servicio.png"),
}

minutos = { # Validación de un campo del formulario
    "minutos": os.path.join("imgs","minutos.png"),
}

descripcion = { # Validación de un campo del formulario
    "descripcion": os.path.join("imgs","descripcion.png"),
}

lupa = { # Validación de lupa
    "lupa": os.path.join("imgs","lupa.png"),
}

facturable = { # Validación dd facturable
    "facturable": os.path.join("imgs","facturable.png"),
}

no_facturable = { # Validación dd no facturable
    "no_facturable": os.path.join("imgs","no_facturable.png"),
}

webbrowser.open(f'http://181.129.9.162:2523/SCTWEB/Paginas/LogIN.aspx')

# Cargar el archivo JSON
with open('config.json') as f:
    full_data = json.load(f)

def busca_pagina_fun():
    pyautogui.moveTo(0,500)
    found=False
    while found == False:
        for _, image_pathX in busca_pagina.items():
            print("Buscando página")
            locationX = pyautogui.locateOnScreen(image_pathX, confidence=0.95)
            if locationX:
                found=True
                break

#MAIN#
busca_pagina_fun()



found = False  # Valida input de inicio
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path in input_inicio.items():
        print("For 1")
        location = pyautogui.locateOnScreen(image_path, confidence=0.95)
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
            time.sleep(0.5)
            found=True
            break

found = False # Valida icono de completar cuenta
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path1 in logeo1.items():
        print("For 2")
        location1 = pyautogui.locateOnScreen(image_path1, confidence=0.95)
        if location1:
            center = pyautogui.center(location1)
            pyautogui.click(center)
            time.sleep(0.5)
            found=True
            break

found = False # Valida botón aceptar
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path2 in aceptar1.items():
        print("For boton aceptar 1")
        location2 = pyautogui.locateOnScreen(image_path2, confidence=0.95)
        if location2:
            center = pyautogui.center(location2) 
            pyautogui.click(center)
            time.sleep(0.5)
            found=True
            break

busca_pagina_fun()

found = False # Valida botón ver_mas
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path3 in ver_mas.items():
        print("For ver mas")
        location3 = pyautogui.locateOnScreen(image_path3, confidence=0.95)
        if location3:
            center = pyautogui.center(location3) 
            pyautogui.click(center)
            time.sleep(0.5)
            found=True
            break

found=False # Validar si está en página formulario
while found == False:
    for _, image_pathX in pagina_formulario.items():
        print("Buscando página formulario")
        locationX = pyautogui.locateOnScreen(image_pathX, confidence=0.95)
        if locationX:
            found=True
            break

found = False # Valida input interno
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path4 in interno.items():
        print("For interno")
        location4 = pyautogui.locateOnScreen(image_path4, confidence=0.95)
        if location4:
            center = pyautogui.center(location4) 
            pyautogui.click(center)
            texto = full_data['interno'][0]
            pyautogui.typewrite(texto)
            time.sleep(0.5)
            found=True
            break

found = False # Valida lupa
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path5 in lupa.items():
        print("For lupa")
        location5 = pyautogui.locateOnScreen(image_path5, confidence=0.95)
        if location5:
            center = pyautogui.center(location5) 
            pyautogui.click(center) 
            time.sleep(0.8)
            found=True
            break

found = False # Valida input descripcion
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path6 in descripcion.items():
        print("For descripcion")
        location6 = pyautogui.locateOnScreen(image_path6, confidence=0.95)
        if location6:
            center = pyautogui.center(location6) 
            pyautogui.click(center)
            texto = full_data['descripcion'][0]
            pyautogui.typewrite(texto)
            time.sleep(0.8)
            found=True
            break

found = False # Valida input minutos
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path7 in minutos.items():
        print("For minutos")
        location7 = pyautogui.locateOnScreen(image_path7, confidence=0.95)
        if location7:
            center = pyautogui.center(location7) 
            pyautogui.click(center)
            texto = full_data['minutos'][0]
            pyautogui.typewrite(texto)
            time.sleep(0.3)
            found=True
            break

found = False # Valida input fecha_servicio
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path8 in fecha_servicio.items():
        print("For minutos")
        location8 = pyautogui.locateOnScreen(image_path8, confidence=0.95)
        if location8:
            center = pyautogui.center(location8) 
            pyautogui.click(center)
            texto = datetime.datetime.now().strftime("%Y/%m/%d")
            pyautogui.typewrite(texto)
            time.sleep(0.3)
            found=True
            break
        
found = False # Valida input servicio_prestado
while found == False:
    pyautogui.moveTo(0,500)
    for _, image_path9 in servicio_prestado.items():
        print("For servicio_prestado")
        location9 = pyautogui.locateOnScreen(image_path9, confidence=0.95)
        if location9:
            center = pyautogui.center(location9) 
            pyautogui.click(center)
            texto1 = full_data['servicio_prestado'][0]
            texto2 = full_data['servicio_prestado'][1]
            if texto1.endswith('1') and texto2.endswith('1'): # CERRAR PROGRAMA POR ERROR DEL CONFIG MAL LLENADO
                sys.exit()  # Cerrar el programa
            if texto1.endswith('1'): # SI ES FACTURABLE HACE ESTO
                while found == False:
                    pyautogui.moveTo(0,500)
                    for _, image_path10 in facturable.items():
                        print("For facturable")
                        location10 = pyautogui.locateOnScreen(image_path10, confidence=0.95)
                        if location10:
                            center = pyautogui.center(location10) 
                            pyautogui.click(center)
                            found=True
            if texto2.endswith('1'): # SI ES NO FACTURABLE HACE ESTO
                while found == False:
                    pyautogui.moveTo(0,500)
                    for _, image_path11 in no_facturable.items():
                        print("For no_facturable")
                        location11 = pyautogui.locateOnScreen(image_path11, confidence=0.95)
                        if location11:
                            center = pyautogui.center(location11) 
                            pyautogui.click(center)
                            found=True
            time.sleep(0.3)
            found=True
            break