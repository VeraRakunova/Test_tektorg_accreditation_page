Проект реализует тестирование заполнения полей сайта ТЭК-ТОРГ страницы "Аккредитация нового пользователя на ЭТП" валидными значеними. 

Если после заполнения сгенерированными данными доступна кнопка "Подписать и отправить заявку...", то тест считается успешным.
Сгенерированные данные по каждому тесту в ходе выполнения записываются в файл "x.log"

Установка:

После скачивания архива проекта и его распаковки, установить окружение из файла requirements.txt.

Для корректной работы необходим Chrome и соответсвующий ему драйвер браузера. Скачать драйвера можно здесь: https://selenium-python.readthedocs.io/installation.html#drivers

Запуск тестов осуществляется из рабочей папки командой python3 -m pytest 
