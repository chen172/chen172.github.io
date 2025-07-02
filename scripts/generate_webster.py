import os
import json

# Define the output HTML file path and the path to your CSS file
output_html = "Merriam-Webster's_Vocabulary_Builder_Audio.html"
css_link = 'assets/css/webster.css'
js_link = 'assets/js/backToTop.js'  # Path to your external JS file

# Function to generate HTML for each unit
def generate_unit_html(unit_number, json_data):
    """
    Generates the HTML content for a given unit using the provided JSON data.
    """
    unit_name = f"Unit {unit_number}"
    unit_section_html = f'''
    <div class="unit-section">
        <div class="unit-header">
            <a href="Merriam-Webster's_Vocabulary_Builder/Unit{unit_number}.txt.html">{unit_name}</a>
            <a href="Merriam-Webster's_Vocabulary_Builder/Unit{unit_number}_supplement.txt.html">[Supplement]</a>
        </div>
        <table class="unit-table">
            <tbody>
    '''

    # Loop through the roots in the JSON data and generate the table rows (2 roots per row)
    row = []
    for entry in json_data:
        root = entry['root']
        
        # Add the root to the current row
        row.append(f'<td><a href="Merriam-Webster\'s_Vocabulary_Builder/Unit{unit_number}.txt.html#{root}">{root}</a></td>')
        
        # If the row has two roots, add the quiz link and close the row
        if len(row) == 2:
            unit_section_html += f'''
                <tr>
                    {''.join(row)}
                    <td><a href="Merriam-Webster\'s_Vocabulary_Builder/Unit{unit_number}.txt.html#QUIZ">Quiz</a></td>
                </tr>
            '''
            row = []  # Reset the row for the next pair

    # If there's an odd number of roots, add the last one and a quiz link
    if row:
        unit_section_html += f'''
            <tr>
                {''.join(row)}
                <td><a href="Merriam-Webster\'s_Vocabulary_Builder/Unit{unit_number}.txt.html#QUIZ">Quiz</a></td>
            </tr>
        '''

    # Close the unit section HTML
    unit_section_html += '''
            </tbody>
        </table>
    </div>
    '''

    return unit_section_html

# Function to generate the full HTML page
def generate_full_html():
    """
    Generates the full HTML page, including the unit sections and linking to the CSS.
    """
    # Start the HTML page structure
    full_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Merriam-Webster's Vocabulary Builder Audio</title>
        <link rel="icon" href="img/webster.ico" type="image/x-icon">
        <link rel="stylesheet" href="assets/css/webster.css">
        <link rel="stylesheet" href="assets/css/backToTop.css">
    </head>
    <body>
        <div class="container">
    '''

    # Process each unit JSON file from Unit1 to Unit30
    for unit_number in range(1, 31):
        json_file_path = f'def_root_Unit{unit_number}.json'

        # Check if the JSON file exists for the current unit
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            # Generate HTML for the current unit
            unit_html = generate_unit_html(unit_number, json_data)

            # Append the unit HTML to the full page content
            full_html += unit_html
        else:
            print(f"Warning: {json_file_path} not found!")

    # Add Back to Top and Go to Bottom buttons
    full_html += '''
        <a href="#" class="back-to-top">↑</a>
        <a href="#bottom" class="go-to-bottom">↓</a>
    '''

    # Link the external JavaScript file for the Back to Top and Go to Bottom functionality
    full_html += f'''
    <script src="{js_link}"></script>
    '''

    # Add bottom section to be targeted by the Go to Bottom button
    full_html += '''
        <div id="bottom" style="height: 100px;"></div>
    '''

    # Close the HTML body and document
    full_html += '''
        </div> <!-- End container -->
    </body>
    </html>
    '''

    # Write the final HTML to the output file
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
        print(f'Generated: {output_html}')

# Run the function to generate the HTML page
generate_full_html()
