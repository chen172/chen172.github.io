document.getElementById('submitQuiz').addEventListener('click', function () {
  let score = 0;

  // Get all question elements dynamically
  const totalQuestions = Object.keys(answers).length; // Get the total number of questions
  
  // Loop through each question and check the answers
  for (let i = 1; i <= totalQuestions; i++) {
    const selected = document.querySelector(`input[name="q${i}"]:checked`);
    if (selected && selected.value === answers[`q${i}`]) {
      score++;
    }
  }

  // Display results
  const resultsElement = document.getElementById('results');
  const scoreElement = document.getElementById('score');

  // If the user answered all questions correctly
  if (score === totalQuestions) {
    scoreElement.innerHTML = `
      <span class="congratulations-icon">🏆</span>
      <span class="congratulations-text">Congratulations! You got all the questions correct!</span>
    `;
    scoreElement.classList.add('congratulations');
  } else {
    scoreElement.innerHTML = `You got ${score} out of ${totalQuestions} questions correct!`;
    scoreElement.classList.remove('congratulations');
  }

  // Show results section
  resultsElement.style.display = 'block';

  // Scroll to results
  resultsElement.scrollIntoView({ behavior: 'smooth' });
});
