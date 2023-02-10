# ������ ��� ������������ ��������

������ ������ ��������� ��������� ��������� � ����������� ��������� ��� ����������. ������������ ������������ ��������� ������ �������, �������� ��������� � ���������� ���������� ������� �� ��������.

## ����������

���������� ������ ������ ����� �� ������� �������� ����� ������������ ��������. �������� ��� ��� [�����](https://github.com/devmanorg/e-diary/tree/master).

��� ������� � ��� ��� ������ ���� ���������� Python 3.

- �������� ���, �������� ��������� ������
- ���������� ����������� �������� `pip install -r requirements.txt`
- �������� �� �������� python3 `manage.py migrate`
- ��������� ������ �������� `python3 manage.py runserver`

����� ����� ���������� �� ������ [127.0.0.1:8000](http://127.0.0.1:8000), �� ������� ������� ��������.

��� ����������� ������ ��� ���������� ������� [����� � ����� ������](https://dvmn.org/filer/canonical/1562234129/166/), � ����� ������� .env ���� � ������� ��� ���� � ���� ������ � ����:

```
DATABASE_NAME=schoolbase.sqlite3
```

����� ����� �� ����� ����� �������� ������, �������, ������ � �.�.


## ������ �������

������, ����� ���� ����� � ���������� �������, �������� ���� 'scripts.py' � ��������� ��� � �����, ��� ��������� ��� �����. �����:

- �������� ������ ���� � ��������� �������
- ��������� ������� `python3 manage.py shell`
- ������������ ����������� ������, ����������� � ��� ���� ��������� �������:

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

## ����������

� ������� ������� ���� ��������� ��������� ����������:

#### fix_marks

������ ������ � ������ ���������� ������� �� �������. ��� ������� �������:

```
fix_marks('��� �������')
```

#### remove_chastisements

������� ��� ��������� �� �������� ���������� �������. ��� ������� �������:

```
remove_chastisements('��� �������')
```

#### create_commendation

������� ���������� ����� �� ������� ��� ���������� ������� �� ���������� ��������. ��� ������� �������:

```
create_commendation('��� �������', '����������� �������')
```

## ���� �������

��� ������� � ������� ����� � ��� ���� � ����� �� Python � ���-���������� �� ����� [Devman](https://dvmn.org).