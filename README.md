# Загрузка и рассылка фото NASA и SPACEX

Данный скрипт позволяет загружать фотографии с сервисов [NASA EPIC](https://api.nasa.gov/#epic) и [NASA APOD](https://api.nasa.gov/#apod)
и фотографии [последнего запуска SPACEX](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1),
а затем постить их в свой телеграмм канал.

### Как установить

Для начала работы необходимо:
- Зарегистрироваться на [сайте NASA](https://api.nasa.gov/) и сгенерировать токен.
- Затем создать бота в TG [(Как создать канал, бота и получить токен.)](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
- Создать канал в TG и добавить бота в него

Далее, в папке со скриптом необходимо создать файл `.env` и записать в него настройки в виде:
```
NASA_API_KEY=Ваш токен NASA
TG_BOT_TOKEN=токен Вашего бота в телеграмм
TG_HAT_ID=@название Вашего канала
SPACEX_LAUNCH_ID=ваш айди
```

[Python3](https://www.python.org/downloads/) должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как использовать
- Для загрузки изображений NASA используйте команду
```
 python fetch_nasa_apod.py
```
- Для загрузки изображений SPACEX используйте команду 
```
python fetch_spacex_images.py
```
- Для постинга изображений в телеграмм используйте команд
```
python main.py
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).