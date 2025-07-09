import json
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("❌ Please provide the input JSON file name.")
        print("👉 Example: python generate_quiz_html.py quiz_data.json")
        return

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"❌ File not found: {input_file}")
        return

    if not input_file.endswith(".json"):
        print("❌ Input file must be a JSON file.")
        return

    output_file = os.path.splitext(input_file)[0] + ".html"

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    part1_ids = []
    part2_ids = []

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{data["quiz_title"]}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/choices.js/public/assets/styles/choices.min.css" />
  <link rel="stylesheet" href="assets/css/quiz_root.css" />
</head>
<body>
  <div class="quiz-container">
    <h1>{data["quiz_title"]}</h1>
"""

    # Part 1
    part1 = data["parts"][0]
    html += f"""
    <section class="quiz-section">
      <h2>{part1["title"]}</h2>
      <form id="part1Form">
        <div class="quiz-group" id="part1-questions">
"""

    for q in part1["questions"]:
        label, term = q["item"].split(". ", 1)
        select_id = term.lower().replace("-", "").strip()  # Remove hyphens in term
        part1_ids.append(select_id)
        html += f"""          <label>{label}. <strong>{term}</strong><select id="{select_id}"></select></label>\n"""

    html += """
        </div>
        <button type="button" onclick="checkPart1()">Submit Part 1</button>
      </form>
    </section>
"""

    # Part 2
    part2 = data["parts"][1]
    html += f"""
    <section class="quiz-section">
      <h2>{part2["title"]}</h2>
      <form id="part2Form">
        <div class="quiz-group" id="part2-questions">
"""

    for i, q in enumerate(part2["questions"], start=1):
        word = q["word"]
        structure = q["prefix_root_suffix"]
        part2_ids.append(word)
        html += f"""          <label>{i}. <strong>{word}</strong> <em>({structure})</em><select id="{word}"></select></label>\n"""

    html += """
        </div>
        <button type="button" onclick="checkPart2()">Submit Part 2</button>
      </form>
    </section>
"""

    # Part 3
    part3 = data["parts"][2]
    html += f"""
    <section class="quiz-section">
      <h2>{part3["title"]}</h2>
      <div class="question-block">
"""

    for i, q in enumerate(part3["questions"], start=1):
        html += f"""        <label for="part3q{i}">Q{i}: {q["question"]}</label>\n"""
        html += f"""        <p><em>Example: {q["example"]}</em></p>\n"""
        html += f"""        <textarea id="part3q{i}" placeholder="{q["user_input_placeholder"]}"></textarea>\n\n"""

    html += """
        <button type="button" onclick="checkPart3()">Submit Part 3</button>
      </div>
    </section>
    <div id="result" class="result"></div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/choices.js/public/assets/scripts/choices.min.js"></script>
  <script src="assets/js/quiz_root.js"></script>
  <script>
"""

    # JS options for Part 1
    html += "    const optionsPart1 = [\n"
    part1_answers = {}
    for i, q in enumerate(part1["questions"], start=1):
        html += f'      {{ value: {i}, text: "{q["meaning"]}" }},\n'
        # Fix: Remove hyphen and special characters for part1 answers
        key = q["item"].split(". ")[1].lower().strip().replace("-", "")  # Remove hyphens
        part1_answers[key] = i
    html += "    ];\n\n"

    # JS options for Part 2
    html += "    const optionsPart2 = [\n"
    part2_answers = {}
    for i, q in enumerate(part2["questions"], start=1):
        html += f'      {{ value: {i}, text: "{q["definition"]}" }},\n'
        # Fix: Remove hyphen and special characters for part2 answers
        key = q["word"].lower().strip().replace("-", "")  # Remove hyphens
        part2_answers[key] = i
    html += "    ];\n\n"

    # JS function for Part 1 and Part 2 answers
    html += """
    const part1Answers = """ + json.dumps(part1_answers) + """;
    const part2Answers = """ + json.dumps(part2_answers) + """;

    window.onload = function () {
    """

    # Randomize the options for Part 1 and Part 2
    for id in part1_ids:
        html += f'      randomizeOptions("{id}", optionsPart1);\n'
    for id in part2_ids:
        html += f'      randomizeOptions("{id}", optionsPart2);\n'
    html += "    };\n"

    html += """
  </script>
</body>
</html>
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ HTML file '{output_file}' has been generated.")

if __name__ == "__main__":
    main()
