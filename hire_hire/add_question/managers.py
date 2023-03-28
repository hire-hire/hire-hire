from django.db import models
from django.utils import timezone


class AddQuestionManager(models.Manager):
    """Возвращает количество предложенных вопросов за 24 часа."""
    def get_24_hours_added_question(self, request):
        ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
        current_user_cookie = request.COOKIES.get('user_cookie')

        if request.user.is_authenticated:
            return self.get_queryset().filter(
                pub_date__gte=ago_24_hours,
                author=request.user,
            ).count()

        return self.get_queryset().filter(
            pub_date__gte=ago_24_hours,
            user_cookie=current_user_cookie,
        ).count()
