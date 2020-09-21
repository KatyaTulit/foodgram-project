![foodgram_workflow](https://github.com/turbokach/foodgram-project/workflows/foodgram_workflow/badge.svg?branch=master)

# Foodgram-project
http://84.201.142.109/
## Описание
Приложение «Продуктовый помощник»: сайт, на котором пользователи публикуют рецепты, добавляют чужие рецепты в избранное и подписываются на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Стек технологий
- Python
- Django
- PostgreSQL
- Docker
- Nginx
- Gunicorn
- Git / GitHub actions

## Как запустить проект, используя Docker (база данных PostgreSQL):
1) Клонируйте репозиторий с проектом:
```
git clone https://github.com/turbokach/foodgram-project.git
```

3) С помощью Dockerfile и docker-compose.yaml разверните проект:
```
docker-compose up -d --build -V
```

###### Аккаунт суперпользователя после деплоя
http://127.0.0.1/admin/panel/
Login: admin
Password: fisting
