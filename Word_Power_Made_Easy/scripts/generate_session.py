import sys
import os

def read_lines_strip(filename):
    with open(filename, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_html.py session1.txt")
        sys.exit(1)

    base_file = sys.argv[1]

    base_dir = os.path.dirname(base_file)
    base_name = os.path.basename(base_file)

    phonetic_file = os.path.join(base_dir, f"prs_{base_name}")
    audio_file = os.path.join(base_dir, f"audio_{base_name}")

    if not os.path.exists(base_file):
        print(f"Word file '{base_file}' not found.")
        sys.exit(1)
    if not os.path.exists(phonetic_file):
        print(f"Phonetic file '{phonetic_file}' not found.")
        sys.exit(1)
    if not os.path.exists(audio_file):
        print(f"Audio file '{audio_file}' not found.")
        sys.exit(1)

    words = read_lines_strip(base_file)
    phonetics = read_lines_strip(phonetic_file)
    audios = read_lines_strip(audio_file)

    if not(len(words) == len(phonetics) == len(audios)):
        print(f"ERROR: Lines count mismatch between files.")
        print(f"Words: {len(words)}, Phonetics: {len(phonetics)}, Audios: {len(audios)}")
        sys.exit(1)

    entries_js = []
    for w, p, a in zip(words, phonetics, audios):
        if not (p.startswith('[') and p.endswith(']')):
            p = f'[{p}]'
        audio_path = f"audio/{a}.mp3"
        entries_js.append(f"  {{ word: '{w}', phonetic: '{p}', audio: '{audio_path}' }}")

    entries_str = ",\n".join(entries_js)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Session 1</title>
  <link href="assets/css/session.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet" />
</head>
<body>
  <div class="button-container">
    <button class="toggle-btn" onclick="toggleLayout()" id="toggleViewBtn">Card View</button>
    <button class="toggle-btn" onclick="playAll()">▶️ Play All</button>
    <button class="toggle-btn" id="playPauseBtn" onclick="togglePlayPause()">⏸️ Pause</button>
    <div class="delay-wrapper" title="Delay between audios in milliseconds">
      <label for="delayInput" style="user-select:none;">Delay (ms):</label>
      <input type="number" id="delayInput" value="500" min="0" />
    </div>
  </div>

  <!-- TABLE VIEW -->
  <table class="table-view" id="tableView" cellspacing="0" cellpadding="0" role="grid" aria-label="Word list table">
    <thead>
      <tr>
        <th scope="col">Word</th>
        <th scope="col">Phonetic</th>
        <th scope="col">Audio</th>
      </tr>
    </thead>
    <tbody id="tableBody"></tbody>
  </table>

  <!-- CARD VIEW -->
  <div class="card-view" id="cardView" role="list"></div>

  <script>
    const entries = [
{entries_str}
    ];
  </script>
  <script src="assets/js/session.js"></script>
</body>
</html>"""

    output_file = base_file.replace('.txt', '.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML file '{output_file}' generated successfully.")

if __name__ == "__main__":
    main()
