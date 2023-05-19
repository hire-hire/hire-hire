from django.db import models


class ContributorManager(models.Manager):
    def get_contributors_with_contacts_and_roles(self):
        return (
            self.get_queryset()
            .select_related('role')
            .prefetch_related('contacts')
            .order_by('role')
        )


class ContributorContactManager(models.Manager):
    def get_contributor_contacts_count(self, contributor):
        return self.get_queryset().filter(contributor=contributor).count()
