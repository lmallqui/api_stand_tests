import configuration
import requests
import data

#Obtener el estado de la URL de docs
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

#response = get_docs()
#print(response.status_code)

#Obtener el estado de la URL de logs
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})

#response = get_logs()
#print(response.status_code)
#print(response.headers)

#Obtener el estado de la tabla de la bd
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

#response = get_users_table()
#print(response.status_code)

#Solicitar el estado y datos de un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.json())

#Solicitar el estado y datos de los kits

def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=products_ids, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


#response = post_products_kits(data.product_ids)
#print(response.status_code)
#print(response.json()) # Muestra del resultado en la consola
