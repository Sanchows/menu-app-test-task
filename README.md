[![Python 3.11](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/downloads/release/python-3110/)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%23316192.svg?style=for-the-badge&logo=docker&logoColor=white)
### Задача
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
 
Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
{% draw_menu 'main_menu' %}
 
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний.

Задание выложить на гитхаб.

### TODO
- Implement a expanding/collapsing items by selected item


### Starting the project
1. Clone it
   `https://github.com/Sanchows/menu-app-test-task.git`

2. Create `.env` file in the project root `touch .env` containing this variables:
```
SECRET_KEY=<your_secret_here>
DJANGO_SUPERUSER_USERNAME=<your_django_superuser_username>
DJANGO_SUPERUSER_PASSWORD=<your_django_superuser_password>
DJANGO_SUPERUSER_EMAIL=someone@company.local
DB_NAME=<your_db_name_here>
DB_USER=<your_db_user_here>
DB_PASSWORD=<your_db_password_here>
DB_HOST=db
DB_PORT=5432
```

3. Start docker containers `docker-compose up --build`

4. That's it. Go to the `localhost:8000/`

5. Admin-panel: `localhost:8000/admin`
