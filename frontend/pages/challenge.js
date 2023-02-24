const answerTitle = document.querySelector('.challenge__form-title_type_correctly');
const answerText = document.querySelector('.challenge__form-text_type_correctly');
const challengeFormButton = document.querySelector('.challenge__form-button_type_button');
const challengeFormLink = document.querySelector('.challenge__form-button_type_link');
const challengeNextButton = document.querySelector('.challenge__form-button_type_next');
const questionsAnswersNodesArr = document.querySelectorAll('.challenge__qa');
const questionsLength = document.querySelector('.questions__length');
const questionText = document.querySelector('.challenge__form-text_type_question');
const questionCounter = document.querySelector('.questions__counter');
const textArea = document.querySelector('.challenge__form-input');
const challengeForm = document.querySelector('.challenge__form');

textArea.setAttribute('maxlength', '400');
textArea.setAttribute('minlength', '2');
textArea.setAttribute('required', 'true');

const formValidation = () => {
  const isFormValid = challengeForm.checkValidity();
  if(isFormValid) {
    challengeFormButton.disabled = false;
    challengeFormButton.style.opacity = 1;
  } else {
    challengeFormButton.disabled = true;
    challengeFormButton.style.opacity = 0.4;
  };
};

formValidation();
textArea.addEventListener('input', formValidation);

(() => questionsLength.textContent = questionsAnswersNodesArr.length)();

let questionsAnswersArr = [];

questionsAnswersNodesArr.forEach((qa) => {
  const qaArr = qa.textContent.split('?');
  questionsAnswersArr.push({question: qaArr[0], answer: qaArr[1]});
});

let counter = 0;

function setQA() {
  questionText.textContent = questionsAnswersArr[counter].question;
  answerText.textContent = questionsAnswersArr[counter].answer;
};

setQA();

function setQuestionCounter() {
  questionCounter.textContent = counter + 1;
};

setQuestionCounter();

function showAnswer() {
  answerTitle.classList.add('challenge__form-title_type_visible');
  answerText.classList.add('challenge__form-text_type_visible');
  challengeFormButton.classList.remove('challenge__form-button_type_visible');
  if(counter === questionsAnswersArr.length - 1) {
    challengeFormLink.classList.add('challenge__form-button_type_visible');
  } else {
    challengeNextButton.classList.add('challenge__form-button_type_visible');
  }
  counter = counter + 1;
}

function nextQuestion() {
  answerTitle.classList.remove('challenge__form-title_type_visible');
  answerText.classList.remove('challenge__form-text_type_visible');
  challengeFormButton.classList.add('challenge__form-button_type_visible');
  challengeFormLink.classList.remove('challenge__form-button_type_visible');
  challengeNextButton.classList.remove('challenge__form-button_type_visible');
  setQA();
  setQuestionCounter();
}

challengeFormButton.addEventListener('click', showAnswer);
challengeNextButton.addEventListener('click', nextQuestion);