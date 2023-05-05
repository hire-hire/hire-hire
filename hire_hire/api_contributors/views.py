from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import viewsets

from api_contributors.serializers import ContributorSerializer
from contributors.models import Contributor
from hire_hire.schema import not_found


@extend_schema_view(
    list=extend_schema(
        tags=['Contributors'],
        description='Список участников команды с ролями',
        request=ContributorSerializer,
        responses={
            200: OpenApiResponse(
                response=ContributorSerializer,
                examples=[
                    OpenApiExample(
                        'valid_result',
                        summary='Валидный результат',
                        description='Возвращает ошибку '
                                    'о несоответствии кол-ва '
                                    'вопросов допустимому',
                        value={
                                'first_name': 'кукла',
                                'last_name': 'колдуна',
                                'middle_name': 'кишовна',
                                'photo': 'урл какой-то фотки',
                                'role': 'мужик',
                                'contacts': [
                                    {
                                        'social_network': 'сеть1',
                                        'contact': 'http://ya.ru'
                                    }
                                ]
                            },
                        response_only=False,
                    ),
                ],
            ),
        },
    ),
    retrieve=extend_schema(
        tags=['Contributors'],
        description='Информация по конкретному интервью',
        request=ContributorSerializer,
        responses={
            200: OpenApiResponse(response=ContributorSerializer),
            404: OpenApiResponse(
                response=ContributorSerializer,
                examples=[not_found],
            ),
        },
    ),
)
class ContributorsListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.get_contributors_with_contacts_and_roles()
