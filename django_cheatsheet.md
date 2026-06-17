# Django шпаргалка

## Базові команди

```powershell
django-admin startproject mysite
python manage.py runserver
python manage.py startapp blog
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Що означає кожна команда

- `startproject` - створює новий Django-проєкт
- `runserver` - запускає локальний сервер
- `startapp` - створює новий застосунок всередині проєкту
- `makemigrations` - готує зміни для бази даних
- `migrate` - застосовує зміни до бази даних
- `createsuperuser` - створює адміністратора для `/admin`

## Типовий порядок роботи

1. Створити проєкт
2. Створити app
3. Додати app в `INSTALLED_APPS`
4. Описати моделі
5. Запустити `makemigrations`
6. Запустити `migrate`
7. Створити суперкористувача
8. Запустити `runserver`

## Корисні команди

```powershell
python manage.py shell
python manage.py test
python manage.py showmigrations
python manage.py createsuperuser
```

## Міні-підказка

- Якщо не пам'ятаєш, спочатку думай про 3 кроки: `startapp`, `makemigrations`, `migrate`
- Якщо сайт не відкривається, перевір `runserver`
- Якщо адмінка недоступна, перевір `createsuperuser`
