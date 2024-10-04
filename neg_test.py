import sender_stand_request
import data
# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
# эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body
# Тест 11. Ошибка
# Параметр fisrtName состоит из пустой строки
def test_create_user_empty_first_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body("")
    # Проверка полученного ответа
    negative_assert_no_first_name(user_body)
# Функция для позитивной проверки
# def negative_assert_symbol(first_name):
#     # В переменную user_body сохраняется обновлённое тело запроса
#     user_body = get_user_body(first_name)
#     # В переменную user_response сохраняется результат запроса на создание пользователя:
#     user_response = sender_stand_request.post_new_user(user_body)
#
#     # Проверяется, что код ответа равен 201
#     assert user_response.status_code == 400
#     assert user_response.json()['code'] == 400
#     assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
#                                             "Имя может содержать только русские или латинские буквы, " \
#                                             "длина должна быть не менее 2 и не более 15 символов"

    # # В переменную users_table_response сохраняется результат запроса на получение данных из таблицы user_model
    # users_table_response = sender_stand_request.get_users_table()
    #
    # # Строка, которая должна быть в ответе
    # str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
    #            + user_body["address"] + ",,," + user_response.json()["authToken"]
    #
    # # Проверка, что такой пользователь есть и он единственный
    # assert users_table_response.text.count(str_user) == 1
def negative_assert_no_first_name(first_name):
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(first_name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    user_response = sender_stand_request.post_new_user(user_body)

    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 400
    assert user_response.json()['code'] == 400
    assert user_response.json()["message"] == "Не все необходимые параметры были переданы"

    # # Тест 10. Ошибка
    # # В запросе нет параметра firstName
    # def test_create_user_no_first_name_get_error_response():
    #     # Копируется словарь с телом запроса из файла data в переменную user_body
    #     # Иначе можно потерять данные из исходного словаря
    #     user_body = data.user_body.copy()
    #     # Удаление параметра firstName из запроса
    #     user_body.pop("firstName")
    #     # Проверка полученного ответа
    #     negative_assert_no_first_name(user_body)
# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test_create_user_no_first_name_get_error_response():
    negative_assert_no_first_name("")