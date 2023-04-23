from django.db import models
from django.utils import timezone


class AddQuestionManager(models.Manager):
    """Возвращает количество предложенных вопросов за 24 часа."""
    def get_24_hours_added_question(self, **kwargs):  # user, user_cookie):
        ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
        if kwargs.get('author').is_authenticated:  # user.is_authenticated:
            return self.get_queryset().filter(
                pub_date__gte=ago_24_hours,
                # **kwargs,
                author=kwargs.get('author'),  # user,
            ).count()
        return self.get_queryset().filter(
            pub_date__gte=ago_24_hours,
            # **kwargs,
            user_cookie=kwargs.get('user_cookie'),  # user_cookie,
        ).count()
        # return 5

# class AddQuestionManager(models.Manager):
#     """Возвращает количество предложенных вопросов за 24 часа."""
#     def get_24_hours_added_question(self, user, user_cookie):
#         ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
#         if user.is_authenticated:
#             return self.get_queryset().filter(
#                 pub_date__gte=ago_24_hours,
#                 author=user,
#             ).count()
#         return self.get_queryset().filter(
#             pub_date__gte=ago_24_hours,
#             user_cookie=user_cookie,
#         ).count()
