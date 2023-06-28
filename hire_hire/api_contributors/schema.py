from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
)

from hire_hire.schema_settings import not_found


class ContributorsView(OpenApiViewExtension):
    target_class = 'api_contributors.views.ContributorsListViewSet'

    def view_replacement(self):
        from api_contributors.serializers import ContributorSerializer

        class Extended(self.target_class):

            @extend_schema(
                description='Список участников команды с ролями',
                tags=['Contributors'],
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
                                            'contact': 'http://ya.ru',
                                        }
                                    ]
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                },
            )
            def list(self):
                pass

            @extend_schema(
                description='Информация по конкретному интервью',
                tags=['Contributors'],
                request=ContributorSerializer,
                responses={
                    200: OpenApiResponse(response=ContributorSerializer),
                    404: OpenApiResponse(
                        response=ContributorSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def retrieve(self):
                pass

        return Extended
