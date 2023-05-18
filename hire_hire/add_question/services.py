def get_count_questions_text(count_questions):
    last_digit = count_questions % 10
    if 10 <= count_questions <= 20 or last_digit == 0 or last_digit >= 5:
        return f'о {count_questions} вопросов'
    elif last_digit == 1:
        return f' {count_questions} вопрос'
    return f'о {count_questions} вопроса'


def get_user_data_dict(user, user_cookie_id):
    return (
        dict(author=user)
        if user.is_authenticated
        else dict(user_cookie_id=user_cookie_id)
    )
