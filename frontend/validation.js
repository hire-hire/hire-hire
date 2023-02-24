const authForm = document.querySelector('.form_type_auth');
const registerForm = document.querySelector('.form_type_register');
const openAuthFormButton = document.querySelector('.header__link_type_blue');
const openRegisterFormButton = document.querySelector('.form__button_type_register');

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
  };
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
  };
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

  if(input.name === 'password' && input.value === emailInput.value) {
    isInputValid = false;
  };

  if (isInputValid) {
    hideError(input, closestForm);
  } else {
    showError(input, closestForm);
  };
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
  };
  if (input.type === 'email') {
    input.setAttribute('maxlength', '150');
    input.setAttribute('minlength', '2');
  }
});

const inputContainerArr = registerForm.querySelectorAll('.form__input-container');
inputContainerArr.forEach((inputContainer) => {
  const input = inputContainer.querySelector('.form__input');
  const hintElement = inputContainer.querySelector('.form__label-hint');
  if(input.name === 'email') {
  } else {
  }
})


openAuthFormButton.addEventListener('click', () => resetValidation(authForm));
openRegisterFormButton.addEventListener('click', () => resetValidation(registerForm));
allInputsArr.forEach((input) => input.addEventListener('input', () => setValidation(input)));