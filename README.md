---
title: TP Final Datosvivos
emoji: 😻
colorFrom: purple
colorTo: indigo
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: mit
short_description: Estimador de precios de una vivienda
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


## Estimador de Precios de viviendas

* El link al Space de Hugging Face

[Abrir la aplicación en Hugging Face Spaces](https://huggingface.co/spaces/MEMONSE/TP_Final_Datosvivos)

* Foto de la pantalla de la aplicación en funcionamiento.

![App en funcionamiento](Interfaz.jpg)


* 🚀 Ejemplo de uso del endpoint de Hugging Face

Una vez desplegada la aplicación en **Hugging Face Spaces**, Gradio genera automáticamente un endpoint público que permite consumir el modelo desde cualquier entorno de Python.

Primero se debera instalar  gradio_client (pip install gradio_client)

Ejecutar => test_api.py (en caso de no tener instalado gradio_client , descomentar la parte "!pip install gradio_client" que se encuentra en la primer línea de codico test_api.py)


* Por otro lado, en la interfaz se genero un botón "🎯 Probar con datos de ejemplo" , que ejecuta otro ejemplo rooms=3,
	bedrooms=2,
	bathrooms=1,
	surface_total=60,
	surface_covered=55,
	place_name="Palermo",
	property_type="Departamento",
	state_name="Capital Federal"
	
