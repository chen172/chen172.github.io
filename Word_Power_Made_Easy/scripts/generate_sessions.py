import os
import subprocess

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, ".."))
words_dir = os.path.join(project_root, "words", "book")
generate_script = os.path.join(script_dir, "generate_session.py")

# Find all session*.txt files
session_files = sorted([
    f for f in os.listdir(words_dir)
    if f.startswith("session") and f.endswith(".txt") and not f.startswith("prs_") and not f.startswith("audio_")
])

if not session_files:
    print("No session*.txt files found in words/book/")
    exit(1)

print(f"Found {len(session_files)} sessions. Generating HTML files...")

for session_file in session_files:
    input_path = os.path.join(words_dir, session_file)
    print(f"Generating HTML for {session_file}...")
    try:
        subprocess.run(
            ["python", generate_script, input_path],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error processing {session_file}: {e}")
        continue

print("All sessions processed.")
