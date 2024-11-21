# Django Users API

Цей проект реалізує веб-додаток на Django для виконання CRUD операцій з користувачами. Користувачі можуть бути створені, отримані, оновлені та видалені через API.


## Запуск додатку

1.	Міграція бази даних:
Виконайте команду для створення таблиць в базі даних:
```bash
python manage.py migrate
```
2.	Запуск сервера:
Запустіть сервер для тестування API:
```txt
python manage.py runserver
```

### Інтерфейс API:
API підтримує наступні маршрути для роботи з користувачами:
- **POST /users/create/**: Створення нового користувача.
- **GET /users/<user_id>/**: Отримання користувача за ID.
- **PUT /users/<user_id>/update/**: Оновлення даних користувача за ID.
- **DELETE /users/<user_id>/delete/**: Видалення користувача за ID.
#### Тестування через Postman

Використовуйте Postman для тестування CRUD операцій, надсилаючи відповідні запити на вищеописані маршрути.

Файл для швидкого імпорту у постмен `django_users_postman_collection.json`