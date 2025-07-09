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

function setSelectStyle(select, isCorrect) {
  const container = select.closest('.choices');
  if (!container) return;
  container.setAttribute('data-state', isCorrect ? 'correct' : 'incorrect');
}

function checkPart1() {
  const answers = {
    cap: 1, anthrop: 2, mis: 3, lyc: 4, re: 5,
    de: 6, ate: 7, ology: 8, oid: 9, ic: 10
  };
  let allCorrect = true;
  for (let key in answers) {
    const select = document.getElementById(key);
    const val = parseInt(select.value);
    const correct = val === answers[key];
    setSelectStyle(select, correct);
    if (!correct) allCorrect = false;
  }
  showResult(allCorrect, "Part 1");
}

function checkPart2() {
  const answers = {
    rejuvenate: 1, misdirect: 2, deforest: 3, recap: 4,
    anthropocentric: 5, lycanthropist: 6, capitulation: 7, zoophilic: 8
  };
  let allCorrect = true;
  for (let key in answers) {
    const select = document.getElementById(key);
    const val = parseInt(select.value);
    const correct = val === answers[key];
    setSelectStyle(select, correct);
    if (!correct) allCorrect = false;
  }
  showResult(allCorrect, "Part 2");
}

function checkPart3() {
  const q1 = document.getElementById('part3q1').value.trim();
  const q2 = document.getElementById('part3q2').value.trim();
  if (q1 && q2) {
    showMessage("Great! Both answers in Part 3 look good.");
  } else {
    showMessage("Please fill in both fields in Part 3.");
  }
}

function showResult(allCorrect, partName) {
  const resultEl = document.getElementById("result");
  if (allCorrect) {
    resultEl.textContent = `Great job! All answers in ${partName} are correct.`;
    resultEl.className = "result correct";
  } else {
    resultEl.textContent = `Some answers in ${partName} are incorrect. Try again!`;
    resultEl.className = "result incorrect";
  }
}

function showMessage(message) {
  const resultEl = document.getElementById("result");
  resultEl.textContent = message;
  resultEl.className = "result";
}
