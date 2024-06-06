import requests

# Step 1: Получение токена
token_url = 'http://127.0.0.1:8000/api/token/'
data = {
    "username": "qwe",
    "email": "qwe@mail.ru",
    "password": "12345"
}

# Отправка POST запроса для получения токена
response = requests.post(token_url, data=data)

# Проверка успешного получения токена
if response.status_code == 200:
    tokens = response.json()
    access_token = tokens.get('access')
    if not access_token:
        print('Не удалось получить access token')
    else:
        print('Access token получен:', access_token)

        # Step 2: Использование токена для защищенного эндпоинта
        create_url = 'http://127.0.0.1:8000/api/project/create/'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        project_data = {
            # данные для создания проекта
            'name': 'Новый проект',
            'description': 'Описание нового проекта'
        }

        # Отправка POST запроса для создания проекта
        response = requests.post(create_url, headers=headers, json=project_data)

        # Вывод статуса и ответа сервера
        print('Статус ответа:', response.status_code)
        print('Ответ сервера:', response.json())
else:
    print('Не удалось получить токен, статус ответа:', response.status_code)
    print('Ответ сервера:', response.json())
