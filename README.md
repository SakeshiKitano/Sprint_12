## Финальный проект 12 спринта
<hr>

## Студент: Исмаилов Саид

## <h>Когорта: #21</h>
<hr>

## <h>Project: Янедкс Самокат</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла     | Содержание файла                     |
|--------------------|--------------------------------------|
| Tests dir          | Директория с тестами                 |
| test_accordion.py  | Тесты на проверку "Вопросы о важном" |
| test_order.py      | Тесты на успешный заказ самоката     |
| test_logo.py       | Тесты на клик по Лого                |
| conftest.py        | Фикстуры                             | |
| data.py            | Файл с данными для методов           |
| helpers.py         | Генератор данных                     |
| requirements.txt   | Файл с зависимостями                 |
| allure_results.dir | Папка с отчетами Allure              |


