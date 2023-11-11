import pytest

from interview.models import Category, Language, Question, QuestionAnswer

QUESTIONS = {
    'вопрос1': 'ответ на вопрос 1',
    'вопрос2': 'ответ на вопрос 2',
    'вопрос3': 'ответ на вопрос 3',
    'вопрос4': 'ответ на вопрос 4',
    'вопрос5': 'ответ на вопрос 5',
    'вопрос6': 'ответ на вопрос 6',
    'вопрос7': 'ответ на вопрос 7',
    'вопрос8': 'ответ на вопрос 8',
    'вопрос9': 'ответ на вопрос 9',
    'вопрос10': 'ответ на вопрос 10',
    'вопрос11': 'ответ на вопрос 11',
    'вопрос12': 'ответ на вопрос 12',
    'вопрос13': 'ответ на вопрос 13',
    'вопрос14': 'ответ на вопрос 14',
    'вопрос15': 'ответ на вопрос 15',
    'вопрос16': 'ответ на вопрос 16',
    'вопрос17': 'ответ на вопрос 17',
    'вопрос18': 'ответ на вопрос 18',
    'вопрос19': 'ответ на вопрос 19',
    'вопрос20': 'ответ на вопрос 20',
    'вопрос21': 'ответ на вопрос 21',

}


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
def all_questions(user, language_1):
    questions = []
    answers = []
    for text, ans in QUESTIONS.items():
        question = Question(language=language_1, author=user, text=text)
        questions.append(question)
        answers.append(
            QuestionAnswer(text=ans, is_correct=True, question=question)
        )
        answers.extend([
            QuestionAnswer(text='bad', is_correct=False, question=question)
            for _ in range(3)
        ])

    Question.objects.bulk_create(questions)
    QuestionAnswer.objects.bulk_create(answers)
    return Question.objects.all()
