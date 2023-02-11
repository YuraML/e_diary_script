from random import choice
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist


commendations = ['Хвалю!', 'Молодец!', 'Отлично!', 'Великолепно!', 'Прекрасно!', 'Очень хороший ответ!', 'Талантливо!',
                 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Так держать!', 'Здорово!']


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        raise MultipleObjectsReturned('Найдено несколько учеников, уточните ФИО')
    except Schoolkid.DoesNotExist:
        raise ObjectDoesNotExist('Не найдено. Уточните ФИО ученика.')


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid_name, subject):
    schoolkid = get_schoolkid(schoolkid_name)
    lesson = Lesson.objects.filter(subject__title__contains=subject, year_of_study=schoolkid.year_of_study,
                                   group_letter=schoolkid.group_letter).order_by('?').first()
    if not lesson:
        return 'Уточните название предмета.'
    else:
        Commendation.objects.create(
            text=choice(commendations),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
