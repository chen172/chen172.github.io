import markdown
import re
import sys
import os

# Function to convert Markdown to HTML
def md_to_html(md_text):
    # Convert the markdown text into HTML
    html = markdown.markdown(md_text)
    
    # Handle custom formatting for <code> tags (converted from backticks) and convert them to <span class="quote">
    html = re.sub(r'(<p>)?<code>(.*?)</code>(</p>)?', r'\1<span class="quote">\2</span>\3', html, flags=re.DOTALL)
    
    # Handle image format (optional, as per your example)
    html = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html)

    # Update href links from 'href="asset"' to 'href="../asset"'
    html = re.sub(r'href="asset', r'href="../asset', html)

    # Convert **bold** to <strong> tags inside <span class="quote">
    html = re.sub(r'<span class="quote">(.*?)</span>', lambda match: f'<span class="quote">{re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", match.group(1))}</span>', html)
    
    # Remove the <h1> header (for custom title handling)
    html = re.sub(r'<h1>.*?</h1>', '', html)

    return html

# Function to extract the first h1 header from markdown and return it (title)
def extract_title_from_md(md_text):
    # Look for the first # header in the markdown
    match = re.search(r'# (.*?)\n', md_text)
    if match:
        return match.group(1)  # Return the content of the first # header
    else:
        return "The Moonlit Adventure"  # Default title if no h1 is found

# Read Markdown from file passed as argument
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Write the converted HTML to an output file
def write_html_to_file(html_content, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python md_to_html.py <input_md_file>")
        sys.exit(1)
    
    # Input markdown file
    input_md_file = sys.argv[1]
    
    # Read the markdown text
    md_text = read_markdown_file(input_md_file)
    
    # Extract the title from the Markdown (first h1 header)
    title = extract_title_from_md(md_text)
    
    # Convert the markdown to HTML
    html_content = md_to_html(md_text)
    
    # Generate the output HTML filename based on the input filename
    base_name = os.path.splitext(input_md_file)[0]  # Remove .md extension
    output_file = f'{base_name}.html'  # Add .html extension
    
    # HTML structure with header and footer
    html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="../../assets/css/story.css" />
    </head>
    <body>
    <h1>{title}</h1>
    {html_content}

    <footer>
        <p>&copy; 2025 {title} - A story designed to help you explore and learn new vocabulary!</p>
    </footer>

    </body>
    </html>
    """
    
    # Write the HTML to the dynamically generated file
    write_html_to_file(html_output, output_file)
    print(f"HTML content has been written to {output_file}")

# Run the main function
if __name__ == '__main__':
    main()
