import json
import sys
import os

def generate_html(quiz_data):
    title = quiz_data["title"]
    description = quiz_data["description"]
    questions = quiz_data["questions"]
    answer_key = quiz_data["answer_key"]

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{description}" />
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&family=Open+Sans:wght@300;400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/quiz_word.css" />
</head>
<body>
  <div class="container">
    <div class="quiz-section">
      <h1>{title}</h1>
      <p>{description}</p>
"""

    for question in questions:
        # Accessing the question text
        question_text = question.get('question', question.get('text', 'Question Text Missing'))
        html += f"""
      <h3>{question['title']}</h3>
      <p>{question_text}</p>
      <ul>
"""
        for option in question['options']:
            html += f"""
        <li><input type="radio" name="{question['id']}" value="{option['label']}"> {option['label']}) <em>{option['text']}</em></li>
"""
        html += """
      </ul>
"""
    
    html += """
      <button class="quiz-button" id="submitQuiz">Submit Quiz</button>
    </div>

    <div id="results" style="display:none;">
      <h2>Your Results</h2>
      <p id="score"></p>
    </div>
  </div>

  <script>
    // Define correct answers globally
    const answers = {
"""
    
    for question_id, answer in answer_key.items():
        html += f"""
      {question_id}: '{answer}',"""
    
    html += """
    };
  </script>
  <script src="assets/js/quiz_word.js"></script>
</body>
</html>
"""
    return html


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_html.py <quiz_data.json>")
        sys.exit(1)

    input_json_file = sys.argv[1]

    # Ensure the input file has a .json extension
    if not input_json_file.endswith('.json'):
        print("Error: Input file should have a .json extension.")
        sys.exit(1)

    # Read JSON data
    with open(input_json_file, "r") as file:
        quiz_data = json.load(file)

    # Generate HTML content
    html_content = generate_html(quiz_data)

    # Get the base name of the input file (without extension)
    base_name = os.path.splitext(input_json_file)[0]

    # Output HTML to a file with the same base name but .html extension
    output_html_file = f"{base_name}.html"
    with open(output_html_file, "w") as output_file:
        output_file.write(html_content)

    print(f"HTML file generated successfully: {output_html_file}")


if __name__ == "__main__":
    main()
