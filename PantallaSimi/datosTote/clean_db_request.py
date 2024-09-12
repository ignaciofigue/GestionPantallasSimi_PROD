import requests

# Definimos la URL de la vista y el valor de la palabra clave
url = 'http://127.0.0.1:8000/limpiarbbdd'
palabra_clave = 'acm1pt'

# Creamos un diccionario con los parámetros de la solicitud
params = {'palabra_clave': palabra_clave}

# Realizamos la solicitud GET
response = requests.get(url, params=params)

# Verificamos el código de estado de la respuesta
if response.status_code == 200:
    # La solicitud fue exitosa, imprimimos el contenido de la respuesta
    print(response.text)
else:
    # Hubo un error en la solicitud, imprimimos el código de estado
    print(f'Error: {response.status_code}')