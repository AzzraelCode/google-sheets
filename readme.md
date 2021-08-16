# Код для видео на Azzrael Code о работе с Google Sheets API

Для каждого видео своя ветка - просто переключайся чтобы посмотреть код 
соотв. видео.

В первом видео я покажу
[Как читать Google Sheet с помощью Сервисного Аккаунта](https://youtu.be/hMl-0yiBMNs).

Подробно о типах ключей в Google API (как их создавать и в чем разница) 
я рассказывал в видео:
[Как создать проект в Google Cloud Platform](https://www.youtube.com/watch?v=WpB42nS1uWE)

### Полезные ссылки

- https://console.cloud.google.com/
- https://github.com/googleapis/google-api-python-client#installation

- https://developers.google.com/sheets/api/guides/concepts
- https://developers.google.com/sheets/api/quickstart/python
- https://developers.google.com/sheets/api/guides/authorizing

### Установка
См прошлые видео в [Плейлисте Google API](https://www.youtube.com/watch?v=PjKMDtLuKPU&list=PLWVnIRD69wY4ane3amNJSFQfls1inhaub)
Но в целом, скорее всего, достаточно: 
`pip install -r req.txt`
Потом создаю Проект в Google Cloud Platform и получи Сервисный Аккаунт
Скачай в папку `creds` файлик json с секретками и назови его `sacc1.json`
Также потом пригодится api_kei в `cred/__init__.py` (см. видео)
Затем расшарь свою таблицу в Google Sheets для емейла созданноего Сервисного Аккаунта с правами Редактор