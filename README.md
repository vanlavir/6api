# Recipes API

## Описание проекта

Recipes API - учебный REST API на Django REST framework для предметной области рецептов блюд.

Проект позволяет хранить и обрабатывать данные о категориях рецептов, самих рецептах и комментариях пользователей к рецептам. API поддерживает получение одного ресурса, получение списков с фильтрами, создание одного или нескольких ресурсов, частичное обновление, массовое обновление и удаление.

## Основной функционал

- CRUD для категорий рецептов.
- CRUD для рецептов блюд.
- CRUD для комментариев к рецептам.
- Фильтрация данных через GET-параметры.
- Создание группы ресурсов через JSON-массив.
- Массовое обновление через `bulk-update`.
- Массовое удаление через `bulk-delete`.
- Swagger/OpenAPI-документация.
- Управление данными через Django admin.
- Работа с базой данных PostgreSQL.

## Адреса проекта

| Адрес | Назначение |
|---|---|
| `http://127.0.0.1:8000/api/v1/` | Главная страница API |
| `http://127.0.0.1:8000/admin/` | Админ-панель Django |
| `http://127.0.0.1:8000/api/schema/` | OpenAPI-схема |
| `http://127.0.0.1:8000/api/schema/swagger-ui/` | Swagger-документация |

## Модели

### Category

Категория рецепта.

Поля: `id`, `name`, `description`.

### Recipe

Рецепт блюда.

Поля: `id`, `title`, `category`, `category_id`, `cooking_time`, `difficulty`, `servings`, `is_published`, `ingredients`, `description`, `created_at`.

### Comment

Комментарий к рецепту.

Поля: `id`, `recipe`, `recipe_id`, `author_name`, `text`, `rating`, `created_at`.

## Эндпоинты

### Categories

| Метод | Эндпоинт | Описание |
|---|---|---|
| GET | `/api/v1/categories/` | Получить список категорий |
| POST | `/api/v1/categories/` | Создать одну категорию или группу категорий |
| GET | `/api/v1/categories/{id}/` | Получить категорию по id |
| PATCH | `/api/v1/categories/{id}/` | Частично обновить категорию |
| DELETE | `/api/v1/categories/{id}/` | Удалить категорию |
| PATCH | `/api/v1/categories/bulk-update/` | Обновить группу категорий |
| DELETE | `/api/v1/categories/bulk-delete/?ids=1,2,3` | Удалить группу категорий |

Фильтры:

| Параметр | Пример | Описание |
|---|---|---|
| `name` | `/api/v1/categories/?name=salad` | Поиск по названию категории |

### Recipes

| Метод | Эндпоинт | Описание |
|---|---|---|
| GET | `/api/v1/recipes/` | Получить список рецептов |
| POST | `/api/v1/recipes/` | Создать один рецепт или группу рецептов |
| GET | `/api/v1/recipes/{id}/` | Получить рецепт по id |
| PATCH | `/api/v1/recipes/{id}/` | Частично обновить рецепт |
| DELETE | `/api/v1/recipes/{id}/` | Удалить рецепт |
| PATCH | `/api/v1/recipes/bulk-update/` | Обновить группу рецептов |
| DELETE | `/api/v1/recipes/bulk-delete/?ids=1,2,3` | Удалить группу рецептов |

Фильтры:

| Параметр | Пример | Описание |
|---|---|---|
| `title` | `/api/v1/recipes/?title=pancake` | Поиск по названию |
| `category_id` | `/api/v1/recipes/?category_id=1` | Фильтр по категории |
| `max_time` | `/api/v1/recipes/?max_time=30` | Рецепты с временем приготовления не больше указанного |
| `difficulty` | `/api/v1/recipes/?difficulty=easy` | Фильтр по сложности |
| `is_published` | `/api/v1/recipes/?is_published=true` | Фильтр по публикации |

### Comments

| Метод | Эндпоинт | Описание |
|---|---|---|
| GET | `/api/v1/comments/` | Получить список комментариев |
| POST | `/api/v1/comments/` | Создать один комментарий или группу комментариев |
| GET | `/api/v1/comments/{id}/` | Получить комментарий по id |
| PATCH | `/api/v1/comments/{id}/` | Частично обновить комментарий |
| DELETE | `/api/v1/comments/{id}/` | Удалить комментарий |
| PATCH | `/api/v1/comments/bulk-update/` | Обновить группу комментариев |
| DELETE | `/api/v1/comments/bulk-delete/?ids=1,2,3` | Удалить группу комментариев |

Фильтры:

| Параметр | Пример | Описание |
|---|---|---|
| `recipe_id` | `/api/v1/comments/?recipe_id=1` | Фильтр по рецепту |
| `author_name` | `/api/v1/comments/?author_name=Ivan` | Поиск по имени автора |
| `rating` | `/api/v1/comments/?rating=5` | Фильтр по оценке |

## Библиотеки

Все использованные библиотеки указаны в `requirements.txt`.
