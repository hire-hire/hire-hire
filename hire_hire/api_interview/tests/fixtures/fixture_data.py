import pytest

from interview.models import Category, Language, Question


@pytest.fixture
def category_1():
    return Category.objects.create(title='Программирование')


@pytest.fixture
def category_2():
    return Category.objects.create(title='Тестирование')


@pytest.fixture
def language_1(category_1):
    return Language.objects.create(title='Python', category=category_1)


@pytest.fixture
def language_2(category_1):
    return Language.objects.create(title='Javascript', category=category_1)


@pytest.fixture
def question_1(language_1):
    return Question.objects.create(
        language=language_1,
        text='Какое слово всегда пишется неправильно?',
        answer='Это слово «неправильно». '
               'Оно всегда так и пишется – «неправильно». '
               'Эффект этой задачи-шутки заключается в том, '
               'что в ней слово «неправильно» употребляется '
               'в двух разных смыслах.',
    )


@pytest.fixture
def question_2(language_1):
    return Question.objects.create(
        language=language_1,
        text='Сколько месяцев в году имеют 28 дней?',
        answer='Все месяцы',
    )


@pytest.fixture
def question_3(language_1):
    return Question.objects.create(
        language=language_1,
        text='С какой скоростью должна двигаться собака '
             '(в возможных для неё пределах), '
             'чтобы не слышать звона сковородки, '
             'привязанной к ее хвосту?',
        answer='С нулевой. Собаке нужно стоять на месте',
    )


@pytest.fixture
def question_4(language_1):
    return Question.objects.create(
        language=language_1,
        text='Собака была привязана к десятиметровой веревке, '
             'а прошла по прямой двести метров. '
             'Как ей это удалось?',
        answer='Её веревка не была ни к чему не привязана',
    )


@pytest.fixture
def question_5(language_1):
    return Question.objects.create(
        language=language_1,
        text='Как спрыгнуть с десятиметровой лестницы и не ушибиться?',
        answer='Нужно прыгать с нижней ступени',
    )


@pytest.fixture
def question_6(language_1):
    return Question.objects.create(
        language=language_1,
        text='Что можно видеть с закрытыми глазами?',
        answer='Сны',
    )


@pytest.fixture
def question_7(language_1):
    return Question.objects.create(
        language=language_1,
        text='Что в огне не горит и в воде не тонет?',
        answer='Лёд',
    )


@pytest.fixture
def question_8(language_1):
    return Question.objects.create(
        language=language_1,
        text='Кого австралийцы называют морской осой?',
        answer='Медузу',
    )


@pytest.fixture
def question_9(language_1):
    return Question.objects.create(
        language=language_1,
        text='Что нужно делать, когда видишь зелёного человечка?',
        answer='Переходить улицу (это рисунок на зелёном сигнале светофора)',
    )


@pytest.fixture
def question_10(language_1):
    return Question.objects.create(
        language=language_1,
        text='Москву раньше называли белокаменной. '
             'А какой город называли чёрным?',
        answer='Чернигов',
    )


@pytest.fixture
def question_11(language_1):
    return Question.objects.create(
        language=language_1,
        text='Жители средневековой Европы иногда '
             'привязывали к подошвам деревянные чурки. '
             'С какой целью они это делали?',
        answer='Для защиты от грязи, т.к. канализации '
               'не было и помои выливали прямо на улицу',
    )


@pytest.fixture
def question_12(language_1):
    return Question.objects.create(
        language=language_1,
        text='В каком процессе вода заменила солнце, '
             'через 600 лет ее заменил песок, '
             'а еще через 1100 лет всех их '
             'заменил механизм?',
        answer='В процессе измерения времени – часах',
    )


@pytest.fixture
def question_13(language_1):
    return Question.objects.create(
        language=language_1,
        text='В прежние времена амбары '
             'строили на отшибе, подальше '
             'от жилищ. С какой целью?',
        answer='Чтобы пожар не уничтожил запасы продовольствия',
    )


@pytest.fixture
def question_14(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 14',
        answer='ответ на вопрос 14',
    )


@pytest.fixture
def question_15(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 15',
        answer='ответ на вопрос 15',
    )


@pytest.fixture
def question_16(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 16',
        answer='ответ на вопрос 16',
    )


@pytest.fixture
def question_17(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 17',
        answer='ответ на вопрос 17',
    )


@pytest.fixture
def question_18(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 18',
        answer='ответ на вопрос 18',
    )


@pytest.fixture
def question_19(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 19',
        answer='ответ на вопрос 19',
    )


@pytest.fixture
def question_20(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 20',
        answer='ответ на вопрос 20',
    )


@pytest.fixture
def question_21(language_1):
    return Question.objects.create(
        language=language_1,
        text='вопрос 21',
        answer='ответ на вопрос 21',
    )
