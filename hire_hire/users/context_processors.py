from users.forms import CreationForm


def login_everywhere(request):
    form = CreationForm()
    return {'login_form': form}
