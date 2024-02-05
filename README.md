# api_yatube - API для блога

## Описание проекта:

**Блогикум** - платформа для публикации личных дневников.

## Установка:

### 1) Клонировать проект:
```Bash
git clone git@github.com:SergeyKDEV/homework_bot.git
```

### 2) Развернуть виртуальное окружение:
- Linux/MacOS:
```Bash
python3 -m venv venv
```

- Windows:
```Bash
python -m venv venv
```

### 3) Активировать виртуальное окружение:
```Bash
source venv/bin/activate
```

### 4) Установить зависимости:
- Обновить pip:
```Bash
python -m pip install --upgrade pip 
```

- Установить зависимости:
```Bash
pip install -r requirements.txt
```

### 5) Запуск проекта:
- Linux/MacOS:
```Bash
source venv/bin/activate
```

- Windows:
```Bash
source venv/Scripts/activate
```

## Описание API:

- Подробная документация API доступна по эндпойнту:
```
http://{api_url}/redoc/
```

---

### Posts (Посты)

#### Получить все посты
- **Endpoint:** `/api/v1/posts/`
- **Метод:** `GET`
- **Описание:** Получить список всех постов.

#### Получить конкретный пост
- **Endpoint:** `/api/v1/posts/{id}/`
- **Метод:** `GET`
- **Описание:** Получить детали конкретного поста по его идентификатору.

#### Получить комментарии к посту
- **Endpoint:** `/api/v1/posts/{post_id}/comments/`
- **Метод:** `GET`
- **Описание:** Получить комментарии к конкретному посту.

#### Получить конкретный комментарий
- **Endpoint:** `/api/v1/posts/{post_id}/comments/{id}/`
- **Методы:** `GET`
- **Описание:** Получить детали конкретного комментария к посту.

### Groups (Группы)

#### Получить все группы
- **Endpoint:** `/api/v1/groups/`
- **Метод:** `GET`
- **Описание:** Получить список всех групп.

#### Получить конкретную группу
- **Endpoint:** `/api/v1/groups/{id}/`
- **Метод:** `GET`
- **Описание:** Получить детали конкретной группы по ее идентификатору.

### Follow (Подписки)

#### Управление подписками
- **Endpoint:** `/api/v1/follow/`
- **Методы:** `GET`, `POST`
- **Описание:** Просмотр и создание отношений подписок.

### JWT Authentication (JWT Аутентификация)

#### Создать JWT-токен
- **Endpoint:** `/api/v1/jwt/create/`
- **Метод:** `POST`
- **Описание:** Создать JWT-токен для аутентификации.

#### Обновить JWT-токен
- **Endpoint:** `/api/v1/jwt/refresh/`
- **Метод:** `POST`
- **Описание:** Обновить существующий JWT-токен.

#### Проверить JWT-токен
- **Endpoint:** `/api/v1/jwt/verify/`
- **Метод:** `POST`
- **Описание:** Проверить валидность JWT-токена.