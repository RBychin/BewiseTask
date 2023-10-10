import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import QuestionSerializer
from core.models import Question


def get_response(count: int | None = 1) -> list | bool:
    try:
        return requests.get(
            url=settings.API_URL,
            params=[('count', count)]
        ).json()
    except:
        return False


class QuestionView(APIView):
    """Представление обрабатывающее POST запросы и в случае успеха -
    отдающее последний сохраненный в БД вопрос (только текст вопроса).
    Реализована валидация переданного квери параметра.
    """

    def post(self, request) -> Response:
        if ('questions_num' in request.data
                and isinstance(request.data.get('questions_num'), int)
                and 101 > request.data.get('questions_num') > 0):

            count = request.data['questions_num']
            questions = []
            response = get_response(count)
            if not response:
                return Response({'detail': 'Ошибка доступа к серверу API'},
                                status=418)
            for question in response:
                while (Question.objects.filter(id=question['id']).exists()
                       or question['id'] in questions):
                    question = get_response()[0]
                data = {
                    'id': question.get('id'),
                    'question_text': question.get('question'),
                    'answer_text': question.get('answer'),
                    'create_date': question.get('created_at'),
                }
                questions.append(Question(**data))
            last_question = Question.objects.last()
            Question.objects.bulk_create(questions)
            return Response(QuestionSerializer(last_question).data)
        return Response(
            {'questions_num': 'Должно содержать значение от 1 до 100'}
        )
