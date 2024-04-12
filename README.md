# Test-cases.py

## Описание программы test-cases.py

На странице https://www.avito.ru/avito-care/eco-impact расположены три счётчика для подсчёта эковклада пользователя: сохранённого объёма воды, предотвращённого объёма выброса CO2 и сэкономленной электроэнергии.

Числа, отображаемые на счётчиках приходят с бэкенда. Обработку этих значений выполняет микрофронтенд:
в его задачи, например, входит подстановка единиц измерений: замена 1000 литров на 1 метр кубический и т.д.

Программа test-cases.py подменяет ответ от сервера со значениями счетчиков на ответ, сохраненный в папке "responses". В новом ответе значения счетчиков CO2, энергии и воды (блок на странице: "Ваш экологический вклад") заменены на тестовые данные, выбранные по технике тест-дизайна "Граничные значения". 

Программа содержит 9 тест-кейсов: 

* test1. Отображение счетчиков при значении "1000" в ответе от сервера.
* test2. Отображение счетчиков при значении "1001" в ответе от сервера.
* test3. Отображение счетчиков при значении "999" в ответе от сервера.
* test4. Отображение счетчиков при значении "1000000" в ответе от сервера.
* test5. Отображение счетчиков при значении "1000001" в ответе от сервера.
* test6. Отображение счетчиков при значении "999999" в ответе от сервера.
* test7. Отображение счетчиков при значении "1000000000" в ответе от сервера.
* test8. Отображение счетчиков при значении "1000000001" в ответе от сервера.
* test9. Отображение счетчиков при значении "999999999" в ответе от сервера.

Описание тест-кейсов находится в файле "TESTCASES.md".

В результате выполнения каждого тест-кейса программа создает скриншот блока со счетчиками. На скриншоте видны тестовые значения и результат их обработки микрофронтендом, что позволяет оценить соответствие реального поведения программы ожидаемому результату. 

## Техническое описание программы

Программа разработана на языке программирования Python.

Используемый фреймворк для тестирования кода: Pytest. 

Автоматизация тестирования выполнена с помощью инструмента Playwright.

Чтобы открыть программу, необходимо в проекте "Avito_Test_for_QA" открыть файл "test_cases.py".

## Как работать с программой

1. Открыть файл "test-cases.py". 
2. В терминале выполнить команду: `pytest --headed`
3. Ожидать завершения выполнения всех 9 тестов.
4. В терминале появится сообщение, что 9 тестов пройдены успешно (passed).
5. Перейти в папку "output" для просмотра скриншотов. Название скриншота состоит из номера тест-кейса, даты (гггг.мм.дд) и времени (чч.мм.сс) создания скриншота. 