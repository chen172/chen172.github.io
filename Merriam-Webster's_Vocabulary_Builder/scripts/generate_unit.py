import json
import os
import sys

def generate_html(base_name):
    # Construct file names based on the base name
    json_file = f"def_root_{base_name}.json"
    words_file = f"{base_name}.txt"
    phonetic_file = f"prs_{base_name}.txt"
    audio_file = f"audio_{base_name}.txt"

    # Check if the required files exist
    for file in [json_file, words_file, phonetic_file, audio_file]:
        if not os.path.exists(file):
            print(f"Error: The file {file} does not exist.")
            sys.exit(1)

    # Read the JSON data (roots and definitions)
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Read words from the words file (Unit1.txt, etc.), skipping lines starting with '#'
    with open(words_file, 'r', encoding='utf-8') as f:
        words = [line for line in f.read().splitlines() if not line.startswith('#')]

    # Read phonetic pronunciations from the phonetic file (prs_Unit1.txt, etc.)
    with open(phonetic_file, 'r', encoding='utf-8') as f:
        phonetics = f.read().splitlines()

    # Read audio file names from the audio file (audio_Unit1.txt, etc.)
    with open(audio_file, 'r', encoding='utf-8') as f:
        audios = f.read().splitlines()

    # Format the unit title to include a space after "Unit" (e.g., "Unit 1")
    unit_title = f"Unit {base_name.lstrip('Unit')}"

    # Create the HTML content
    html_content = f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{unit_title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/unit.css">
</head>

<body>
'''

    word_index = 0  # This will track the current index for words, phonetics, and audio

    # Iterate over each root in the JSON data
    for entry in data:
        root = entry["root"]
        definition = entry["def"]
        count = entry["count"]
        # Replace '/' with '_' in the root name to generate valid filenames
        audio_filename = f"root/def_{root.replace('/', '_')}.wav"

        # Root Section
        html_content += f'''
    <!-- Root Section for "{root}" -->
    <div class="root-section">
        <div class="text" id="{root}">
            <p><strong>{root}</strong> {definition}</p>
        </div>
        <audio controls>
            <source src="{audio_filename}" type="audio/mpeg">
            Browser not supported audio.
        </audio>
    </div>
'''

        # Table Section for the Root
        html_content += f'''
    <!-- Table for {root}-related Words -->
    <table>
        <colgroup>
            <col />
            <col />
        </colgroup>
        <thead>
            <tr>
                <th>Word</th>
                <th>Phonetic</th>
                <th>Audio</th>
            </tr>
        </thead>
        <tbody>
'''

        # Add the related words, phonetic, and audio based on the count value for the current root
        for i in range(count):
            if word_index < len(words):
                word = words[word_index]
                phonetic = phonetics[word_index] if word_index < len(phonetics) else f"[{word}-phonetic]"
                audio_src = audios[word_index]
                
                html_content += f'''
                <tr>
                    <td>{word}</td>
                    <td>{phonetic}</td>
                    <td>
                        <audio controls>
                            <source src="audio/{audio_src}.mp3" type="audio/mpeg">
                            Browser not supported audio.
                        </audio>
                    </td>
                </tr>
'''
                word_index += 1  # Move to the next word, phonetic, and audio

        # Close the table
        html_content += '''
        </tbody>
    </table>
'''

    # Close the HTML tags
    html_content += '''
</body>

</html>
'''

    # Save the generated HTML to a file
    output_filename = f"{base_name}.txt.html"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML file generated successfully: {output_filename}")

# Main function to read the base name from command line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_html.py <base_name>")
        sys.exit(1)

    base_name = sys.argv[1]

    # Generate the HTML file
    generate_html(base_name)
