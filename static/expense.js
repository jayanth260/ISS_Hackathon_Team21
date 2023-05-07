
var speed = 100;
var i = 0;
var txt = document.getElementById('welcome');
var text = txt.innerText; 
txt.innerText = "";

function typeWriter() {
  if (i < text.length) {
    if (text[i] === " ") {
      document.getElementById("welcome").innerHTML +='&nbsp;';
    } else {
      document.getElementById("welcome").innerText += text[i];
    }
    i++;
    setTimeout(typeWriter, speed);
  }
}
typeWriter();

const form = document.querySelector('form');
const numPeopleInput = document.querySelector('#num-people');
const peopleInputsDiv = document.querySelector('#people-inputs');
const submitButton = document.querySelector('.sub');

function generateInputs() {
  const numPeople = Number(numPeopleInput.value);
  peopleInputsDiv.innerHTML = '';
  for (let i = 1; i <= numPeople-1; i++) {
    const div = document.createElement('div');
    div.className = 'noppl';
    const input = document.createElement('input');
    input.type = 'text';
    input.name = `person${i}`;
    input.placeholder = 'Enter user name';
    input.required = true;

    div.appendChild(input);

    peopleInputsDiv.appendChild(div);
  }
}

numPeopleInput.addEventListener('input', () => {
  generateInputs();
  submitButton.disabled = true;
});

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(event.target);
  fetch('/addexgr', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    if (data.success) {
      // Show success message
      alert(data.message);
      // Clear the form inputs
      event.target.reset();
    } else {
      // Show error message
    //   alert(data.error);
    }
  })
  .catch(error => {
    console.error(error);
  });
});

peopleInputsDiv.addEventListener('input', () => {
  const inputs = peopleInputsDiv.querySelectorAll('input');
  let allFilled = true;
  inputs.forEach(input => {
    if (!input.value) {
      allFilled = false;
    }
  });
  submitButton.disabled = !allFilled;
});

