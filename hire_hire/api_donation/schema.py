from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
)


class DonationSchemaView(OpenApiViewExtension):
    target_class = 'api_donation.views.DonationView'

    def view_replacement(self):
        from api_donation.serializers import (
            AcceptPayment, PriceSerializer,
        )

        class Extended(self.target_class):

            @extend_schema(
                description='Список всех платежей',
                tags=['Donation'],
                request=PriceSerializer,
                responses={
                    200: OpenApiResponse(
                        response=PriceSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает заведенные'
                                            ' в админке платежи',
                                value={
                                    'id': 1,
                                    'currency': 'RUB',
                                    'value': 100,
                                },
                            ),
                        ],
                    ),
                },
            )
            def get(self):
                pass

            @extend_schema(
                description='Запрос на создание платежа',
                tags=['Donation'],
                request=AcceptPayment,
                responses={
                    200: OpenApiResponse(
                        response=PriceSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает ссылку на платежку',
                                value={
                                    'id': 'https://yoomoney.ru/'
                                          'checkout/payments/v2/'
                                          'contract?orderId=',
                                },
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=AcceptPayment,
                        examples=[
                            OpenApiExample(
                                '401',
                                summary='Не удалось авторизоваться'
                                        ' в платежном сервисе',
                                description='Возвращает ошибку '
                                            'аутентификации в '
                                            'платежном сервисе',
                                value={
                                    'detail': 'Ошибка аутентификации'
                                              ' в платежном сервисе',
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                },
            )
            def post(self):
                pass

        return Extended
