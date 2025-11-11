#!pip install gradio_client

from gradio_client import Client

client = Client("MEMONSE/TP_Final_Datosvivos")
result = client.predict(
	rooms=4,
	bedrooms=3,
	bathrooms=1,
	surface_total=60,
	surface_covered=55,
	place_name="Belgrano",
	property_type="Departamento",
	state_name="Capital Federal",
	api_name="/predict"
)
print(result)