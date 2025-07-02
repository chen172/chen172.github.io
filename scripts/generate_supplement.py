import sys

def read_file(file_name):
    """Reads the content of a file and returns a list of lines."""
    with open(file_name, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def generate_html(words, prs, audio, definitions, title):
    """Generates the HTML content using the words, pronunciations, audio files, and definitions."""
    
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../assets/css/supplement.css"> <!-- Linking the external CSS -->
</head>

<body>
    <table>
        <thead>
            <tr>
                <th>Word</th>
                <th>Pronunciation</th>
                <th>Audio</th>
                <th>Definition</th>
            </tr>
        </thead>

        <tbody>
    """

    # Loop through the words and generate the table rows
    rows = ""
    for word, pron, audio_file, definition in zip(words, prs, audio, definitions):
        pronunciation = f"[{pron}]"
        audio_path = f"audio/{audio_file}.mp3"  # Assuming the audio filename is {word}001.mp3
        row = f"""
            <tr>
                <td class="word">{word}</td>
                <td class="pronunciation">{pronunciation}</td>
                <td class="audio-control">
                    <audio controls>
                        <source src="{audio_path}" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </td>
                <td class="definition">{definition}</td>
            </tr>
        """
        rows += row

    # Closing the table and body tags
    html_template += rows + """
        </tbody>
    </table>

</body>
</html>
"""
    return html_template

def main():
    # Ensure the correct number of arguments is passed
    if len(sys.argv) != 2:
        print("Usage: python generate_supplement.py session1_supplement.txt")
        sys.exit(1)
    
    # Read the session file path from the argument
    session_file = sys.argv[1]
    
    # Extract the base name (e.g., session1_supplement)
    session_base = session_file.split('.')[0]
    
    # Use the base name to create the title by replacing underscores with spaces
    title = session_base.replace('_', ' ').capitalize()
    
    # File paths for pronunciations, audio files, and definitions
    prs_file = f"prs_{session_base}.txt"
    audio_file = f"audio_{session_base}.txt"
    def_file = f"def_{session_base}.txt"
    
    # Read the content of all files
    words = read_file(session_file)  # Words from session file
    prs = read_file(prs_file)  # Pronunciations
    audio = read_file(audio_file)  # Audio filenames
    definitions = read_file(def_file)  # Definitions
    
    # Generate the HTML content
    html_content = generate_html(words, prs, audio, definitions, title)
    
    # Output the generated HTML to a file
    output_file = f"{session_base}.txt.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML file '{output_file}' generated successfully.")

if __name__ == "__main__":
    main()
