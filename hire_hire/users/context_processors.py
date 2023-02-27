from users.forms import CreationForm, LoginForm


def get_login_and_signup_forms(request):
    return {'signup_form': CreationForm(), 'login_form': LoginForm()}
