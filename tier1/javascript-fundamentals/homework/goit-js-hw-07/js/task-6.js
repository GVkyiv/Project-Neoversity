function getRandomHexColor() {
  return `#${Math.floor(Math.random() * 16777215)
    .toString(16)
    .padStart(6, 0)}`;
}

const input = document.querySelector('#controls input');
const createButton = document.querySelector('[data-create]');
const destroyButton = document.querySelector('[data-destroy]');
const boxes = document.querySelector('#boxes');

createButton.addEventListener('click', () => {
  const amount = Number(input.value);

  if (amount < 1 || amount > 100) {
    return;
  }

  destroyBoxes();
  createBoxes(amount);
  input.value = '';
});

destroyButton.addEventListener('click', destroyBoxes);

function createBoxes(amount) {
  const boxesMarkup = [];

  for (let i = 0; i < amount; i += 1) {
    const size = 30 + i * 10;

    boxesMarkup.push(
      `<div style="width: ${size}px; height: ${size}px; background-color: ${getRandomHexColor()}"></div>`
    );
  }

  boxes.insertAdjacentHTML('beforeend', boxesMarkup.join(''));
}

function destroyBoxes() {
  boxes.innerHTML = '';
}
