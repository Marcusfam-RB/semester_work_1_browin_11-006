#Семестровая работа Бровина Романа 11-006

## Установка и запуск проекта

- python3 -m venv .venv - создать виртуальное окружение
- cd .venv/bin/activate - войти в виртуальное окружение
- pip install -r requirements.txt - установить зависимости
- создайте новую базу данных postgresql
- app.config['SQLALCHEMY_DATABASE_URI'] = postgresql://user_name:password@localhost:5432(localhost)/name_db - прописать в файле takeasemester/semester/__init__.py 
- set FLASKAPP - flaskapp.py - укажите приложение
- flask db init - создайте базу данных
- flask db migrate - создайте миграции
- flask db upgrade - примените миграции к базе данных
- run flask - запустите приложение
