# Telegram-timetable-bot
Данный проект был сделан для удобного отображения расписаний на различные дни, для различных классов.
Текущий функционал бота позволяет: 
Узнать текущую погоду в Омске

![image](https://user-images.githubusercontent.com/90842082/229172638-18297b93-d738-4275-9ed7-58e8ee176971.png)
![image](https://user-images.githubusercontent.com/90842082/229172691-380df32f-da02-4a86-a92c-0b840013b1d6.png)

Расписание для 4-х классов:

![image](https://user-images.githubusercontent.com/90842082/229172741-aded8061-f00c-4e03-ad71-eb71befbabbb.png)
![image](https://user-images.githubusercontent.com/90842082/229172763-b8f21f5f-db55-4511-8f36-ca9d848d5ee1.png)
![image](https://user-images.githubusercontent.com/90842082/229172793-5bcea993-2e4b-4a3c-b64f-cc486b8fe2c0.png)

И текущее время:

![image](https://user-images.githubusercontent.com/90842082/229172917-1b041f00-fac5-4a86-8948-e7a58b4e1d41.png)

При разработке данного проекта были использованы следующие технологии:
Язык программирования Python.
Библиотеки: telebot,requests,datetime.
Библиотека telebot позволяет нам взаимодействоать с API телеграмма.
Библиотека requests позволяет нам делать HTTP-запросы в проекте используется для взаимодействия с сайтом wttr.in, который позволяет нам получить погоду.
Библиотека datetime позволяет нам получать точное время.
Для установки проекта необходимо получить Токен у официального бота https://t.me/BotFather. Токен необходим для взаимодействия с API телеграма.
Также необходимо установить соответствующие бибилиотеки, это можно сделать командами:
pip install pyTelegramBotAPI 
pip install requests
pip install datetime
