// Function to randomize the options
function randomizeOptions(selectId, options) {
  const select = document.getElementById(selectId);
  select.innerHTML = '';
  const shuffled = [...options].sort(() => Math.random() - 0.5);
  shuffled.forEach(opt => {
    const o = document.createElement("option");
    o.value = opt.value;
    o.textContent = opt.text;
    select.appendChild(o);
  });

  new Choices(select, {
    searchEnabled: true,
    itemSelectText: '',
    placeholder: true,
    shouldSort: false
  });
}

// Function to set the select style based on correctness
function setSelectStyle(select, isCorrect) {
  const container = select.closest('.choices');
  if (!container) return;
  container.setAttribute('data-state', isCorrect ? 'correct' : 'incorrect');
}

// Function to check answers for Part 1
function checkPart1() {
  let allCorrect = true;
  for (let key in part1Answers) {
    const select = document.getElementById(key);
    const val = parseInt(select.value);
    const correct = val === part1Answers[key];
    setSelectStyle(select, correct);
    if (!correct) allCorrect = false;
  }
  showResult(allCorrect, "Part 1");
}

// Function to check answers for Part 2
function checkPart2() {
  let allCorrect = true;
  for (let key in part2Answers) {
    const select = document.getElementById(key);
    const val = parseInt(select.value);
    const correct = val === part2Answers[key];
    setSelectStyle(select, correct);
    if (!correct) allCorrect = false;
  }
  showResult(allCorrect, "Part 2");
}

// Function to check answers for Part 3
function checkPart3() {
  const q1 = document.getElementById('part3q1').value.trim();
  const q2 = document.getElementById('part3q2').value.trim();
  if (q1 && q2) {
    showMessage("Great! Both answers in Part 3 look good.");
  } else {
    showMessage("Please fill in both fields in Part 3.");
  }
}

// Function to show the result message
function showResult(allCorrect, partName) {
  let resultEl;
  if (partName === "Part 1") {
    resultEl = document.getElementById("resultPart1");
  } else if (partName === "Part 2") {
    resultEl = document.getElementById("resultPart2");
  } else if (partName === "Part 3") {
    resultEl = document.getElementById("resultPart3");
  }

  if (allCorrect) {
    resultEl.textContent = `Great job! All answers in ${partName} are correct.`;
    resultEl.className = "result correct";
  } else {
    resultEl.textContent = `Some answers in ${partName} are incorrect. Try again!`;
    resultEl.className = "result incorrect";
  }
}

// Function to show a message for Part 3
function showMessage(message) {
  const resultEl = document.getElementById("resultPart3");
  resultEl.textContent = message;
  resultEl.className = "result";
}
