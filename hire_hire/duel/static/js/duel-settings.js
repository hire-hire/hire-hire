const settingsForm = document.querySelector('.duel-settings__form');
const settingsInputs = settingsForm.querySelectorAll('.duel-settings__input');
const settngsFormButton = settingsForm.querySelector('.duel-settings__button');

const checkValidation = () => {
    const isFormValid = settingsForm.checkValidity();
    console.log(isFormValid)
    if (isFormValid) {
        settngsFormButton.style.opacity = 1;
        settngsFormButton.disabled = false;
    } else {
        settngsFormButton.style.opacity = 0.3;
        settngsFormButton.disabled = true;
    }
    ;
};

settingsInputs.forEach((input) => {
    input.setAttribute('minlength', '2');
    input.setAttribute('maxlength', '20');
    input.setAttribute('required', 'true');
    input.addEventListener('input', checkValidation);
});

checkValidation();
