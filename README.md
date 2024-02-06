# api_yatube - API для блога

## Описание проекта:

**Yatube** - проект социальной сети.

Функционал, реализованный в API для Yatube: 
- публикация, удаление и редактирование записей;
- комментирование постов;
- выбор группы для поста;
- подписка и отмена подписки на авторов.

## Стек:

- Python 3.9;
- Django 3.2.16;
- Django DRF;
- JWT + Djoser.

## Запуск проекта:

#### Развернуть виртуальное окружение:
- Linux/MacOS:
```Bash
python3 -m venv venv
```

- Windows:
```Bash
python -m venv venv
```

#### Активировать виртуальное окружение:
```Bash
source venv/bin/activate
```

#### Установить зависимости:
- Обновить pip:
```Bash
python -m pip install --upgrade pip 
```

- Установить зависимости:
```Bash
pip install -r requirements.txt
```

#### Применить миграций:
- Linux/MacOS:
```Bash
python3 manage.py migrate
```

- Windows:
```Bash
python manage.py migrate
```


#### Запустить проект:
- Linux/MacOS:
```Bash
python3 manage.py runserver
```

- Windows:
```Bash
python manage.py runserver
```

#### Создать суперпользователя:
- Linux/MacOS:
```Bash
python3 manage.py createsuperuser
```

- Windows:
```Bash
python manage.py createsuperuser
```

## Admin - панель
Доступна по эндпойнту:
```r
admin/
```

Полностью локализована и позволяет управлять пользователями и их действиями, а так же добавлять группы для постов.

## Запросы к API:

Подробная документация API доступна по эндпойнту:

```r
redoc/
```

---

#### Запросы для неавторизованных пользователей
Доступны только `GET` запросы!

- Получить список всех публикаций

```r
GET api/v1/posts/ 
```
- Параметры `limit` и `offset` для выдачи с пагинацией
```r
GET /api/v1/posts/?limit=5&offset=0
```

- Получение публикации по id
```r
GET api/v1/posts/{id}/
```

- Получение списка сообществ
```r
GET api/v1/groups/
```

- Получение информации о сообществе
```r
GET api/v1/groups/{id}/
```

- Получение комментариев к публикации
```r
GET api/v1/{post_id}/comments/
```
---
#### Работа с JWT-токеном

- Получение JWT-токена
```r
POST /api/v1/jwt/create/
```
```json
{
"username": "string",
"password": "string"
}
```
- Заголовок запроса для авторизации:

```r
Authorization: Bearer {{jwt_token}}
```

- Обновить JWT-токен:

```r
POST /api/v1/jwt/refresh/
```

- Проверить JWT-токен:

```r
POST /api/v1/jwt/verify/
```
---
#### Запросы для авторизованных пользователей:

- Создание публикации:

```r
POST /api/v1/posts/
```

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Обновление публикации:

```r
PUT /api/v1/posts/{id}/
```

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Частичное обновление публикации:

```r
PATCH /api/v1/posts/{id}/
```

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

- Удаление публикации:

```r
DEL /api/v1/posts/{id}/
```
---
Автор: [Сергей Кульбида](https://github.com/SergeyKDEV)