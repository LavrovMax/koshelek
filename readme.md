# Негативные тесты для стриница регистрации https://koshelek.ru/

Зависимости проекта находятся в **requirements.txt**
Устанавливаются записимости через команду `pip install -r requirements.txt`

### Структура проекта
**locators** — тут хранятся все локаторы. 
**pages** — тут хранится структура всех страниц, на которых запускаются тесты.
**tests** - тут хранятся тесты


### Запуск тестов

`py.test` — запускаются все тесты в проекте

`py.test test_NAME_.py` — запускается один конкретный тест