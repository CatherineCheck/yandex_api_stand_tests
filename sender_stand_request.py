
import requests
import configuration
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# def get_users_table():
#     return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
#
#     response = get_users_table()

def get_users_table():
    response = requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
    print(response.text)  # Временное логирование для проверки
    return response
