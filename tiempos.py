import json
import os
import shutil
import pyautogui
import datetime
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from cryptography.fernet import Fernet  # Importar el módulo Fernet para encriptar y desencriptar
#import base64
pyautogui.FAILSAFE=False

#def generate_fernet_key():
    # Generate a 32-byte key and return it as a URL-safe base64-encoded string
    #return Fernet.generate_key().decode()

#def encrypt_password(password, key):
    #cipher_suite = Fernet(key.encode())
    #encrypted_password = cipher_suite.encrypt(password.encode())
    #return encrypted_password

#def decrypt_password(encrypted_password, key):
    #cipher_suite = Fernet(key.encode())
    #decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    #return decrypted_password

busca_pagina = {
    "pagina": os.path.join("imgs","pagina.png"),
}
pagina_formulario = { # Validación si está en página formulario
    "pagina_formulario": os.path.join("imgs","pagina_formulario.png"),
}

# Opciones para los menús desplegables
dropdown_options = {
    "producto": ["Desarrollos Nuevos Productos", "Hagenet", "Facturacion Bancolombia", "control tiempos Web", "Sistema de Tiempos", "Seguridad", "Agente", "Generador de codigo", "WFS  SYSTEM", "DotProyect", "Componentes", "Cartas Laborales", "iBono", "Pruebas", "Página Web", "Institucional Paula Andrea Betancur", "Área digital", "Marketing digital"],
    "contacto": ["Milena Maria Castrillon", "Alejandro Vélez Uribe", "Andrea Alvarez", "Andres Felipe Garcia Serna", "Armando Alberto Acuña", "CARLOS ANDRES MONTEALEGRE", "CATERIN JOHANA VASQUEZ ARISTIZABAL", "CLAUDIA PATRICIA NARANJO", "Diana Baquero", "DIANA MATILDE CORREA AVILA", "Edgar Andres Prada", "Edgar Mauricio Roman", "GIOVANNY GOMEZ CONVERS", "JAMES TORRES OBANDO", "Juan Jose Ruiz", "Luis Alfonso Arango", "Luz Stella Botero", "MAIRA CRISTINA CASTRILLON MONTOYA", "Maria Alejandra Velez", "Nubia Yolanda Urrego", "Oscar Daniel Londoño", "Robinson Munoz", "Sebastian Bermudez", "VICKY LORENA VELASCO RODRIGUEZ", "VICTOR HUGO OSORIO BOTERO"],
    "centro_de_costo": ["Stand By", "Incidentes", "Factor", "Proyectos", "Infraestructura"],
    "actividad": ["Asunto Interno", "Asunto Personal", "Atencion al Cliente", "Auditoria", "Capacitación", "Compensatorio", "Daily", "Estimación", "Factor", "Garantía", "Incapacidad", "Laboratorios", "Overhead", "Problemas Infraestructura", "Registro Tiempos", "Reunión Interna", "Sin Asignación por Cliente", "Sin Asignación por Nexos", "Stand By", "Suspensión administrativa", "Vacaciones"],
    "servicio_prestado": ["Facturable", "No Facturable"]
}

def busca_pagina_fun():
    pyautogui.moveTo(0,500)
    found=False
    while found == False:
        for _, image_pathX in busca_pagina.items():
            print("Buscando página")
            locationX = pyautogui.locateOnScreen(image_pathX, confidence=0.95)
            if locationX:
                print("Página encontrada")
                found=True
                break

full_data = {}  # Variable global para guardar los datos cargados desde el JSON
nuevo_nombre = "config_tiempos_2.json"

def ejecutar_programa():
    global full_data
    #password_key = generate_fernet_key()
    
    # Actualizar los campos del JSON con los datos ingresados por el usuario
    for key, entry in entries.items():
        #if key == "password":
            #full_data['password'][0] = encrypt_password(full_data['password'][0], password_key)
        if key in dropdown_options:
            selected_option = entry.get()  # Obtener la variable de control del menú desplegable
            full_data[key] = [selected_option]  # Actualizar el campo en el JSON
        elif isinstance(entry, tk.Text):  # Verificar si el widget es Text
            full_data[key] = [entry.get("1.0", tk.END).strip()]  # Obtener todo el texto y eliminar espacios en blanco
        else:
            full_data[key] = [entry.get()]  # Para Entry, obtener el texto sin índice
            
    # Guardar los cambios en el JSON
    with open("config_tiempos.json", "w") as file:
        json.dump(full_data, file)
    
    # Usar selenium para interactuar con la página web
    driver = webdriver.Chrome()  # Reemplaza 'Chrome' con el nombre del navegador que quieras usar

    driver.get('http://181.129.9.162:2523/SCTWEB/Paginas/LogIN.aspx')

    busca_pagina_fun() # Valida si entró a la página de logeo

    # Llenar los campos del formulario
    usuario_input = driver.find_element(By.ID, "ASPxRoundPanel1_txtUsuario")
    clave_input = driver.find_element(By.ID, "ASPxRoundPanel1_txtClave")

    if usuario_input and clave_input:
        usuario_input.send_keys(full_data['usuario'][0])
        clave_input.send_keys(full_data['password'][0])
        print("inputs encontrados")
    else:
        print("Los campos del formulario no se encontraron.")

    
    # Encontrar y hacer clic en el botón de "Aceptar"
    aceptar_button = driver.find_element(By.ID, "ASPxRoundPanel1_Button1")
    aceptar_button.click()
    
    busca_pagina_fun() # Valida si entró a la cuenta
    
    # Encontrar y hacer clic en el enlace "Ver mas..."
    ver_mas_link = driver.find_element(By.LINK_TEXT, "Ver mas...")
    ver_mas_link.click()
    
    found=False # Validar si está en página formulario
    while found == False:
        for _, image_pathX in pagina_formulario.items():
            print("Buscando página formulario")
            locationX = pyautogui.locateOnScreen(image_pathX, confidence=0.95)
            if locationX:
                found=True
                break
            
    interno_input = driver.find_element(By.ID, "ContentPlaceHolder3_txtInterno")
    interno_input.send_keys(full_data['interno'][0])
    
    lupa_button = driver.find_element(By.ID, "ContentPlaceHolder3_ImageButton1")
    lupa_button.click()
    
    # Obtener el elemento del menú desplegable
    producto_select = Select(driver.find_element(By.ID, "ContentPlaceHolder3_cboProducto"))
    # Seleccionar la opción correspondiente al valor almacenado en el JSON
    producto_select.select_by_visible_text(full_data['producto'][0])
    
    # Obtener el elemento del menú desplegable
    producto_select = Select(driver.find_element(By.ID, "ContentPlaceHolder3_cboContacto"))
    # Seleccionar la opción correspondiente al valor almacenado en el JSON
    producto_select.select_by_visible_text(full_data['contacto'][0])
    
    # Obtener el elemento del menú desplegable
    producto_select = Select(driver.find_element(By.ID, "ContentPlaceHolder3_cboCentroCosto"))
    # Seleccionar la opción correspondiente al valor almacenado en el JSON
    producto_select.select_by_visible_text(full_data['centro_de_costo'][0])
    
    # Obtener el elemento del menú desplegable
    producto_select = Select(driver.find_element(By.ID, "ContentPlaceHolder3_cboActividad"))
    # Seleccionar la opción correspondiente al valor almacenado en el JSON
    producto_select.select_by_visible_text(full_data['actividad'][0])
    
    # Obtener el elemento del menú desplegable
    producto_select = Select(driver.find_element(By.ID, "ContentPlaceHolder3_cboServicio"))
    # Seleccionar la opción correspondiente al valor almacenado en el JSON
    producto_select.select_by_visible_text(full_data['servicio_prestado'][0])
    
    texto = datetime.datetime.now().strftime("%Y/%m/%d")
    # Obtener el elemento de la fecha
    interno_input = driver.find_element(By.ID, "ContentPlaceHolder3_txtFecha")
    interno_input.send_keys(texto)
    
    interno_input = driver.find_element(By.ID, "ContentPlaceHolder3_txtMinutos")
    interno_input.send_keys(full_data['minutos'][0])
    
    interno_input = driver.find_element(By.ID, "ContentPlaceHolder3_txtDescripcion")
    interno_input.send_keys(full_data['descripcion'][0])
    
    lupa_button = driver.find_element(By.ID, "ContentPlaceHolder3_btnAceptar")
    lupa_button.click()
    
    os.remove(nuevo_nombre)
    
    root = tk.Tk()
    root.title("Tarea Completada")
    
    # Mostrar el mensaje de aviso y el botón "Aceptar"
    aviso_frame = tk.Frame(root)
    aviso_frame.pack(pady=10)
    
    mensaje_aviso = tk.Label(aviso_frame, text="Tiempos llenados, pulse aceptar para cerrar.")
    mensaje_aviso.pack()

    boton_aceptar = tk.Button(aviso_frame, text="Aceptar", command=root.quit)
    boton_aceptar.pack()

# Función para crear menús desplegables
def create_dropdown(frame, options):
    var_dropdown = tk.StringVar(frame)
    var_dropdown.set(options[0])  # Valor por defecto

    dropdown = tk.OptionMenu(frame, var_dropdown, *options)
    dropdown.pack()

    return var_dropdown  # Devolver solo la variable de control

def renombrar_primer_json():
    # Obtener la lista de archivos en la carpeta raíz
    archivos_en_carpeta = os.listdir()

    # Buscar el primer archivo JSON en la lista
    for archivo in archivos_en_carpeta:
        if archivo.endswith(".json"):
            # Renombrar el archivo a 'config_tiempos.json'
            nuevo_nombre = 'config_tiempos.json'
            os.rename(archivo, nuevo_nombre)
            break  # Detener el bucle después de renombrar el primer archivo encontrado

def cargar_json_y_confirmar():
    # Llamar a la función para renombrar el primer archivo JSON
    renombrar_primer_json()
    global entries, full_data, var_producto, var_contacto, var_centro_de_costo, var_actividad, var_servicio_prestado, password_key  # Declarar las variables como globales
    with open("config_tiempos.json", "r") as file:
        full_data = json.load(file)

    root = tk.Tk()
    root.title("Registrar Tiempos")

    confirmacion_frame = tk.Frame(root)
    confirmacion_frame.pack(pady=10)

    entries = {}  # Diccionario para almacenar los widgets Entry

    #password_key = generate_fernet_key()

    for key, value in full_data.items():
        label = tk.Label(confirmacion_frame, text=key + ":")
        label.pack()

        if key == "password":  # Check if it's the password field
            #password = full_data['password'][0]
            #full_data['password'][0] = decrypt_password(password, password_key)
            #print("Contrasena desencriptada:", full_data['password'][0])
            
            entry = tk.Entry(confirmacion_frame, show="*")  # Use 'show' to hide the password characters
        elif key == "descripcion":
            entry = tk.Text(confirmacion_frame, height=3, wrap=tk.WORD, width=50)
        else:
            entry = tk.Entry(confirmacion_frame)

        if key == "password":  # Check if it's the password field
            entry = tk.Entry(confirmacion_frame, show="*")  # Use 'show' to hide the password characters
            entry.insert(0, value[0])  # Add the existing password to the entry field
        elif key == "descripcion":
            entry = tk.Text(confirmacion_frame, height=3, wrap=tk.WORD, width=50)
            entry.insert("1.0", value[0])  # Usar el índice correcto "1.0" para Text
        else:
            entry = tk.Entry(confirmacion_frame)
            entry.insert(0, value[0])  # Usar el índice "0" para Entry

        if key == "producto":
            options = ["Desarrollos Nuevos Productos", "Hagenet", "Facturacion Bancolombia","control tiempos Web","Sistema de Tiempos","Seguridad","Agente","Generador de codigo","WFS  SYSTEM","DotProyect","Componentes","Cartas Laborales","iBono","Pruebas","Página Web","Institucional Paula Andrea Betancur","Área digital","Marketing digital"]  # Opciones personalizadas para el drop-down
            var_producto = create_dropdown(confirmacion_frame, options)
            var_producto.set(value[0])  # Cargar el valor por defecto del menú desplegable desde el JSON
            entries[key] = var_producto  # Asigna solo la variable de control al diccionario
        elif key == "contacto":
            options = ["Milena Maria Castrillon", "Alejandro Vélez Uribe", "Andrea Alvarez","Andres Felipe Garcia Serna","Armando Alberto Acuña","CARLOS ANDRES MONTEALEGRE","CATERIN JOHANA VASQUEZ ARISTIZABAL","CLAUDIA PATRICIA NARANJO","Diana Baquero","DIANA MATILDE CORREA AVILA","Edgar Andres Prada","Edgar Mauricio Roman","GIOVANNY GOMEZ CONVERS","JAMES TORRES OBANDO","Juan Jose Ruiz","Luis Alfonso Arango","Luz Stella Botero","MAIRA CRISTINA CASTRILLON MONTOYA","Maria Alejandra Velez","Nubia Yolanda Urrego","Oscar Daniel Londoño","Robinson Munoz","Sebastian Bermudez","VICKY LORENA VELASCO RODRIGUEZ","VICTOR HUGO OSORIO BOTERO"]  # Opciones personalizadas para el drop-down
            var_contacto = create_dropdown(confirmacion_frame, options)
            var_contacto.set(value[0])  # Cargar el valor por defecto del menú desplegable desde el JSON
            entries[key] = var_contacto  # Asigna solo la variable de control al diccionario
        elif key == "centro_de_costo":
            options = ["Stand By", "Incidentes", "Factor","Proyectos","Infraestructura"]  # Opciones personalizadas para el drop-down
            var_centro_de_costo = create_dropdown(confirmacion_frame, options)
            var_centro_de_costo.set(value[0])  # Cargar el valor por defecto del menú desplegable desde el JSON
            entries[key] = var_centro_de_costo  # Asigna solo la variable de control al diccionario
        elif key == "actividad":
            options = ["Asunto Interno","Asunto Personal", "Atencion al Cliente", "Auditoria","Capacitación","Compensatorio","Daily","Estimación","Factor","Garantía","Incapacidad","Laboratorios","Overhead","Problemas Infraestructura","Registro Tiempos","Reunión Interna","Sin Asignación por Cliente","Sin Asignación por Nexos","Stand By","Suspensión administrativa","Vacaciones"]  # Opciones personalizadas para el drop-down
            var_actividad = create_dropdown(confirmacion_frame, options)
            var_actividad.set(value[0])  # Cargar el valor por defecto del menú desplegable desde el JSON
            entries[key] = var_actividad  # Asigna solo la variable de control al diccionario
        elif key == "servicio_prestado":
            options = ["Facturable","No Facturable"]  # Opciones personalizadas para el drop-down
            var_servicio_prestado = create_dropdown(confirmacion_frame, options)
            var_servicio_prestado.set(value[0])  # Cargar el valor por defecto del menú desplegable desde el JSON
            entries[key] = var_servicio_prestado  # Asigna solo la variable de control al diccionario
        else:
            entry.pack()
            entries[key] = entry
    file.close()

    shutil.copy("config_tiempos.json", nuevo_nombre)

    boton_si = tk.Button(confirmacion_frame, text="Continuar", command=ejecutar_programa)
    boton_si.pack(side=tk.LEFT, padx=5)

    boton_no = tk.Button(confirmacion_frame, text="Cancelar", command=root.destroy)
    boton_no.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
        cargar_json_y_confirmar()