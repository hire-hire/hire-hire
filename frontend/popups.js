const page = document.querySelector('.page');
const popups = page.querySelectorAll('.popup');
const authButton = page.querySelector('.header__link_type_blue');
const authPopup = page.querySelector('.popup_type_auth');
const revivePasswordPopup = page.querySelector('.popup_type_revive-password');
const registerPopup = page.querySelector('.popup_type_register');
const popupCloseButtons = page.querySelectorAll('.popup__close-btn');
const registerButton = authPopup.querySelector('.form__button_type_register');
const revivePasswordButton = authPopup.querySelector('.form__button_type_forgot');

function closeAllPopups() {
  page.classList.remove('page_disabled');
  popups.forEach(popup => popup.classList.remove('popup_active'));
};

popupCloseButtons.forEach(closeButton => closeButton.addEventListener('click', closeAllPopups));

function openAuthPopup() {
  page.classList.add('page_disabled');
  authPopup.classList.add('popup_active');
}

function openRevivePasswordPopup() {
  closeAllPopups();
  page.classList.add('page_disabled');
  revivePasswordPopup.classList.add('popup_active');
}

function openRegisterPopup() {
  closeAllPopups();
  page.classList.add('page_disabled');
  registerPopup.classList.add('popup_active');
}

authButton.addEventListener('click', openAuthPopup);
registerButton.addEventListener('click', openRegisterPopup);

// Revive Passwor Popup

const emailLabel = revivePasswordPopup.querySelector('.form__label_type_email');
const passwordLabel = revivePasswordPopup.querySelector('.form__label_type_password');
const repeatPasswordLabel = revivePasswordPopup.querySelector('.form__label_type_repeat-password');
const infoText = revivePasswordPopup.querySelector('.form__info');

function changeReviveFormInputs() {
  if (emailLabel.classList.contains('form__label_type_visible')) {
    emailLabel.classList.remove('form__label_type_visible');
    passwordLabel.classList.add('form__label_type_visible');
    repeatPasswordLabel.classList.add('form__label_type_visible');
  } else {
    emailLabel.classList.remove('form__label_type_visible');
    passwordLabel.classList.remove('form__label_type_visible');
    repeatPasswordLabel.classList.remove('form__label_type_visible');
    infoText.classList.add('form__info_type_visible');
  }
}

popups.forEach((popup) => {
  popup.addEventListener('click', (e) => {
    if(e.target.classList.contains('popup_active')) {
      closeAllPopups();
    };
  });
  
});
