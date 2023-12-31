Наименование проекта ПЕРЕВАЛЫ

ОПИСАНИЕ Данное мобильное приложение разработано для упрощения задачи туристам по отправке данных о перевале. Оно позволяет туристам вносить данные о перевале и отправлять их в ФСТР, как только появится доступ в Интернет. Модератор из федерации верифицирует и вносит в базу данных информацию, а пользователи могут просматривать статус модерации и просматривать базу с объектами, внесенными другими.

РЕАЛИЗАЦИЯ

МЕТОДЫ:

Метод POST /submitData - для отправки данных о перевале на сервер. Параметры запроса: JSON-объект с полями, описывающими информацию о перевале: beauty_title, title, other_titles, connect, add_time, user, coords, level, images.

Метод GET /submitData/ - для получения одной записи (перевала) по ее id. Параметры запроса: id - уникальный идентификатор записи (перевала).

Метод PATCH /submitData/ - для редактирования существующей записи (перевала), если она в статусе "new". Параметры запроса: id - уникальный идентификатор записи (перевала). JSON-объект с полями, которые необходимо отредактировать.

Метод GET /submitData/?user__email= - для получения списка данных обо всех объектах, которые пользователь с почтой отправил на сервер. Параметры запроса: user__email - адрес электронной почты пользователя.

ПРОГРАММЫ И ТЕХНОЛОГИИ:

Django 4.2.3
Django REST framework 3.14.0
Pillow 10.0.0
Swagger
УСТАНОВКА И ЗАПУСК

Клонируйте репозиторий проекта на свой компьютер.
Установите все зависимости, указанные в файле requirements.txt.
Выполните миграции для создания базы данных и таблиц.
Запустите сервер командой "python manage.py runserver".
Приложение будет доступно по адресу "http://localhost:8000".