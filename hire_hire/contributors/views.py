from django.views.generic import ListView

from contributors.models.contributor import Contributor


class ContributorsView(ListView):
    template_name = 'contributors/contributors_list.html'
    queryset = Contributor.objects.get_contributors_with_contacts_and_roles()
    context_object_name = 'contributors'
