from bs4 import BeautifulSoup
import json

with open('outputnew1.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

data = []

for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    title = heading.get_text().strip()
    paragraphs = []
    next_element = heading.next_sibling
    while next_element and next_element.name != heading.name:
        if next_element.name == 'p':
            paragraph = next_element.get_text().strip()
            paragraphs.append(paragraph)
        next_element = next_element.next_sibling
    
    if paragraphs:
        concatenated_context = ' '.join(paragraphs)
        single_context_data = {
            'title': title,
            'context': concatenated_context
        }
        data.append(single_context_data)

json_data = json.dumps({'data': data}, indent=2)

with open('output_context1.json', 'w') as file:
    file.write(json_data)
