# gems_project

## Развертывание в режиме разработчика
### Клонировать репозиторий
```
git clone 
```
### Перейти в директорию medical-information-backend
```
cd gems_project
```
### Создать виртуальное окружение
```
python3.11 -m venv venv
```
### Активировать виртуальное окружение
```
source ./venv/bin/activate
```
### Обновить установщик пакетов pip
```
pip install --upgrade pip
```
### Установить зависимости
```
pip install -r requirements/dev.txt
```
### В директории stethoscope скопировать файл `.env.example` в `.env` и задать значения переменным


| Переменная | Значение по умолчанию | Описание |
| --- | --- | --- |
| DEBUG | False | Режим отладки |
| SECRET_KEY | None | `from django.core.management.utils import get_random_secret_key; get_random_secret_key()` |

```
### Применить миграции
```
python manage.py migrate
```
### Создать суперпользователя
```
python manage.py createsuperuser
```
### Запустить сервер
```
python manage.py runserver
```
### Запустить тесты
```
pytest
```

### Установка pre-commit хуков
```
pre-commit install
```
