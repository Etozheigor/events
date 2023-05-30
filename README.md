# Events
### О проекте
Events - проект для организации мероприятий. Пользователи состоят в органазациях, одно мероприятие может быть организовано
несколькими организациями. Доступна регистрация и авторизация пользователей по токену. Есть эндпоинты для
создания организаций и мероприятий, а так же для получения мероприятий со списком пользователей, которые участвуют в организации 
мероприятия. Добавлена возможность поиска, фильтрации, сортировки и лимитной пагинации.

### Технологии
- Python
- Django
- DRF
- Djoser
- Docker
- PostgreSQL

### Как запустить проект
- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Etozheigor/events.git
```

```
cd events
```

- Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt (версии библиотек совместимы с Python версии 3.9):

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- перейти в папку events_project/events_project, создать файл .env и заполнить его по шаблону (можно использовать
файл .env.example, заполнив необходимые данные и просто переименовав его в .env) :


шаблон заполнения файла:

```
SECRET_KEY= # секретный ключ Джанго-проекта
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных (установите свой)
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST=localhost
DB_PORT=5432
```


База данных Postgres запускается в контейнере Docker:

- Перейти в папку с файлом docker-compose.yml и запустить контейнер:

```
docker-compose up
```
- Перейти в папку events_project и выполнить миграции

```
cd events_project
python manage.py makemigrations
python manage.py migrate
```

Проект будет доступен локально по адресу:

```
http://localhost/
```

Документация к Api находится по адресу:

```
http://localhost/swagger/
```