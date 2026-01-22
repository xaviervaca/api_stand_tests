import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_log():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body,
                         headers = data.headers)

def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json = product_ids,
                         headers = data.headers)
"""
OBTIENE LOS KITS
response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())


CREA USUARIO
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())              

OBTIENE LA TABLA 
response = get_users_table()
print(response.status_code)

OBTIENE LOS LOGS
response = get_log()
print(response.status_code)
print(response.headers)"""

