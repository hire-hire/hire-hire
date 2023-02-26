from django.views.generic import TemplateView


class ContributorsView(TemplateView):
    template_name = 'contributors/contributors_list.html'
