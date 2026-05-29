# Recipes API

Это учебный проект на Django REST framework.

Тема проекта: рецепты блюд. В API есть категории, рецепты и комментарии к рецептам.

## Как запустить

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

API:
http://127.0.0.1:8000/api/v1/

Swagger:
http://127.0.0.1:8000/api/schema/swagger-ui/

Админка:
http://127.0.0.1:8000/admin/

Логин и пароль для админки:
admin
admin12345

## Модели

Category - категория рецепта.
Поля: id, name, description.

Recipe - рецепт блюда.
Поля: id, title, category, category_id, cooking_time, difficulty, servings, is_published, ingredients, description, created_at.

Comment - комментарий к рецепту.
Поля: id, recipe, recipe_id, author_name, text, rating, created_at.

## Эндпоинты

Категории:
GET    /api/v1/categories/
GET    /api/v1/categories/{id}/
POST   /api/v1/categories/
PATCH  /api/v1/categories/{id}/
DELETE /api/v1/categories/{id}/

Рецепты:
GET    /api/v1/recipes/
GET    /api/v1/recipes/{id}/
POST   /api/v1/recipes/
PATCH  /api/v1/recipes/{id}/
DELETE /api/v1/recipes/{id}/

Фильтры для рецептов:
GET /api/v1/recipes/?category=1
GET /api/v1/recipes/?max_time=30
GET /api/v1/recipes/?difficulty=easy
GET /api/v1/recipes/?is_published=true

Групповые запросы для рецептов:
POST   /api/v1/recipes/bulk_create/
PATCH  /api/v1/recipes/bulk_update/
DELETE /api/v1/recipes/bulk_delete/

Пример для bulk_create:
[
  {
    "title": "Pancakes",
    "category_id": 1,
    "cooking_time": 25,
    "difficulty": "easy",
    "servings": 4,
    "is_published": true,
    "ingredients": "milk, eggs, flour",
    "description": "Simple recipe"
  }
]

Пример для bulk_delete:
{
  "ids": [1, 2, 3]
}

Комментарии:
GET    /api/v1/comments/
GET    /api/v1/comments/{id}/
POST   /api/v1/comments/
PATCH  /api/v1/comments/{id}/
DELETE /api/v1/comments/{id}/

Фильтр комментариев:
GET /api/v1/comments/?recipe_id=1

## Библиотеки

Все библиотеки записаны в requirements.txt.
