from django.shortcuts import render
from django.views import View
from test_interview.models import Question


class InterviewView(View):
    def get(self, request):
        # Получаем рандомный вопрос из базы
        question = Question.objects.order_by('?').first()
        return render(
            request, 'test_interview/question.html', {'question': question}
            )

    def post(self, request):
        # Получаем ответ пользователя
        submitted_answer = request.POST.get('answer')

        # Получаем выданный вопрос для сравнения ответов
        question_id = request.POST.get('question_id')
        question = Question.objects.get(id=question_id)

        # Сравниваем ответ с верным
        if submitted_answer.lower() == question.answer.lower():
            result = 'Верно!'
        else:
            result = 'Неправильно!'

        next_question = Question.objects.order_by('?').first()

        return render(
            request, 'test_interview/question.html', {
                'question': next_question, 'result': result
                }
            )
