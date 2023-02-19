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
revivePasswordButton.addEventListener('click', openRevivePasswordPopup);

// Revive Passwor Popup

