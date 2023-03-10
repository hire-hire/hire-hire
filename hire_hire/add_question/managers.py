from django.db import models
from django.utils import timezone


class AddQuestionManager(models.Manager):
    """Возвращает количество предложенных вопросов за 24 часа."""
    def get_24_hours_added_question(self, request):
        ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
        current_ip_address = request.META.get('REMOTE_ADDR')
        return self.get_queryset().filter(
            pub_date__gte=ago_24_hours,
            ip_address=current_ip_address).count()
