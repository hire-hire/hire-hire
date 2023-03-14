const duelForm = document.querySelector('.duel__form');
const duelInputsArr = duelForm.querySelectorAll('.duel__radio');
const duelPlayersContainer = document.querySelector('.duel__players');

duelPlayersContainer.style.gridTemplateColumns = '1fr 128px 1fr';
duelPlayersContainer.style.gap = '32px';
duelInputsArr[2].setAttribute('checked', 'true');
