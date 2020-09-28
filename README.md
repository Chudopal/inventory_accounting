# Учет инвенторя на складах предприятия
### Александр Чудопал, гр 821701
Вторая лабораторная представляет из себя приложение, у которого есть определенная бизнес-логика, и которое сохраняет свои данные в базу данных.

В данной лабораторной я реализовывал приложение для учета прихода и расхода инвентаря со склада. 

Для функционирования приложения необходимо 7 таблиц: наименования инвентаря, склады, приходные накладные, множество инвентаря в приходных накладных, расходные накладные, множество инвентаря в расходных накладных, карточки для каждого наименования инвентаря.

Создаются таблицы при помощи django-моделей, находящихся в файле `storage/models.py`. В этом файле определены основные зависимости между таблицами и типы полей.

Для запросов к базе данных служит пакет `storage/database_actions`. В файле `storage/database_actions/database` определен класс-одиночка для поддержания связи с базой данных. В файле `storage/database_actions/generators` определены функции, которое пораждают функции-запросы к базе данных. Это реализовано при помощи свойства замыкания в языке python. В этом файле содержится 4 порождающих функции: для создания insert-запросов, для создания update-запросов, для создания delete-запросов, для создания select-запросов. В файле `storage/database_actions/requests.py` содержатся сами функции select-, update-, insert-, delete-запросов, созданные при помощи пораждающих функций. 

Бизнес-логика приложения содержится в файле `storage/views.py`, там же содержатся обаботчики запросов.

Для реализации приложения я выбрал фреймворки django, vue.js с ajax-запросчиком axios и СУБД postgreSQL.

Чтобы запустить данное приложение на своем компьтере необходимо:
 + Склонировать данный репозиторий
 + Установить:
    + Django==2.2 
    + psycopg2 
    + postgreSQL 12.0 
 + Сделать базу данных в postgreSQL
 + Задать переменные среды:
  ```bash
  export DB_NAME="your_db_name"
  export DB_USER="name_of_user"
  export DB_PASSWORD="password_of_db"
  export HOST="host_of_app"
  ```
 + Мигрировать таблицы базы данных:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
 + Запустить приложение:
   ```bash
   python3 manage.py runserver
   ```
 + Открыть в браузере `localhost:8000/queries`