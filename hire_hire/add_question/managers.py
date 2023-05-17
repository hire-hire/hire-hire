from django.db import models
from django.utils import timezone

from add_question.services import user_data_dict


class AddQuestionManager(models.Manager):
    def get_24_hours_added_question_count(self, user, user_cookie_id):
        ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
        return (
            self.get_queryset()
            .filter(
                pub_date__gte=ago_24_hours,
                **user_data_dict(user, user_cookie_id),
            )
            .count()
        )
