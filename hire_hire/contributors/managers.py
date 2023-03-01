from django.db import models


class ContributorManager(models.Manager):
    def get_contributors_with_contacts_and_roles(self):
        """Если тут делать Contributor.role.field.name то будет цирк импорт."""
        return (
            self.get_queryset()
            .select_related('role')
            .prefetch_related('contacts')
            .order_by('role')
        )
