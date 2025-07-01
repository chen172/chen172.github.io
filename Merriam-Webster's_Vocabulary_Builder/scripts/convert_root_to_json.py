import sys
import os
import re
import json

def convert_text_to_json(text):
    # Regular expression to match the pattern of the word blocks
    pattern = re.compile(r'<p><strong>(.*?)</strong>(.*?)</p>', re.DOTALL)
    matches = pattern.findall(text)
    
    # Prepare a list to hold all word data
    word_data = []
    
    # A flag to check if "Words from Mythology and History" was added
    words_from_mythology_added = False
    
    # Iterate over the matches and process the content
    for match in matches:
        root = match[0].strip()
        definition = match[1].strip()
        
        # If the definition is empty, just set it to an empty string and count as 8
        if not definition:
            word_data.append({
                "root": root,
                "def": "",
                "count": 8
            })
        else:
            # Clean up the definition, remove extra spaces and preserve HTML tags
            definition = re.sub(r'\s+', ' ', definition)
            
            # Add the word data to the list
            word_data.append({
                "root": root,
                "def": definition,
                "count": 4
            })
    
    return word_data

def process_files_in_directory(directory_path):
    # Iterate through all the files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            # Build the full path of the file
            file_path = os.path.join(directory_path, filename)
            
            # Open and read the file
            with open(file_path, 'r') as file:
                text = file.read()
            
            # Convert the text to JSON
            result = convert_text_to_json(text)
            
            # Define the output filename
            output_filename = os.path.splitext(filename)[0] + '.json'
            output_path = os.path.join(directory_path, output_filename)
            
            # Write the result to a JSON file
            with open(output_path, 'w') as json_file:
                json.dump(result, json_file, indent=4)
            
            print(f"Processed file: {filename} -> {output_filename}")

def main():
    # Check if the directory argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    # Directory path from the command line argument
    directory_path = sys.argv[1]
    
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: The directory {directory_path} does not exist.")
        sys.exit(1)
    
    # Process all files in the directory
    process_files_in_directory(directory_path)

if __name__ == '__main__':
    main()
