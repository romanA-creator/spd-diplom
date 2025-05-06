# Документация по запуску и работе с проектом


## Описание проекта

Этот проект представляет собой backend для социальной сети фотографий. Он включает в себя следующие функции:

* Регистрация и аутентификация пользователей.
* Создание, получение, обновление и удаление постов.
* Комментирование постов.
* Лайки постов.

## Требования

Для запуска проекта вам понадобятся следующие зависимости:

Python 3.8+
Django 3.2+
Django REST Framework
djangorestframework-simplejwt

## Установка
Клонируйте репозиторий:

git clone https://github.com/romanA-creator/spd-diplom.git

Установите зависимости:

cd your-project
pip install -r requirements.txt

## Настройка DATABASES для PostgreSQL

Для использования PostgreSQL в качестве базы данных нужно ее установить на компьютер и настроить.
Затем добавьте следующие настройки в settings.py:
# Настройка DATABASES для PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Поменяйте в шаблоне настройки на свои для NAME,USER,PASSWORD

Создайте базу данных:

python manage.py migrate

Создайте суперюзера (для доступа к административной панели):

python manage.py createsuperuser

Настройка SIMPLE_JWT

Вы можете поменять по желанию ACCESS_TOKEN_LIFETIME и REFRESH_TOKEN_LIFETIME в settings.py

Запуск проекта
Запустите сервер разработки:

python manage.py runserver
Откройте браузер и перейдите по адресу http://localhost:8000/admin/ для доступа к административной панели.

Тестирование API
Вы можете использовать Postman для тестирования API. Вот несколько примеров запросов:

1. Регистрация пользователя

curl -X POST http://localhost:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{
  "username": "new_user",
  "email": "new_user@example.com",
  "password": "new_password"
}'

2. Получение токена

curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{
  "username": "new_user",
  "password": "new_password"
}'

3. Создание поста

curl -X POST http://localhost:8000/api/posts/ \
-H "Authorization: Bearer your_access_token" \
-F "text=Новый пост" \
-F "image=@/path/to/your/image.jpg"

4. Получение списка постов

curl -X GET http://localhost:8000/api/posts/ \
-H "Authorization: Bearer your_access_token"

5. Получение конкретного поста

curl -X GET http://localhost:8000/api/posts/1/ \
-H "Authorization: Bearer your_access_token"

6. Редактирование поста

curl -X PUT http://localhost:8000/api/posts/1/ \
-H "Authorization: Bearer your_access_token" \
-H "Content-Type: application/json" \
-d '{
  "text": "Обновленный текст"
}'

7. Удаление поста

curl -X DELETE http://localhost:8000/api/posts/1/ \
-H "Authorization: Bearer your_access_token"


8. Создание комментария

curl -X POST http://localhost:8000/api/comments/ \
-H "Authorization: Bearer your_access_token" \
-d '{
  "post": 1,
  "text": "Отличный пост!"
}'

9. Создание лайка

curl -X POST http://localhost:8000/api/likes/ \
-H "Authorization: Bearer your_access_token" \
-d '{
  "post": 1
}'