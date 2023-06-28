from django.db import models
from django.utils import timezone


class AddQuestionManager(models.Manager):
    def get_24_hours_added_question_count(self, user, user_cookie_id):
        if user.is_authenticated:
            return self.get_24_hours_added_question_count_by_user(user)
        return self.get_24_hours_added_question_count_by_user_cookie_id(
            user_cookie_id,
        )

    def get_24_hours_added_question_count_by_user(self, user):
        return self._get_24_hours_added_question().filter(author=user).count()

    def get_24_hours_added_question_count_by_user_cookie_id(
        self,
        user_cookie_id,
    ):
        return (
            self._get_24_hours_added_question()
            .filter(user_cookie_id=user_cookie_id)
            .count()
        )

    def _get_24_hours_added_question(self):
        ago_24_hours = timezone.now() - timezone.timedelta(hours=24)
        return self.get_queryset().filter(pub_date__gte=ago_24_hours)
