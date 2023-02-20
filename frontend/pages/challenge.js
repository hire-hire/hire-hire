const answerTitle = document.querySelector('.challenge__form-title_type_correctly');
const answerText = document.querySelector('.challenge__form-text_type_correctly');
const challengeFormButton = document.querySelector('.challenge__form-button_type_button');
const challenFormLink = document.querySelector('.challenge__form-button_type_link');

console.log(challengeFormButton, challenFormLink)

function showAnswer() {
  answerTitle.classList.add('challenge__form-title_type_visible');
  answerText.classList.add('challenge__form-text_type_visible');
  challengeFormButton.classList.remove('challenge__form-button_type_visible');
  challenFormLink.classList.add('challenge__form-button_type_visible');
}

challengeFormButton.addEventListener('click', showAnswer);