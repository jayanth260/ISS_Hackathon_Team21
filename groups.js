


const form = document.querySelector('form');
const numPeopleInput = document.querySelector('#num-people');
const peopleInputsDiv = document.querySelector('#people-inputs');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const numPeople = Number(numPeopleInput.value);
  peopleInputsDiv.innerHTML = '';
  for (let i = 1; i <= numPeople; i++) {
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
  
  const submitButton = document.getElementsByClassName('.sub')[0];
  peopleInputsDiv.appendChild(submitButton);
  peopleInputsDiv.remove();
});










