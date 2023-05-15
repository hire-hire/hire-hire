from django.db import models
from django.utils import timezone


class AddQuestionManager(models.Manager):
    def get_24_hours_added_question_count(self, user, user_cookie_id):
        ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
        user_data_dict = (
            dict(author=user)
            if user.is_authenticated
            else dict(user_cookie_id=user_cookie_id)
        )
        return (
            self.get_queryset()
            .filter(
                pub_date__gte=ago_24_hours,
                **user_data_dict,
            )
            .count()
        )
