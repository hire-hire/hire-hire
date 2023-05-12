import pytest


@pytest.fixture
def category_1():
    from interview.models import Category
    return Category.objects.create(title='Программирование')


@pytest.fixture
def category_2():
    from interview.models import Category
    return Category.objects.create(title='Тестирование')


@pytest.fixture
def language_1():
    from interview.models import Language
    return Language.objects.create(title='Python', category=category_1)


@pytest.fixture
def language_2():
    from interview.models import Language
    return Language.objects.create(title='Javascript', category=category_1)


@pytest.fixture
def question_1():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Какое слово всегда пишется неправильно?',
        answer='Это слово «неправильно». '
               'Оно всегда так и пишется – «неправильно». '
               'Эффект этой задачи-шутки заключается в том, '
               'что в ней слово «неправильно» употребляется '
               'в двух разных смыслах.'
    )


@pytest.fixture
def question_2():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Сколько месяцев в году имеют 28 дней?',
        answer='Все месяцы'
    )


@pytest.fixture
def question_3():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='С какой скоростью должна двигаться собака '
             '(в возможных для неё пределах), '
             'чтобы не слышать звона сковородки, '
             'привязанной к ее хвосту?',
        answer='С нулевой. Собаке нужно стоять на месте'
    )


@pytest.fixture
def question_4():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Собака была привязана к десятиметровой веревке, '
             'а прошла по прямой двести метров. '
             'Как ей это удалось?',
        answer='Её веревка не была ни к чему не привязана'
    )


@pytest.fixture
def question_5():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Как спрыгнуть с десятиметровой лестницы и не ушибиться?',
        answer='Нужно прыгать с нижней ступени'
    )


@pytest.fixture
def question_6():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Что можно видеть с закрытыми глазами?',
        answer='Сны'
    )


@pytest.fixture
def question_7():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Что в огне не горит и в воде не тонет?',
        answer='Лёд'
    )


@pytest.fixture
def question_8():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Кого австралийцы называют морской осой?',
        answer='Медузу'
    )


@pytest.fixture
def question_9():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Что нужно делать, когда видишь зелёного человечка?',
        answer='Переходить улицу (это рисунок на зелёном сигнале светофора)'
    )


@pytest.fixture
def question_10():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Москву раньше называли белокаменной. '
             'А какой город называли чёрным?',
        answer='Чернигов'
    )


@pytest.fixture
def question_11():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='Жители средневековой Европы иногда '
             'привязывали к подошвам деревянные чурки. '
             'С какой целью они это делали?',
        answer='Для защиты от грязи, т.к. канализации '
               'не было и помои выливали прямо на улицу'
    )


@pytest.fixture
def question_12():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='В каком процессе вода заменила солнце, '
             'через 600 лет ее заменил песок, '
             'а еще через 1100 лет всех их '
             'заменил механизм?',
        answer='В процессе измерения времени – часах'
    )


@pytest.fixture
def question_13():
    from interview.models import Question
    return Question.objects.create(
        language=language_1,
        text='В прежние времена амбары '
             'строили на отшибе, подальше '
             'от жилищ. С какой целью?',
        answer='Чтобы пожар не уничтожил запасы продовольствия'
    )
