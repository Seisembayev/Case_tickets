## Chocotravel&Aviata "Возврат билетов"
#### MethodPro 2018. Команда №18. NonStop

> #### Краткое описание
> Разработка модуля для определения суммы возврата. При бронировании авиабилета мы получаем информацию об условиях возврата и обмена авиабилета. Данный текст не структурированный, и может отличаться в зависимости от авиакомпании. В рамках данного проекта необходимо собрать информацию по штрафам и определить статус билета и посчитать для клиента сумму возврата по условиям авиакомпании.
> * Мы предлагаем решение для data science:
>   + Мы спарсим данные авиабилета и определяем какой у перелета статус.
>   + Мы спарсим текст правил тарифа, и извлекаем нужную информацию для определения суммы для возврата.<br/>
> (В основном, наш проект связан с парсингом.)

### Как работает наш продукт?
Что делает наш продукт особенным, так это его скорость и точность. Наша программа принимает два файла с данными о брони и правил тарифов. Так как каждая компания имеет свой шаблон правил, при считывании правил программа использует поиск, что бы получить необходимые данные о штрафах. После считывания правил, непосредственное высчитывается сумма возврата и на выход выводиться файл с основной информацией о всем процессе.

### Полное описание проекта
* **Класс main.py.** Это наш самый главный класс. Здесь мы получаем 2 json файла(booking and fareRules) и делаем первый шаг для вычисления.
  + Функция **get_json_data()** считывает данные полученные через API.
  + Функция **write_data()** конвертирует вычисленные данные в json файл.
  + Функция **main()** полученные данные из функции get_json_data, отправляются в класс parsing.py.
* **Класс parsing.py.** Здесь мы парсим данные из json файла. То есть мы получаем данные о билете и правила о тарифе.
  + Функция **__get_codes().** Получает Operating Airline Code компании.
  + Функция **__get_total_fares().**
  + Функция **__get_taxes().**
  + Функция **__get_base_fares().**
  + Функция **__get_currencies().**
  + Функция **__get_dates().**
  + Функция **__get_full_names().**
  + Функция **__get_rules().**
  + Функция **__get_data().** Эта функция создает массив и заполняет данные, полученные с помощью указанных выше функциями.
  + Функция **__get_cities().** получаем данные о городе отъезда и прибытия пассажира.
