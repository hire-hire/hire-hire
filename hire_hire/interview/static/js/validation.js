const authForm = document.querySelector('.form_type_auth');
const registerForm = document.querySelector('.form_type_register');
const openAuthFormButton = document.querySelector('.header__link_type_blue');
const openRegisterFormButton = document.querySelector('.form__button_type_register');
const registerSubmitButton = registerForm.querySelector('.form__button');
const agreementElement = registerForm.querySelector('.form__checkbox-container');
const authLoginInput = authForm.querySelector('#email');
const headerItems = document.querySelector('.header__items');
const headerItemArr = headerItems.querySelectorAll('.header__item');

headerItems.style.gap = '48px';
headerItemArr.forEach(headerItem => headerItem.style.marginRight = 0);

authLoginInput.setAttribute('placeholder', 'Логин');

agreementElement.innerHTML = '';

registerSubmitButton.textContent = "Зарегистрироваться";

document.querySelectorAll('.form__input-error').forEach((element) => {
    element.style.minHeight = `35px`;
    element.style.marginBottom = `4px`;
});

const checkFormValidity = (form => form.checkValidity());

const showError = ((input, form) => {
    const errorItem = form.querySelector(`.${input.name}-error`);
    const emailInput = form.querySelector('#email');

    if ((input.name === 'password') && (input.value === emailInput.value)) {
        errorItem.textContent = 'Логин и пароль не должны совпадать';
        errorItem.classList.add('form__input-error_type_visible');
        input.classList.add('form__input_type_error');
    } else {
        errorItem.textContent = input.validationMessage;
        errorItem.classList.add('form__input-error_type_visible');
        input.classList.add('form__input_type_error');
    }
    ;
});

const hideError = ((input, form) => {
    const errorItem = form.querySelector(`.${input.name}-error`);
    errorItem.textContent = '';
    errorItem.classList.remove('form__input-error_type_visible');
    input.classList.remove('form__input_type_error');
});

const toggleButtonState = ((input) => {
    const form = input.closest('.form');
    const isFormValid = checkFormValidity(form);
    const formButton = form.querySelector('.form__button');
    if (isFormValid) {
        formButton.style.opacity = 1;
        formButton.disabled = false;
    } else {
        formButton.style.opacity = 0.4;
        formButton.disabled = true;
    }
    ;
});

const resetValidation = ((form) => {
    toggleButtonState(form);
    const inputsArr = form.querySelectorAll('.form__input');
    inputsArr.forEach(input => hideError(input, form));
});

const checkInputValidity = ((input) => {
    let isInputValid = input.validity.valid;
    const closestForm = input.closest('.form');
    const emailInput = closestForm.querySelector('#email');

    if (input.name === 'password' && input.value === emailInput.value) {
        isInputValid = false;
    }
    ;

    if (isInputValid) {
        hideError(input, closestForm);
    } else {
        showError(input, closestForm);
    }
    ;
});

const setValidation = ((input) => {
    toggleButtonState(input);
    checkInputValidity(input);
});

const allInputsArr = document.querySelectorAll('.form__input');

allInputsArr.forEach((input) => {
    if (input.type === 'password') {
        input.setAttribute('maxlength', '128');
        input.setAttribute('minlength', '8');
        input.setAttribute('pattern', '\(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z]{8,}');
    }
    ;
    if (input.type === 'email') {
        input.setAttribute('type', 'text');
        input.setAttribute('maxlength', '150');
        input.setAttribute('minlength', '2');
    }
});

const inputContainerArr = registerForm.querySelectorAll('.form__input-container');
inputContainerArr.forEach((inputContainer) => {
    const input = inputContainer.querySelector('.form__input');
    const hintElement = inputContainer.querySelector('.form__label-hint');
    if (input.name === 'email') {
        hintElement.textContent = 'Длина логина должна быть от 2 до 150 символов. Логин и пароль не должны совпадать';
    } else {
        hintElement.textContent = 'Длина пароля должна быть от 8 до 128 символов. В пароле должна быть хотя бы одна латинская буква. Пароль не должен совпадать с логином';
    }
})


openAuthFormButton.addEventListener('click', () => resetValidation(authForm));
openRegisterFormButton.addEventListener('click', () => resetValidation(registerForm));
allInputsArr.forEach((input) => input.addEventListener('input', () => setValidation(input)));