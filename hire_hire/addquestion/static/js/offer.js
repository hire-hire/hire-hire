const offerForm = document.querySelector('.offer__form');
const answerField = offerForm.querySelector('#answer');
const questionField = offerForm.querySelector('#question');
const answerHint = offerForm.querySelector('#answerHint');
const questionHint = offerForm.querySelector('#questionHint');
const submitButton = offerForm.querySelector('.offer__button');
const questionError = offerForm.querySelector('#questionError');
const answerError = offerForm.querySelector('#answerError');

const formValidation = () => {
  const isFormValid = offerForm.checkValidity();
  if(isFormValid) {
    submitButton.classList.remove('offer__button_type_disabled');
    submitButton.disabled = false;
  } else {
    submitButton.classList.add('offer__button_type_disabled');
    submitButton.disabled = true;
  };
};

const answerFieldHandler = () => {
  formValidation();
  answerHint.textContent = `${answerField.value.length} / 10-500`;
  const isTextareaValid = answerField.validity.valid;
  if(isTextareaValid) {
    answerField.classList.remove('offer__textarea_type_error');
    answerError.classList.remove('offer__error_type_visible');
    answerError.textContent = '';
  } else {
    answerField.classList.add('offer__textarea_type_error');
    answerError.textContent = answerField.validationMessage;
    answerError.classList.add('offer__error_type_visible');
  };
};

const questionFieldHandler = () => {
  formValidation();
  questionHint.textContent = `${questionField.value.length} / 10-500`;
  const isTextareaValid = questionField.validity.valid;
  if(isTextareaValid) {
    questionField.classList.remove('offer__textarea_type_error');
    questionError.classList.remove('offer__error_type_visible');
    questionError.textContent = '';
  } else {
    questionField.classList.add('offer__textarea_type_error');
    questionError.textContent = questionField.validationMessage;
    questionError.classList.add('offer__error_type_visible');
  };
};

answerField.addEventListener('input', answerFieldHandler);
questionField.addEventListener('input', questionFieldHandler);