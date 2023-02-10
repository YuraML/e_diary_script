# Скрипт для электронного дневника

Данный скрипт позволяет проводить махинации с электронным дневником для школьников. Пользователю предлагается изменение оценок ученика, удаление замечаний и добавление похвальных отзывов от учителей.

## Подготовка

Опробывать данный скрипт можно на примере готового сайта электронного дневника. Скачайте его код [здесь](https://github.com/devmanorg/e-diary/tree/master).

Для запуска у вас уже должен быть установлен Python 3.

- Скачайте код, откройте командную строку
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте БД командой python3 `manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

Для отображения данных вам необходимо скачать [архив с базой данных](https://dvmn.org/filer/canonical/1562234129/166/), а также создать .env файл и указать там путь к базе данных в виде:

```
DATABASE_NAME=schoolbase.sqlite3
```

После этого на сайте будут показаны классы, ученики, оценки и т.д.


## Запуск скрипта

Теперь, когда сайт готов к применению скрипта, скачайте файл 'scripts.py' и поместите его в папку, где находится код сайта. Затем:

- Откройте другое окно с командной строкой
- Запустите команду `python3 manage.py shell`
- Импортируйте необходимые данные, скопипастив в это окно следующие команды:

```
from random import choice
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from scripts import get_schoolkid
from scripts import fix_marks
from scripts import remove_chastisements
from scripts import create_commendation
```

## Функционал

У данного скрипта есть несколько вариантов применения:

#### fix_marks

Меняет двойки и тройки выбранного ученика на пятерки. Для запуска введите:

```
fix_marks('ФИО ученика')
```

#### remove_chastisements

Удаляет все замечания от учителей выбранного ученика. Для запуска введите:

```
remove_chastisements('ФИО ученика')
```

#### create_commendation

Создает похвальный отзыв от учителя для выбранного ученика по выбранному предмету. Для запуска введите:

```
create_commendation('ФИО ученика', 'Необходимый предмет')
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).